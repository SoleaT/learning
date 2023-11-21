from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, RadioField,SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('passwd', validators=[DataRequired(),
                                                   Length(min=6, max=30, message='Длина пароля - от 6 до 30 символов')])
    submit = SubmitField('Войти')
    def validate_username(self, username):
        if not self.username.data.startswith('usr'):
            raise ValidationError("Имя должно начинаться на usr")


class RegForm(LoginForm):
    confirm_pass = PasswordField('confirm passwd', validators=[DataRequired(), EqualTo('password')])
    email = EmailField('email', validators=[DataRequired(), Email()])
    gender = RadioField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')])
    submit = SubmitField('Зарегистрироваться')

class NewCategory(FlaskForm):
    cat_name=StringField('Новая категория ')
    submit = SubmitField('Создать')