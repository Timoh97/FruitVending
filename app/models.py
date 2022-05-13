

from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import UserMixin #authentication then pass UserMixin as parameter of model
from . import login_manager #helps in loggin
from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) #callback function that retrieves a user when a unique identifier is passed.
class User(UserMixin,db.Model):
    __tablename__='users'
    
    id=db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    firstname = db.Column(db.String(255))
    secondname = db.Column(db.String(255))
    url_to_store = db.Column(db.String(255))
        #creating user login and authentication
    pass_secure = db.Column(db.String(255))
    
    @property
    def password(self): #user authentication
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password): #user authentication
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password): #user authentication
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
             return f'User {self.username}'
    
class Fruit(db.Model):
    __tablename__='fruits'
    
    id=db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    price= db.Column(db.Integer)
    seller= db.Column(db.String(255))
    availability= db.Column(db.String(255))
    perishability= db.Column(db.String)
    
class Transport (db.Model):
    __tablename__='transport'
    
    
    id=db.Column(db.Integer,primary_key = True)
    cost= db.Column(db.Integer)
    duration= db.Column(db.Integer)
    offloaders= db.Column(db.String)
    loaders= db.Column(db.String)