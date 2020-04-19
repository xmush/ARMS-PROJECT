from blueprints import db
from flask_restful import fields
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.sql import func
from datetime import datetime
# from blueprints.client.model import Client

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    status = db.Column(db.Boolean, nullable = False)
    salt = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

    response_fields = {
        'id' : fields.Integer,
        'name' : fields.String,
        'password' : fields.String,
        'status' : fields.String
    }
    # jwt_claim_fields = {
    #     'client_key' : fields.String,
    #     'status' : fields.String,
    #     'internal' : fields.Boolean 
    # }


    def __init__(self,name,password,salt,status):
        self.name = name
        self.password = password
        self.salt = salt
        self.status = status

    def __repr__(self):
        return '<User %r>' % self.id