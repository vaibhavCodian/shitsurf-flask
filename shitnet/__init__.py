from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)


ENV = 'prod'

app.config['SECRET_KEY'] = 'a5f21203f2c64b4dcea2fbec31723edd'

if ENV == 'dev':    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uushrpjwsxyhol:2683e641bd0159e6aefc7547e5495dd12db0012bfafb19bc48b3b86127702d2f@ec2-54-227-250-19.compute-1.amazonaws.com:5432/deqkuq8n66h1rt'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
LoginManager.login_message_catagory = 'info'

from shitnet import routes