import requests, json
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
    

        url = ('%s%s' % (self.host,args['zodiak']))
        
        response = requests.get(url)

        result = {
            "zodiac" : args["zodiak"],
            "compatibility" : response.json()[0]["compatibility"],
            "good_traits" : response.json()[0]["good_traits"],
            "bad_traits" : response.json()[0]["bad_traits"],
            "element" : response.json()[0]["element"]
        }

        return result, 200, {'Content-Type': 'application/json'}


api.add_resource(ZodiakDetailResource, '')