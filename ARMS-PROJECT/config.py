import configparser
from datetime import timedelta

cfg = configparser.ConfigParser()
cfg.read('config.cfg')


class Config():
    
    JWT_SECRET_KEY = cfg['secret_key']['key']
    JWT_ACCES_TOKEN_EXPIRES = timedelta(days=1)
    # WIO_HOST = cfg['host']['wio_host']
class DevelopmentConfig(Config):
    APP_DEBUG = True
    DEBUG = True
    MAX_BYTES = 10000
    APP_PORT = cfg['app']['port']
    APP_HOST = cfg['app']['host']
   
class ProductionConfig(Config):
    APP_DEBUG = True
    DEBUG = True
    MAX_BYTES = 100000
    APP_PORT = cfg['app']['port']
    APP_HOST = cfg['app']['host']