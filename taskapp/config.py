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

    REGISTER_ENDPOINT = f"{HOST}/auth/register"
    LOGIN_ENDPOINT = f"{HOST}/auth/login"
    LOGOUT_ENDPOINT = f"{HOST}/auth/logout"
    TASK_ENDPOINT = f"{HOST}/task"

    TEST_USER = "Bill"
    TEST_PASSWORD = "12345"
