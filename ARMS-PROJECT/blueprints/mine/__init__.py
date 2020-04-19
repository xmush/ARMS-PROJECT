from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from flask_jwt_extended import create_access_token, get_jwt_identity, get_jwt_claims,jwt_required
import hashlib
from blueprints import db #, internal_required

bp_auth = Blueprint('auth',__name__)
api = Api(bp_auth)

class CreateTokenResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='args', required=True)
        parser.add_argument('client_secret', location='args', required=True)
        args = parser.parse_args()

        qry_client = Client.query.filter_by(client_key=args['client_key']).first()
        client_salt = qry_client.salt
        hash_pass = hashlib.sha512(('%s%s' % (args['client_secret'], client_salt)).encode('utf-8')).hexdigest()

        if hash_pass == qry_client.client_secret:
            qry_client = marshal(qry_client, Client.jwt_claim_fields)
            token = create_access_token(identity=args['client_key'], user_claims=qry_client)
            return {'token' : token} , 200
        else:
            return {'status' : 'UNAUTHORIZED', 'message': 'invalid key or secret'}, 401

api.add_resource(CreateTokenResource,'')