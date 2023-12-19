import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")


class TestConfig(object):
    HOST = "http://127.0.0.1:5001"

    REGISTER_ENDPOINT = f"{HOST}/users/register"
    LOGIN_ENDPOINT = f"{HOST}/users/login"
    LOGOUT_ENDPOINT = f"{HOST}/users/logout"
    TASK_ENDPOINT = f"{HOST}/tasks"

    TEST_USER = "Bill"
    TEST_PASSWORD = "12345"
