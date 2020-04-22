import json, random, string
from . import app, client, cache, create_noninternal_token, create_internal_token, logging, init_database

class TestUserCrud :

    def test_user_list_noninternal(self, client, init_database) :
        token = create_noninternal_token()
        data = {
            'p' : 1,
            'rp' : 10
        }
        res = client.get('user/list', headers = {'Authorization' : 'Bearer ' + token}, query_string = data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 403

    def test_user_list_internal_asc(self, client, init_database) :
        token = create_internal_token()
        data = {
            'p' : 1,
            'rp' : 10,
            'orderby' : 'name',
            'sort' : 'asc',
            'name' : 'sholeh'
        }
        res = client.get('user/list', headers = {'Authorization' : 'Bearer ' + token}, query_string = data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_user_list_internal(self, client, init_database) :
        token = create_internal_token()
        data = {
            'p' : 1,
            'rp' : 10,
            'orderby' : 'name',
            'sort' : 'desc',
            'name' : 'sholeh'
        }
        res = client.get('user/list', headers = {'Authorization' : 'Bearer ' + token}, query_string = data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_user_list_internal_status_desc(self, client, init_database) :
        token = create_internal_token()
        data = {
            'p' : 1,
            'rp' : 10,
            'orderby' : 'status',
            'sort' : 'desc',
            'name' : 'sholeh'
        }
        res = client.get('user/list', headers = {'Authorization' : 'Bearer ' + token}, query_string = data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_user_list_internal_status_asc(self, client, init_database) :
        token = create_internal_token()
        data = {
            'p' : 1,
            'rp' : 10,
            'orderby' : 'status',
            'sort' : 'asc',
            'name' : 'sholeh'
        }
        res = client.get('user/list', headers = {'Authorization' : 'Bearer ' + token}, query_string = data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_user_list_internal_id_desc(self, client, init_database) :
        token = create_internal_token()
        data = {
            'p' : 1,
            'rp' : 10,
            'orderby' : 'id',
            'sort' : 'desc',
            'name' : 'sholeh'
        }
        res = client.get('user/list', headers = {'Authorization' : 'Bearer ' + token}, query_string = data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_user_list_internal_id_asc(self, client, init_database) :
        token = create_internal_token()
        data = {
            'p' : 1,
            'rp' : 10,
            'orderby' : 'id',
            'sort' : 'asc',
            'name' : 'sholeh'
        }
        res = client.get('user/list', headers = {'Authorization' : 'Bearer ' + token}, query_string = data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_user_list_internal_offset(self, client, init_database) :
        token = create_internal_token()
        data = {
            'p' : 2,
            'rp' : 1,
            'orderby' : 'id',
            'sort' : 'asc',
            'name' : 'sholeh'
        }
        res = client.get('user/list', headers = {'Authorization' : 'Bearer ' + token}, query_string = data, content_type='application/json')

        res_json = json.loads(res.data)

        assert res.status_code == 200

    def test_user_get_by_id_noninternal(self, client, init_database) :
        token = create_noninternal_token()

        res = client.get('/user/1', headers= {'Authorization' : 'Bearer ' + token}, content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 403

    def test_user_get_by_id_internal(self, client, init_database) :
        token = create_internal_token()

        res = client.get('/user/1', headers= {'Authorization' : 'Bearer ' + token}, content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 200

    def test_user_get_by_id_404(self, client, init_database) :
        token = create_internal_token()

        res = client.get('/user/0', headers= {'Authorization' : 'Bearer ' + token}, content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 404


    def test_user_post(self, client, init_database) :
        
        # token = create_noninternal_token()
        
        data = {
            "name" : "yopi",
            "bod" : "10/11/1990",
            "password" : "yopi"
        }

        res = client.post('/user', data = json.dumps(data),content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 200

    def test_user_put_noninternal(self, client, init_database) :

        token = create_noninternal_token()

        data = {
            "name" : "yopi",
            "bod" : "10/11/1990",
            "password" : "yopi"
            # "status" : 'true'
        }

        res = client.put('/user/2', headers= {'Authorization' : 'Bearer ' + token}, data=json.dumps(data), content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 403

    def test_user_put_internal(self, client, init_database) :

        token = create_internal_token()

        data = {
            "name" : "yopi",
            "bod" : "10/11/1990",
            "password" : "yopi",
            "status" : 0
        }

        res = client.put('/user/2', headers= {'Authorization' : 'Bearer ' + token}, data=json.dumps(data), content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 200

    def test_user_put_internal_404(self, client, init_database) :

        token = create_internal_token()

        data = {
            "name" : "yopi",
            "bod" : "10/11/1990",
            "password" : "yopi",
            "status" : 0
        }

        res = client.put('/user/0', headers= {'Authorization' : 'Bearer ' + token}, data=json.dumps(data), content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 404


    def test_delete_user_noninternal(self, client, init_database) :
        token = create_noninternal_token()

        res = client.delete('/user/2', headers= {'Authorization' : 'Bearer ' + token}, content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 403

    def test_delete_user_internal(self, client, init_database) :
        token = create_internal_token()

        res = client.delete('/user/2', headers= {'Authorization' : 'Bearer ' + token}, content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 200

    def test_delete_user_internal_404(self, client, init_database) :
        token = create_internal_token()

        res = client.delete('/user/0', headers= {'Authorization' : 'Bearer ' + token}, content_type='application/json')

        res_json = json.loads(res.data)
        
        assert res.status_code == 404