import json,logging,config,os
from functools import wraps
from flask_restful import fields, Resource, Api
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from logging.handlers import RotatingFileHandler
from flask_jwt_extended import JWTManager, verify_jwt_in_request,get_jwt_claims

app = Flask(__name__)

jwt = JWTManager(app)


def internal_required(fn):
    @wraps(fn)
    def wrapper (*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if not claims['internal']:
            return {'status' : 'FORBIDDEN', 'message' : 'Internal Only!'}, 403
        else:
            return fn(*args, **kwargs) 
    return wrapper

if os.environ.get('FLASK_ENV', 'Production') == "Production":
    app.config.from_object(config.ProductionConfig)
else:
    app.config.from_object(config.DevelopmentConfig)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.after_request
def after_request(response):
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()
    if response.status_code == 200:
        app.logger.warning("REQUEST_LOG\t%s",
        json.dumps({'method' : request.method, 
        'code' : response.status, 
        'uri' : request.full_path, 
        'request' : requestData,
        'response': json.loads(response.data.decode('utf-8'))
        }))
    else: 
        app.logger.error("")
    return response
# from blueprints.user.resources import bp_user 
# app.register_blueprint(bp_user, url_prefix = '/user')

# from blueprints.book.resources import bp_book 
# app.register_blueprint(bp_book, url_prefix = '/book')



db.create_all()
