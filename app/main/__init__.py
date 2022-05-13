from flask import Blueprint
from . import main

app=Blueprint('main',__name__)
from . import error, views, forms