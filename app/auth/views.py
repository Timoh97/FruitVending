from flask import render_template,redirect,url_for
from . import auth
from .. models import *
from . forms import RegistrationForm



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
    
        # mail_message("Welcome to Timverse World","email/welcome_user",user.email,user=user) #call the mail inside register function
        return redirect(url_for('auth.login'))
    
    return render_template("auth/register.html",registration_form=form)