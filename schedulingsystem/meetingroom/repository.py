from schedulingsystem.meetingroom.models import MeetingRoom

class MeetingRoomRepository:

    def get_by_id(self, id):
        return MeetingRoom.query.filter_by(id = int(id)).first()

    def get_all(self):
        return MeetingRoom.query.all()

    def get_by_name(self, name):
        return MeetingRoom.query.filter_by(name = name).first()