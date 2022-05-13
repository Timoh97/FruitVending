from flask import Flask
from . import main
from . import auth
from . import app
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap=Bootstrap()


def create_app(config_name):
 app=Flask(__name__)
 
 bootstrap.init_app('self',app)
 
 from main import main as main_blueprint
 app.register_blueprint(main_blueprint)
 from auth import auth as auth_blueprint
 app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
 
 
 return app