from scheduling.meetingroom.models import MeetingRoom

class MeetingRoomRepository():

    def get_by_id(self, idMeetingRoom):
        return MeetingRoom.query.filter_by(id = int(idMeetingRoom)).first()

    def get_all(self):
        return MeetingRoom.query.all()