from blueprints import db
from flask_restful import fields

class Client(db.Model):
    __tablename__ = "client"
    client_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    client_key = db.Column(db.String(50), unique = True, nullable = False)
    client_secret = db.Column(db.String(255), nullable = False, default = 20)
    salt = db.Column(db.String(255))
    status = db.Column(db.String(10), nullable = False)
    internal = db.Column(db.Boolean)

    response_fields = {
        'client_id' : fields.Integer,
        'client_key' : fields.String,
        'client_secret' : fields.String,
        'internal' : fields.Boolean
    }    
    jwt_claim_fields = {
        'client_key' : fields.String,
        'internal' : fields.Boolean 
    }

    def __init__(self,client_key,client_secret,salt,status, internal):
        self.client_key = client_key
        self.client_secret = client_secret
        self.salt = salt
        self.internal = internal

    def __repr__(self):
        return '<Client %r>' % self.client_id