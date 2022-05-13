from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/cart')
def cart():
    return render_template("cart.html")

@main.route('/about')
def about():
   
    return render_template("about.html")

@main.route('/checkout')
def checkout():

    return render_template("checkout.html")

@main.route('/contact')
def contact():
    return render_template("contact.html")

@main.route('/indexx')
def indexx():
    return render_template("index_2.html")

@main.route('/news')
def news():

    return render_template("news.html")

@main.route('/shop')
def shop():
    return render_template("shop.html")

@main.route('/singles')
def single():
    return render_template("single-news.html")

@main.route('/product')
def product():
    return render_template("single-product.html") 