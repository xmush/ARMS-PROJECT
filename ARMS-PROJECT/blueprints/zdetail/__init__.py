import requests
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal
from blueprints import app
# from flask_jwt_extended import jwt_required

bp_zodiakDetail = Blueprint('zodiakDetail', __name__)
api = Api(bp_zodiakDetail)


class ZodiakDetailResource(Resource):

    # get zodiak detail host
    host = app.config['ZDETAIL_HOST']

    # get function for get detail horscope fro zodiak parameter
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('zodiak', location='args', required=True)
        args = parser.parse_args()

        url = ('%s?sign=%s&day=today' % (self.host,args['zodiak']))
        payload = "{}"
        headers = {
        'Content-Type': 'application/json'
        }
        print(url)
        response = requests.request("POST", url, headers=headers, data = payload)

        # response = requests.get(self.host, params={'sign' : args['zodiak'], 'day' : 'today'})
        return response.json(), 200, {'Content-Type': 'application/json'}



#         rq = requests.get(self.wio_host + '/ip', params={'ip': args['ip']})
#         geo = rq.json()
#         lat = geo['latitude']
#         lon = geo['longitude']
#         rq = requests.get(self.wio_host + '/current', params={'lat': lat, 'lon': lon})
#         current = rq.json()

#         return {
#             'city': geo['city'],
#             'organization': geo['organization'],
#             'timezone': geo['timezone'],
#             'current_weather': {
#                 'date': current['data'][0]['datetime'],
#                 'temp': current['data'][0]['temp']
#             }
#         }

api.add_resource(ZodiakDetailResource, '')