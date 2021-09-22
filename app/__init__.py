from flask import Flask, app 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# from config import config_options


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app= Flask(__name__)
    

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    bootstrap.init_app(app)
    db.init_app(app)




    return app



