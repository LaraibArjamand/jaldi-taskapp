from flask import Flask

app = Flask(__name__)

# connect app to database
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:root@db:3306/taskapp")
connection = engine.connect()

# register routes
from blueprints import auth_bp

app.register_blueprint(auth_bp, url_prefix='/')
