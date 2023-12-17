from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@db/taskapp"
db = SQLAlchemy(app)

# register routes
from blueprints import auth_bp

app.register_blueprint(auth_bp, url_prefix='/')
