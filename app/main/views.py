from flask import render_template
from . import main
from flask_login import login_required

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/cart')
# @login_required
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
# @login_required
def news():

    return render_template("news.html")

@main.route('/shop')
# @login_required
def shop():
    return render_template("shop.html")

@main.route('/singles')
# @login_required
def single():
    return render_template("single-news.html")

@main.route('/product')
# @login_required
def product():
    return render_template("single-product.html") 