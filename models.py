from app import db

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(30))

    def __repr__(self):
        return "<Name %r>" % self.name


class Users(db.Model):
    nickname = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return "<Name %r>" % self.name