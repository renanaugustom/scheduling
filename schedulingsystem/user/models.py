from datetime import datetime
from schedulingsystem import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    schedulings = db.relationship('Scheduling', backref='user', lazy=True)

    def __repr__(self):
        return self.username

    def __init__(self, username, name):
        self.username = username
        self.name = name