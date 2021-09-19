from flask import Flask 
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app(config_name):
    app= Flask(__name__)


from .main import views
