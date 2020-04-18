from blueprints import db
from flask_restful import fields
from sqlalchemy import Integer, ForeignKey, String, Column
from blueprints.client.model import Client

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name_male = db.Column(db.String(30), unique = True, nullable = False)
    bod_male = db.Column(db.DateTime())
    name_female = db.Column(db.String(30), unique = True, nullable = False)
    bod_female = db.Column(db.DateTime())
     

    response_fields = {
        'id' : fields.Integer,
        'name_male' : fields.String,
        'bod_male' : fields.String,
        'name_female' : fields.String,
        'bod_female' : fields.String
    }    

    def __init__(self,name,age,sex):
        self.name_male = name
       

    def __repr__(self):
        return '<User %r>' % self.id