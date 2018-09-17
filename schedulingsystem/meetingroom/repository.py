from schedulingsystem.meetingroom.models import MeetingRoom


def get_by_id(id):
    return MeetingRoom.query.filter_by(id = int(id)).first()

def get_all():
    return MeetingRoom.query.all()

def get_by_name(name):
    return MeetingRoom.query.filter_by(name = name).first()