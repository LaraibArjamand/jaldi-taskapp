from os import environ

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URI")
app.config["SECRET_KEY"] = environ.get('SECRET_KEY')
db = SQLAlchemy(app)

# instantiate package for encryption
bcrypt = Bcrypt(app)

# add config for flask_login
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# setup database tables
from .models import Task, User

with app.app_context():
    db.create_all()

# register routes
from . import views

app.add_url_rule("/register", view_func=views.UserRegisterView.as_view("register"))
app.add_url_rule("/login", view_func=views.UserLoginView.as_view("login"))
app.add_url_rule("/logout", view_func=views.UserLogoutView.as_view("logout"))
app.add_url_rule("/task/<int:id>", view_func=views.TaskItemView.as_view("task-item", Task))
app.add_url_rule("/task/", view_func=views.TaskView.as_view("task", Task))

