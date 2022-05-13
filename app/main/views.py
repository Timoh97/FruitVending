from flask import render_template
from . import main

@main.route('/')
def index():
    title='Fruit Vending application'
    return render_template("index.html",title=title)