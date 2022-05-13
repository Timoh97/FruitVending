
#2nd step set the initialization of the app
#4th step register main blueprint class
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


bootstrap=Bootstrap


def create_app(config_name):
    app=Flask(__name__)
    from .main import main as main_blueprint
    
    # Initializing flask extensions
    bootstrap.init_app('self',app)

    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    
    return app
