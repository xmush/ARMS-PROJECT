import json, random, string
from . import app, client, cache, create_noninternal_token, create_internal_token, logging, init_database
from unittest import mock
from unittest.mock import patch


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

class TestZodiak :
    

    def mocked_requests_get(*args, **kwargs):
        host = "https://script.google.com/"
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data
        
        if len(args) > 0:
            if args[0] == host+'macros/exec?' :
                return MockResponse(
                    {
                        'status': 'success',
                        'data': {
                            'nama': 'ican',
                            'lahir': 'Jumat Kliwon, 10 Agustus 1990',
                            'usia': '29 Tahun 8 Bulan 12 Hari',
                            'ultah': '3 Bulan 20 Hari',
                            'zodiak': 'Leo'
                        }
                    }, 200
                )

        else:
            return MockResponse(None, 404)

    # @mock.patch('requests.get', get_mock, post_mock, client_mock, client)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_client_list(self, get_mock, client) :
        # token = create_internal_token()
        data = {
            "name" : "namaanda",
            "bod" : "08-12-1994"
        }
        res = client.get('http://0.0.0.0:5000/zodiak', query_string=data)

        res_json = json.loads(res.data)
        
        assert res.status_code == 200


