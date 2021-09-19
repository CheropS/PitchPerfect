from flask import Flask, app 
from flask_bootstrap import Bootstrap
# from config import config_options


bootstrap = Bootstrap()


def create_app(config_name):
    app= Flask(__name__)
    

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app



