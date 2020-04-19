from blueprints import db
from flask_restful import fields
from sqlalchemy import Integer, ForeignKey, String, Column
# from blueprints.client.model import Client

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # client_id = db.Column(db.Integer, ForeignKey(Client.client_id))
    name = db.Column(db.String(30), unique = True, nullable = False)
    age = db.Column(db.Integer, nullable = False, default = 20)
    sex = db.Column(db.String(10), nullable = False)

    response_fields = {
        'id' : fields.Integer,
        'client_id' : fields.Integer,
        'name' : fields.String,
        'age' : fields.Integer,
        'sex' : fields.String
    }    

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self):
        return '<User %r>' % self.id