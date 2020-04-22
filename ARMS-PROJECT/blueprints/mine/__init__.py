import requests, json
from flask import Blueprint, jsonify, make_response
from flask_restful import Api, reqparse, Resource, marshal
from blueprints import app
# from flask_jwt_extended import jwt_required

bp_mine = Blueprint('mine', __name__)
api = Api(bp_mine)


class MineResource(Resource):

    # get zodiak detail host
    # host = app.config['ZODIAK_HOST']
    # service = app.config['ZODIAK_SERVICE']
    host = 'http://'+app.config['APP_HOST']+':'+app.config['APP_PORT']

    # get function for get detail horscope from zodiak parameter
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name1', location='args', required=True)
        parser.add_argument('bod1', location='args', required=True)
        parser.add_argument('name2', location='args', required=True)
        parser.add_argument('bod2', location='args', required=True)
        args = parser.parse_args()

        zodiak1 = requests.get(self.host+'/zodiak?name='+args['name1']+'&bod='+args['bod1']).json()
        zodiak2 = requests.get(self.host+'/zodiak?name='+args['name2']+'&bod='+args['bod2']).json()

        if zodiak1["Zodiak"] == "sagitarius" or zodiak1["Zodiak"] == "Sagitarius" :
            zodiak1["Zodiak"] = "Sagittarius"
        if zodiak2["Zodiak"] == "sagitarius" or zodiak2["Zodiak"] == "Sagitarius" :
            zodiak2["Zodiak"] = "Sagittarius"


        # print(zodiak1.json())

        respon1 = requests.get(self.host+'/detail?zodiak='+zodiak1["Zodiak"]).json()
        respon2 = requests.get(self.host+'/detail?zodiak='+zodiak2["Zodiak"]).json()

        compability = respon1['compatibility']

        new_compability = []

        for comp in compability :
            zdk = comp.replace(' ', '')
            if zdk == 'aurus' :
                zdk = 'Taurus'
            new_compability.append(zdk)

        compability_with = zodiak2["Zodiak"] in new_compability



        # print(new_compability)

        result = {
            "your_name" : args["name1"],
            "your_zodiak" : zodiak1["Zodiak"],
            "partner_name" : args["name2"],
            "partner_zodiak" : zodiak2["Zodiak"],
            'compatibility_status' : compability_with,
            'partner_recommend_zodiac' : respon1["compatibility"],
            "partner_good_traits" : respon2["good_traits"],
            "partner_bad_traits" : respon2["bad_traits"],
            "your_element" : respon1["element"],
            "partner_element" : respon2["element"]
        }
        
        return result, 200, {'Content-Type': 'application/json'}


api.add_resource(MineResource, '')