from flask import render_template
from . import main

@main.route('/')
def index():
    title='OnlineFruits'
    subject='application development'
    return render_template("index.html")