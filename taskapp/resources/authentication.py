from flask import request
from flask_login import current_user, login_required, login_user, logout_user
from flask_restful import Resource

from ..app import bcrypt, db, login_manager
from ..models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if User.query.filter_by(username=username).first():
            return {'message': 'Username already exists'}, 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return {'message': 'Logged in successfully'}, 200

        return {'message': 'Invalid username or password'}, 401

class LogoutResource(Resource):
    @login_required
    def post(self):
        logout_user()
        return {'message': 'Logged out successfully'}, 200

class ProtectedResource(Resource):
    @login_required
    def get(self):
        return {'message': f'Hello, {current_user.username}! You are accessing a protected resource.'}, 200
 
