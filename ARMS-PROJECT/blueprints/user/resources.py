from flask import Blueprint
from flask_restful import Resource, Api,reqparse, marshal, inputs
from .model import User
from blueprints import db, app,internal_required
from sqlalchemy import desc

bp_user = Blueprint('user',__name__)
api = Api(bp_user)

# using flask restful

class UserResource(Resource):

    # @internal_required 
    def get(self,id=None): 
        qry = User.query.get(id)
        if qry is not None:

            return marshal(qry, User.response_fields),200
        return {'status' : 'NOT_FOUND'}, 404

    # @internal_required 
    def post(self): 
        parser = reqparse.RequestParser()
        parser.add_argument('client_id', location='json', required=True)
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('age', location='json',type=int, required=True)
        parser.add_argument('sex', location='json', required=True,choices=('male', 'female'))
        
        args = parser.parse_args()
        user = User(args['client_id'],args['name'],args['age'],args['sex'])
    
        db.session.add(user)
        db.session.commit()

        app.logger.debug('DEBUG : %s', user )
        return marshal(user, User.response_fields), 200 , {'Content-Type':'application/json'}

    # @internal_required  
    def put(self,id): 
        parser = reqparse.RequestParser()
        parser.add_argument('client_id', location='json', required=True)
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('age', location='json',type=int, required=True)
        parser.add_argument('sex', location='json', required=True,choices=('male', 'female'))
        args = parser.parse_args()

        qry = User.query.get(id)
        if qry is None :
            return {'status' : 'NOT_FOUND'}, 404
        qry.client_id = args['client_id']
        qry.name = args['name']
        qry.age = args['age']
        qry.sex = args['sex']
        db.session.commit()

        return marshal(qry, User.response_fields),200

    # @internal_required 
    def delete(self,id):
        qry = User.query.get(id)
        if qry is None:
            return {'status' : 'NOT_FOUND'}, 404
        db.session.delete(qry)
        db.session.commit()
       

    def patch(self): 
        return 'Not yet implement',501

class UserList(Resource):
    def __init__(self):
        pass
    # @internal_required 
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('sex', location='args', help='invalid status', choices=('male', 'female'))
        parser.add_argument('orderby', location='args', help='invalid order by value',choices=('age','sex'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

        args = parser.parse_args()
        offset = (args['p'] * args['rp']) - args['rp']
        qry = User.query
        if args['sex'] is not None:
            qry = qry.filter_by(sex=args['sex'])

        if args['orderby'] is not None:
            if args['orderby'] == 'age':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(User.age))
                else:
                    qry =  qry.order_by(User.age)
            elif args['orderby'] == 'sex':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(User.sex))
                else:
                    qry =  qry.order_by(User.sex)
        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, User.response_fields))
        return rows, 200
api.add_resource(UserList,'','/list')
api.add_resource(UserResource, '', '/<id>')