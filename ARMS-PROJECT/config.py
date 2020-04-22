import configparser
from datetime import timedelta

cfg = configparser.ConfigParser()
cfg.read('config.cfg')


class Config():
    SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s:%s/%s' %(
        cfg['database']['default_connection'],
        cfg['mysql']['driver'],
        cfg['mysql']['user'],
        cfg['mysql']['password'],
        cfg['mysql']['host'],
        cfg['mysql']['port'],
        cfg['mysql']['db']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = cfg['jwt']['key']
    JWT_ACCES_TOKEN_EXPIRES = timedelta(days=int(cfg['jwt']['time_live']))
    
    ZODIAK_HOST = cfg['zodiak']['host']
    ZODIAK_SERVICE = cfg['zodiak']['service']
    ZDETAIL_HOST = cfg['zdetail']['host']

    DISCORD_TOKEN = cfg['discord']['token']
    DISCORD_CONFIG = cfg['discord']['guild']

class DevelopmentConfig(Config):
    APP_DEBUG = True
    DEBUG = True
    MAX_BYTES = 10000
    APP_PORT = cfg['app']['port']
    APP_HOST = cfg['app']['host']
   
class ProductionConfig(Config):
    APP_DEBUG = False
    DEBUG = False
    MAX_BYTES = 100000
    APP_PORT = cfg['app']['port']
    APP_HOST = cfg['app']['host']

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s:%s/%s_testing' %(
        cfg['database']['default_connection'],
        cfg['mysql']['driver'],
        cfg['mysql']['user'],
        cfg['mysql']['password'],
        cfg['mysql']['host'],
        cfg['mysql']['port'],
        cfg['mysql']['db']
    )    
    APP_DEBUG = True
    DEBUG = True
    MAX_BYTES = 100000
    APP_PORT = cfg['app']['port']
    APP_HOST = cfg['app']['host']