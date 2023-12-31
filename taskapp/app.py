from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from taskapp.config import Config

app = Flask(__name__)
config = Config()

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = config.SECRET_KEY

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"


from taskapp.models import Task, User

with app.app_context():
    db.create_all()

from taskapp.views import task_bp, user_bp

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(task_bp, url_prefix='/tasks')
