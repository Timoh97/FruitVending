from flask import render_template
from . import main

@main.route('/')
def index():
    title='OnlineFruits'
    subject='application development'
    return render_template("index.html")

@main.route('/cart')
def cart():
    title='OnlineFruits'
    subject='application development'
    return render_template("cart.html")
@main.route('/about')
def about():
    title='OnlineFruits'
    subject='application development'
    return render_template("about.html")
@main.route('/checkout')
def checkout():
    title='OnlineFruits'
    subject='application development'
    return render_template("checkout.html")
@main.route('/contact')
def contact():
    title='OnlineFruits'
    subject='application development'
    return render_template("contact.html")
@main.route('/indexx')
def indexx():
    title='OnlineFruits'
    subject='application development'
    return render_template("index_2.html")
@main.route('/news')
def news():
    title='OnlineFruits'
    subject='application development'
    return render_template("news.html")
@main.route('/shop')
def shop():
    title='OnlineFruits'
    subject='application development'
    return render_template("shop.html")

@main.route('/singles')
def single():
    title='OnlineFruits'
    subject='application development'
    return render_template("single-news.html")

@main.route('/product')
def product():
    title='OnlineFruits'
    subject='application development'
    return render_template("single-product.html")