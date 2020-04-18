from flask import Blueprint
from flask_restful import Resource, Api,reqparse, marshal, inputs
from .model import Client
from blueprints import db, app,internal_required
from sqlalchemy import desc
import uuid, hashlib

bp_client = Blueprint('client',__name__)
api = Api(bp_client)

# using flask restful

class ClientResource(Resource):

    # @internal_required 
    def get(self,id=None): 
        qry = Client.query.get(id)
        if qry is not None:
            return marshal(qry, Client.response_fields),200
        return {'status' : 'NOT_FOUND'}, 404
    # @internal_required 
    def post(self): 
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        parser.add_argument('internal', type=bool, location='json', required=True)
        args = parser.parse_args()

        salt = uuid.uuid4().hex
        hash_pass = hashlib.sha512(('%s%s' % (args['client_secret'], salt)).encode('utf-8')).hexdigest()

        client = Client(args['client_key'], hash_pass, salt, args['internal'])
        db.session.add(client)
        db.session.commit()

        app.logger.debug('DEBUG : %s', client )
        return marshal(client, Client.response_fields), 200 , {'Content-Type':'application/json'}
    
    # @internal_required 
    def put(self,id): 
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        parser.add_argument('internal', location='json', required=True)
        args = parser.parse_args()

        qry = Client.query.get(id)
        if qry is None :
            return {'status' : 'NOT_FOUND'}, 404
        qry.client_key = args['client_key']
        qry.client_secret = args['client_secret']
        qry.internal = args['internal']

        db.session.commit()

        return marshal(qry, Client.response_fields),200

    # @internal_required 
    def delete(self,id):
        qry = Client.query.get(id)
        if qry is None:
            return {'status' : 'NOT_FOUND'}, 404
        db.session.delete(qry)
        db.session.commit()
       
    # @internal_required 
    def patch(self): 
        return 'Not yet implement',501

class ClientList(Resource):
    def __init__(self):
        pass
    # @internal_required 
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('client_key', location='args', help='invalid status')
        parser.add_argument('orderby', location='args', help='invalid order by value')
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

        args = parser.parse_args()
        offset = (args['p'] * args['rp']) - args['rp']
        qry = Client.query
        if args['client_key'] is not None:
            qry = qry.filter_by(client_key=args['client_key'])

        if args['orderby'] is not None:
            if args['orderby'] == 'client_key':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Client.client_key))
                else:
                    qry =  qry.order_by(Client.client_key)
            elif args['orderby'] == 'client_secret':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Client.client_secret))
                else:
                    qry =  qry.order_by(Client.client_secret)
        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Client.response_fields))
        return rows, 200
api.add_resource(ClientList,'','/list')
api.add_resource(ClientResource, '', '/<id>')