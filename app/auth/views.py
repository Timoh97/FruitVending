from flask import render_template
from . import auth
from .. models import *
from . forms import RegisterForm



@auth.route('/register')
def register():
    return render_template