
#2nd step set the initialization of the app
#4th step register main blueprint class
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy #initialize db
from flask_login import LoginManager #loggin

bootstrap=Bootstrap

db = SQLAlchemy() #initialize db
login_manager = LoginManager() # allows login
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app=Flask(__name__)
    from .main import main as main_blueprint
    
    # Initializing flask extensions
    bootstrap.init_app('self',app)
    db.init_app(app)

    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    
    return app
