from flask import render_template
from . import main

@main.app_errorhandler
def error(error):
    
    return render_template('error.html'),404
