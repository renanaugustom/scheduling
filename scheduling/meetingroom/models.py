from datetime import datetime
from scheduling import db

class MeetingRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Meeting Room - '{self.name}'"

    def __init__(self, name, description):
        self.name = name
        self.description = description