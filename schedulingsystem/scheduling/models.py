from datetime import datetime
from schedulingsystem import db

class Scheduling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    initial_date = db.Column(db.DateTime, nullable=False)
    final_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meeting_room_id = db.Column(db.Integer, db.ForeignKey('meeting_room.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Agendamento - '{self.title} - {self.initial_date} até {self.final_date} '"

    def __init__(self, title, initial_date, final_date, meeting_room_id, user_id):
        self.title = title
        self.initial_date = initial_date
        self.final_date = final_date
        self.meeting_room_id = meeting_room_id
        self.user_id = user_id