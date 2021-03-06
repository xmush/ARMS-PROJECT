from flask import Blueprint
from flask_restful import Resource, Api,reqparse, marshal, inputs
from .model import User
from blueprints import db, app, internal_required
from sqlalchemy import desc
import uuid, hashlib
from datetime import datetime
from dateutil.parser import parse

bp_user = Blueprint('user',__name__)
api = Api(bp_user)

# using flask restful

class UserResource(Resource):

    @internal_required 
    def get(self,id=None): 
        qry = User.query.get(id)
        if qry is not None:
            return marshal(qry, User.response_fields),200
        return {'status' : 'NOT_FOUND'}, 404
        
    def post(self): 
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('bod', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        # parser.add_argument('status', type=bool, location='json', required=True)
        args = parser.parse_args()

        salt = uuid.uuid4().hex
        hash_pass = hashlib.sha512(('%s%s' % (args['password'], salt)).encode('utf-8')).hexdigest()

        bod = datetime.strptime(args['bod'], '%d/%m/%Y')
        status = False
        user = User(args['name'],bod, hash_pass, salt, status)
        db.session.add(user)
        db.session.commit()


        app.logger.debug('DEBUG : %s', user )
        return marshal(user, User.response_fields), 200 , {'Content-Type':'application/json'}
    
    @internal_required
    def put(self,id): 
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('bod', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('status', type=bool, location='json', required=False)
        args = parser.parse_args()

        qry = User.query.get(id)

        if qry is None :
            return {'status' : 'NOT_FOUND'}, 404
        
        salt = qry.salt
        hash_pass = hashlib.sha512(('%s%s' % (args['password'], salt)).encode('utf-8')).hexdigest()

        bod = datetime.strptime(args['bod'], '%d/%m/%Y')

        qry.name = args['name']
        qry.bod = bod
        qry.password = hash_pass
        qry.status = args['status']

        db.session.commit()

        return marshal(qry, User.response_fields),200

    @internal_required 
    def delete(self,id):
        qry = User.query.get(id)
        if qry is None:
            return {'status' : 'NOT_FOUND'}, 404
        db.session.delete(qry)
        db.session.commit()
       
    # @internal_required 
    # def patch(self): 
    #     return 'Not yet implement',501

class UserList(Resource):
    def __init__(self):
        pass
    @internal_required 
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('name', location='args', help='invalid status')
        parser.add_argument('orderby', location='args', help='invalid order by value', choices=('id', 'name', 'status'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

        args = parser.parse_args()
        if args['p'] == 1:
            offset = 0
        else:
            offset = (args['p'] * args['rp']) - args['rp']
        qry = User.query
        if args['name'] is not None:
            qry = qry.filter_by(name=args['name'])

        if args['orderby'] is not None:
            if args['orderby'] == 'name':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(User.name))
                else:
                    qry =  qry.order_by(User.name)
            elif args['orderby'] == 'status':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(User.status))
                else:
                    qry = qry.order_by(User.status)
            elif args['orderby'] == 'id':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(User.id))
                else:
                    qry = qry.order_by(User.id)
        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, User.response_fields))
        
        return rows, 200
api.add_resource(UserList,'','/list')
api.add_resource(UserResource, '', '/<id>')