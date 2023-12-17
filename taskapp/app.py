from os import environ

from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URI")
app.config["SECRET_KEY"] = environ.get('SECRET_KEY')
db = SQLAlchemy(app)

# configure rest api
api = Api(app)

# add config for flask_login
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# setup database tables
from .models import User

with app.app_context():
    db.create_all()

# register routes
from .blueprints import (LoginResource, LogoutResource, ProtectedResource,
                         RegisterResource, auth_bp)

api.add_resource(RegisterResource, "/register")
api.add_resource(LoginResource, "/login")
api.add_resource(LogoutResource, "/logout")
api.add_resource(ProtectedResource, "/")
app.register_blueprint(auth_bp, url_prefix='/')
