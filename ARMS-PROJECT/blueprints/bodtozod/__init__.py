import requests
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal
from blueprints import app
# from flask_jwt_extended import jwt_required

bp_zodiak = Blueprint('zodiak', __name__)
api = Api(bp_zodiak)


class ZodiakResource(Resource):

    # get zodiak detail host
    host = app.config['ZODIAK_HOST']
    service = app.config['ZODIAK_SERVICE']

    # get function for get detail horscope from zodiak parameter
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='args', required=True)
        parser.add_argument('bod', location='args', required=True)
        args = parser.parse_args()

        url = ('%sservice=%s&nama=%s&tanggal=%s' % (self.host, self.service, args['name'], args['bod']))
        response = requests.get(url)

        return response.json(), 200, {'Content-Type': 'application/json'}
        
        # url = ('%s?sign=%s&day=today' % (self.host,args['zodiak']))
        # payload = "{}"
        # headers = {
        # 'Content-Type': 'application/json'
        # }
        # print(url)
        # response = requests.request("POST", url, headers=headers, data = payload)

        # return response.json(), 200, {'Content-Type': 'application/json'}


api.add_resource(ZodiakResource, '')