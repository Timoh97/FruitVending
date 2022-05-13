
import os


class Config():
    
 class DevConfig():
     
    pass
    
 class ProdConfig():
    Debug=True
 config_options={
    'development':DevConfig,
    'production':ProdConfig
}
    