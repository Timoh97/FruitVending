


from . import db

def User():
    __table__='users'
    
    id=db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(255))
    firstname=db.Column(db.String(255))
    secondname=db.Column(db.String(255))
    url_to_store=db.Column(db.String(255))
def Fruit():
    __table__='fruits'
    name = db.Column(db.String(255))
    price= db.Column(db.Integer)
    seller= db.Column(db.String(255))
    availability= db.Column(db.String(255))
    perishability= db.Column(db.String)
    
def Transport ():
    __table__='transport'
    
    cost=db.Column(db.Integer)
    duration=db.Column(db.Integer)
    offloaders=db.Column(db.String)
    loaders=db.Column(db.String)