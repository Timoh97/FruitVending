import os

#s1st step set configurations

class Config:

   
    SECRET_KEY = 'tim'
   

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tim:12345@localhost/fruitsvending'
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

