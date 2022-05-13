


from . import db

class User(db.Model):
    __tablename__='users'
    
    id=db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    secondname = db.Column(db.String(255))
    url_to_store = db.Column(db.String(255))
    
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