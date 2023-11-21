import os.path

from flask import Flask, render_template, make_response, request, session, abort, redirect, url_for, flash
from models import db, User, Categories, Animal
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
import forms

app = Flask(__name__)
app.session_cookie_secure = True
app.secret_key = '77f05516314fb99ba1481d11528422a75b2f959c01d1bc27224eea6cb4ab3fb4'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

homeworks = [
    {'link': 'homework1', 'img_url': 'images/shop_01.jpg', 'name': 'домашнее задание 1'},
    {'link': 'homework2', 'img_url': 'images/shop_02.jpg', 'name': 'домашнее задание 2'},
    {'link': 'regform', 'img_url': 'images/shop_03.jpg', 'name': 'домашнее задание 3'},
]
context = {}


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('ok')


@app.route('/cookie/')
def del_cook():
    response = make_response('Cookie is set')
    response.delete_cookie('user')
    return response


@app.route('/')
def index():
    context = {'homeworks': homeworks, 'title': 'Учебный проект по курсам Верстка, Flask, fastAPI'}
    response = make_response(render_template('template_index.html', **context))
    # моментальная установка кукисов!
    # if not request.cookies.get('user'):
    #     response.set_cookie('user', 'learn')
    # else:
    #     make_response(f'Cookie: {request.cookies.get("user")}')
    return response


@app.errorhandler(404)
def page404(e):
    return render_template('404.html', err_num='404', err_text='Страница не найдена'), 404


@app.errorhandler(500)
def page500(e):
    return render_template('404.html', err_num='500', err_text='Ошибка сервера'), 500


@app.route('/adm_category')
def list_categories():
    categories = Categories.query.all()
    context['cats'] = categories
    return render_template('template_categories.html', create=False, **context)


@app.route('/create_category')
def create_cat():
    form = forms.NewCategory()
    return render_template('template_categories.html', create=True, form=form)


@app.post('/do_create_cat')
@csrf.exempt
def creating_cat():
    form = forms.NewCategory()
    if form.cat_name.data:
        count = len(Categories.query.all())
        new_cat = Categories(cat_name=form.cat_name.data, cat_link='cat' + str(count),
                             cat_image='images/shop_0' + str(count + 1) + '.jpg')
        db.session.add(new_cat)
        db.session.commit()
    return redirect(url_for('list_categories'))

@app.route('/delete_cat/<int:id_cat>')
def delete_cat(id_cat):
    cat=Categories.query.filter_by(id=id_cat).first()
    print(cat)
    db.session.delete(cat)
    db.session.commit()
    return redirect(url_for('list_categories'))

@app.route('/homework1/<string:animal>')
@app.route('/homework1/')
def homework1(animal=False):
    categories = [
        {'link': 'lizards', 'name': 'Ящерицы', 'img_url': 'images/shop_01.jpg'},
        {'link': 'dragons', 'name': 'Драконы', 'img_url': 'images/shop_02.jpg'},
        {'link': 'efts', 'name': 'Тритоны', 'img_url': 'images/shop_03.jpg'},
        {'link': 'danger', 'name': 'ОПАСНОСТЬ!', 'img_url': 'images/shop_04.jpg'},
    ]
    context['title'] = 'Домашнее задание 1 - интернет магазин, шаблон'
    if not animal:
        context['shop_title'] = 'Интернет-магазин'
        context['shop_description'] = 'Редкие сказочные животные со всего мира'
        context['categories'] = categories
        return render_template('template_shop.html', **context)
    else:
        flag = any(animal in i.values() for i in categories)
        if not flag:
            return abort(404)
        context['shop_title'] = 'Карточка товара'
        context['info'] = {'img_url': 'images/prob.jpg', 'name': 'Ящерка-элементаль',
                           'text': ['пыхает огнём', 'быстро бегает', 'голубого цвета'], 'price': 150000000}
        return render_template('template_shop_page.html', **context)


@app.route('/homework2')
def homework2():
    username = request.cookies.get('username')
    if username and username in session.values():
        context['name'] = username
        context['email'] = session['email']
        context['user'] = True
        return render_template('template_user.html', **context)
    else:
        return redirect(url_for('login'))


@app.route('/homework3')
def homework3():
    username = request.cookies.get('username')
    if username and username in session.values():
        users = User.query.filter(User.username == username).all()
        if users and users[0].email == session['email']:
            context['name'] = username
            context['email'] = session['email']
            context['user'] = True
            context['gender'] = 'Женщина' if users[0].usergender == True else 'Мужчина'
            return render_template('template_user.html', **context)

    return redirect(url_for('login'))


@app.route('/regform')
def regform():
    form = forms.RegForm()
    return render_template('template_regform.html', form=form)


@app.post('/register')
def new_user():
    form = forms.RegForm()
    username = form.username.data
    useremail = form.email.data
    responce = make_response(redirect(url_for('homework3')))
    if form.validate():
        if User.query.filter(User.username == username).all() or User.query.filter(User.email == useremail).all():
            flash('Пользователь уже существует,залогиньтесь', 'warning')
            form = forms.LoginForm
            return render_template('template_user.html', user=False, form=form)
        else:
            user_gender = True if form.gender.data == 'female' else False
            flash('Регистрация успешна', 'success')
            new_user = User(username=username, email=useremail,
                            passwd=generate_password_hash(str(form.password.data)), usergender=user_gender)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            session['email'] = useremail
            responce.set_cookie('username', username)
    else:
        return render_template('template_regform.html', form=form)
    return responce


@app.route('/auth', methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    if request.method == "POST" and form.validate():
        username = form.username.data
        userpaswd = form.password.data
        if not username:
            if not userpaswd:
                flash('Не введены имя и пароль', 'warning')
            else:
                flash('Не введено имя', 'warning')
        else:
            users = User.query.filter(User.username == username).all()
            print(users)
            if users:
                if check_password_hash(users[0].passwd, userpaswd):
                    session['username'] = username
                    session['email'] = users[0].email
                    responce = make_response(redirect(url_for('homework3')))
                    responce.set_cookie('username', username)
                    flash('Авторизация пройдена', 'success')
                    return responce
                else:
                    flash('Пароль неверный', 'danger')
            else:
                flash('Такого пользователя не существует', 'danger')
    return render_template('template_user.html', user=False, form=form)


@app.route('/logout')
def logout():
    session.pop('username', None)
    responce = make_response(redirect(url_for('homework2')))
    responce.delete_cookie('username')
    flash('Выход выполнен', 'success')
    return responce


if __name__ == '__main__':
    app.run(debug=True)
