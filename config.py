 
import configparser
from datetime import timedelta

cfg = configparser.ConfigParser()
cfg.read('.env')

class Config() :
    API1_HOST = cfg['app']['host']
    API2_HOST = cfg['app']['port']
    JWT_SECRET_KEY = cfg['jwt']['key']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=int(cfg['jwt']['time_live']))

    WIO_HOST = cfg['wio']['host']
    WIO_KEY = cfg['wio']['key']


class DevelopmentConfig(Config) :
    APP_DEBUG =True
    DEBUG = True


class ProductionConfig(Config) :
    APP_DEBUG = False
    DEBUG = False