from flask import render_template
from . import main

@main.route('/')
def index():
    title=''
    subject='applicationdevelopment'
    return render_template("index.html",name=title,subject=subject)