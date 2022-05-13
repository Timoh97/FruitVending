from flask import Blueprint
from . import auth

app=Blueprint('auth',__name__)
from . import views,forms