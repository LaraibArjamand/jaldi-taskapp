from flask import request
from flask.views import MethodView
from flask_login import current_user, login_user, logout_user

from ..app import bcrypt, db, login_manager
from ..models import User
from .utils import response_message, validate_user_details, validate_user_input


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class UserRegisterView(MethodView):

    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if response := validate_user_input(username, password):
            return response

        if User.query.filter_by(username=username).first():
            return response_message("ERROR: Username already exists"), 400

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return response_message("INFO: User registered successfully"), 201


class UserLoginView(MethodView):

    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if response := validate_user_input(username, password):
            return response

        user = User.query.filter_by(username=username).first()

        if response := validate_user_details(user, password):
            return response
        
        login_user(user)
        return response_message("INFO: Logged in successfully"), 200

    def delete(self):
        username = request.json.get("username")
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        return response_message("SUCCESS: USER REMOVED")


class UserLogoutView(MethodView):

    def post(self):
        if current_user.is_authenticated:
            logout_user()
            return response_message("INFO: Logged out successfully"), 200
        return response_message("ERROR: You need to login first"), 401
