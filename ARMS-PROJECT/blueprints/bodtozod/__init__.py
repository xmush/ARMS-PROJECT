from blueprints import db
from flask_restful import fields
from sqlalchemy import Integer, ForeignKey, String, Column


class Bod(db.Model):
    __tablename__ = "bod"
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

    def __init__(self,name_male, bod_male, name_female, bod_female):
        self.name_male = name_male
        self.bod_male = bod_male
        self.name_female = name_female
        self.bod_female = bod_female
       

    def __repr__(self):
        return '<Bod %r>' % self.id