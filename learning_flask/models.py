from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    passwd = db.Column(db.String(30), nullable=False)
    usergender = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean, default=True)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cat_name = db.Column(db.String(80), unique=True, nullable=False)
    cat_link = db.Column(db.String(80), unique=True, nullable=False)
    cat_image = db.Column(db.String(200))


class Animal(db.Model):
    id_rep = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    cat = db.Column(db.Integer, db.ForeignKey('categories.id'))
