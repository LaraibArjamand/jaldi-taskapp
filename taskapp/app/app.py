from blueprints import auth_bp
from flask import Flask

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix='/')

