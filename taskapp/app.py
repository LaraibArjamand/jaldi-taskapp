from flask import Flask

app = Flask(__name__)

from blueprints import auth_bp

app.register_blueprint(auth_bp, url_prefix='/')
