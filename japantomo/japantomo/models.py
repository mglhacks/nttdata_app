
import datetime
from japantomo import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(120))
    country = db.Column(db.String(10))

    def __init__(self, username, email, pw_hash, ):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username