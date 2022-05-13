import os

#s1st step set configurations

class Config:

   
    SECRET_KEY = 'tim'
   

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

