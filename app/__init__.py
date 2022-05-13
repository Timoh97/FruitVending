from flask import Flask
from . import main as main_blueprint
from config import config_options
from . import auth as auth_blueprint

from flask_bootstrap import Bootstrap

bootstrap=Bootstrap()


def create_app(config_name):
 app=Flask(__name__)
 
 bootstrap.init_app(app)
 
 
 app.register_blueprint(main_blueprint)
 
 app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
 app.config.from_object(config_options[config_name])
 
 
 return app