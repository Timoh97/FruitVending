
import os


class Config():
    SECRET_KEY='TIM'
class DevConfig():
     
    pass
    
class ProdConfig():
    Debug=True
    
config_options={
    'development':DevConfig,
    'production':ProdConfig
}
    