from flask import Blueprint
from flask_restful import Resource, Api,reqparse, marshal, inputs
from .model import Data
from blueprints import db, app, internal_required
from sqlalchemy import desc
import uuid, hashlib

bp_data = Blueprint('data',__name__)
api = Api(bp_data)

# using flask restful

class DataResource(Resource):
    def __init__(self) :
        pass
    # @internal_required 
    # def get(self,id=None): 
    #     qry = Data.query.get(id)
    #     if qry is not None:
    #         return marshal(qry, Data.response_fields),200
    #     return {'status' : 'NOT_FOUND'}, 404
    # @internal_required 
    # def post(self): 
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('user_id', location='json', required=True)
    #     parser.add_argument('name_couple', location='json', required=True)
    #     parser.add_argument('bod_couple', location='json', required=True)
    #     parser.add_argument('respon', location='json', required=True)
      
    #     args = parser.parse_args()

    #     salt = uuid.uuid4().hex
    #     hash_pass = hashlib.sha512(('%s%s' % (args['password'], salt)).encode('utf-8')).hexdigest()

    #     data = Data(args['name'],args['bod'], hash_pass, salt, args['status'])
    #     db.session.add(data)
    #     db.session.commit()

    #     app.logger.debug('DEBUG : %s', data )
    #     return marshal(data, Data.response_fields), 200 , {'Content-Type':'application/json'}
    
    # @internal_required 
    # def put(self,id): 
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('name', location='json', required=True)
    #     parser.add_argument('bod', location='json', required=True)
    #     parser.add_argument('password', location='json', required=True)
    #     parser.add_argument('status', type=bool, location='json', required=True)
    #     args = parser.parse_args()

    #     qry = Data.query.get(id)
    #     if qry is None :
    #         return {'status' : 'NOT_FOUND'}, 404
    #     qry.name = args['name']
    #     qry.bod = args['bod']
    #     qry.password = args['password']
    #     qry.status = args['status']

    #     db.session.commit()

    #     return marshal(qry, Data.response_fields),200

    # @internal_required 
    # def delete(self,id):
    #     qry = Data.query.get(id)
    #     if qry is None:
    #         return {'status' : 'NOT_FOUND'}, 404
    #     db.session.delete(qry)
    #     db.session.commit()
       
    # @internal_required 
    # def patch(self): 
    #     return 'Not yet implement',501

class DataList(Resource):
    def __init__(self):
        pass
    # @internal_required 
    # def get(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('p', type=int, location='args', default=1)
    #     parser.add_argument('rp', type=int, location='args', default=25)
    #     parser.add_argument('name', location='args', help='invalid status')
    #     parser.add_argument('orderby', location='args', help='invalid order by value')
    #     parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

    #     args = parser.parse_args()
    #     if args['p'] == 1:
    #         offset = 0
    #     else:
    #         offset = (args['p'] * args['rp']) - args['rp']
    #     qry = Data.query
    #     if args['name'] is not None:
    #         qry = qry.filter_by(name=args['name'])

    #     if args['orderby'] is not None:
    #         if args['orderby'] == 'name':
    #             if args['sort'] == 'desc':
    #                 qry = qry.order_by(desc(Data.name))
    #             else:
    #                 qry =  qry.order_by(Data.name)
    #         elif args['orderby'] == 'status':
    #             if args['sort'] == 'desc':
    #                 qry = qry.order_by(desc(Data.status))
    #             else:
    #                 qry = qry.order_by(Data.status)
    #         elif args['orderby'] == 'id':
    #             if args['sort'] == 'desc':
    #                 qry = qry.order_by(desc(Data.id))
    #             else:
    #                 qry = qry.order_by(Data.id)
    #     rows = []
    #     for row in qry.limit(args['rp']).offset(offset).all():
    #         rows.append(marshal(row, Data.response_fields))
        
    #     return rows, 200
api.add_resource(DataList,'','/list')
api.add_resource(DataResource, '', '/<id>')