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
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vmpjgckmtjwgxr:2d14a8c7090990980490e1b43eb9d1e3bb27dda5a17405d3f5b2a917d0fc5bc0@ec2-174-129-254-218.compute-1.amazonaws.com:5432/dsqnofkns97f'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
LoginManager.login_message_catagory = 'info'

from shitnet import routes