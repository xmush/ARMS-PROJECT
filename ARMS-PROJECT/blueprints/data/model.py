from blueprints import db
from flask_restful import fields
from blueprints.user.model import User
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.sql import func
from datetime import datetime


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, ForeignKey(User.id))
    name_couple = db.Column(db.String(30), unique = True, nullable = False)
    bod_couple = db.Column(db.Date, nullable=False)
    respon = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

    response_fields = {
        'id' : fields.Integer,
        'user_id' : fields.Integer,
        'name_couple' : fields.String,
        'bod_couple' : fields.String,
        'respon' : fields.String
        }
   
    def __init__(self,user_id,name_couple,bod_couple,respon):
        self.user_id = user_id
        self.name_couple = name_couple
        self.bod_couple = bod_couple
        self.respon = respon
       
    def __repr__(self):
        return '<Data %r>' % self.id