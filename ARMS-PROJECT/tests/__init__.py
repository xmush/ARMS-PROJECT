import pytest, logging
from flask import Flask, request, json
from blueprints import app, cache
from blueprints.user.model import User
from blueprints import db
import hashlib, uuid
from datetime import datetime
from dateutil.parser import parse

def call_client(requests) :
    client = app.test_client()
    # wheather = app.test_weather()
    return client

    
@pytest.fixture
def init_database() :

    db.drop_all()

    db.create_all()

    strdata = 'sholeh'
    strdata2 = 'aji'

    salt = uuid.uuid4().hex
    hash_pass = hashlib.sha512(('%s%s' % (strdata, salt)).encode('utf-8')).hexdigest()
    bod = datetime.strptime('01/11/1995', '%d/%m/%Y')
    client1 = User(strdata, bod, hash_pass, salt, status=1)

    # salt = uuid.uuid4().hex
    hash_pass2 = hashlib.sha512(('%s%s' % (strdata2, salt)).encode('utf-8')).hexdigest()
    bod = datetime.strptime('12/02/1992', '%d/%m/%Y')
    client2 = User(strdata2, bod, hash_pass2, salt, status=0)

    db.session.add(client1)
    db.session.add(client2)

    db.session.commit()

@pytest.fixture
def client(request) :
    return call_client(request)

def create_internal_token() :
    token = cache.get('test-token')
    if token is None :
        data = {
            'name' : 'sholeh',
            'password' : 'sholeh'
        }

        req = call_client(request) 
        res = req.get('/auth', query_string=data)

        res_json = json.loads(res.data)

        logging.warning('RESULT : %s', res_json)

        assert res.status_code == 200

        cache.set('test-token', res_json['token'], timeout=60)

        return res_json['token']
    else :
        return token

def create_noninternal_token() :
    token = cache.get('test-token-internal')
    if token is None :
        data = {
            'name' : 'aji',
            'password' : 'aji'
        }

        req = call_client(request) 
        res = req.get('/auth', query_string=data)

        res_json = json.loads(res.data)

        logging.warning('RESULT : %s', res_json)

        assert res.status_code == 200

        cache.set('test-token-internal', res_json['token'], timeout=60)

        return res_json['token']
    else :
        return token