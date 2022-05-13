from flask import Flask
from . import main
from . import auth
from . import app




def create_app():
 app=Flask(__name__)
 
 from main import main as main_blueprint
 app.register_blueprint(main_blueprint)
 from auth import auth as auth_blueprint
 app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
 
 
 return app