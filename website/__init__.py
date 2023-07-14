from flask import Flask
from os import path

def create_app():
    app = Flask(__name__)

    from .index import homePage
    app.register_blueprint(homePage, url_prefix='/')
    return app