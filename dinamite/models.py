from dinamite.ext.database import db
from sqlalchemy_serializer import SerializerMixin

class Services(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(30))


class Users(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    