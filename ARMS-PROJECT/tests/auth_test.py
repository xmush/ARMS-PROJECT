import json, random, string
from . import app, client, cache, create_noninternal_token, create_internal_token, logging, init_database

class TestAuth :
    
    def test_auth(self, client, init_database) :
        data = {
            'name' : 'sholeh',
            'password' : 'sholeh'
        }

        res = client.get('/auth', query_string=data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_auth_fail(self, client, init_database) :
        data = {
            'name' : 'sholeh',
            'password' : 'sholehdd'
        }

        res = client.get('/auth', query_string=data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 401    

    def test_get_auth_claim(self, client, init_database) :
        header = {
            'Authorization' : 'Bearer ' + create_internal_token()
        }

        res = client.post('/auth', headers= header, content_type='application/json')

        res_json = json.loads(res.data) 

        assert res.status_code == 200

    def test_refresh_token_internal(self, client, init_database) :
        header = {
            'Authorization' : 'Bearer ' + create_internal_token()
        }

        res = client.post('/auth/refresh', headers= header, content_type='application/json')
        
        res_json = json.loads(res.data) 

        assert res.status_code == 200
    
