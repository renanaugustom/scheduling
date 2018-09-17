from sqlalchemy import or_, and_
from schedulingsystem import db
from schedulingsystem.scheduling.models import Scheduling


class SchedulingRepository:

    def get_by_id(self, id):
        return Scheduling.query.filter_by(id=int(id)).first()

    def get_by_meeting_room_id(self, meeting_room_id):
        return Scheduling.query.filter_by(meeting_room_id=meeting_room_id)\
            .order_by(Scheduling.final_date.desc())

    def get_by_period(self, initial_date, final_date):
        return Scheduling.query.filter(or_(
            and_(Scheduling.initial_date.between(initial_date, final_date)),
            and_(Scheduling.final_date.between(initial_date, final_date))
        ))

    def get_existing_by_meeting_room_and_period(self, meeting_room_id, initial_date, final_date):
        return Scheduling.query.filter(
            and_(Scheduling.meeting_room_id == meeting_room_id,
                 or_(
                     and_(Scheduling.initial_date.between(initial_date, final_date)),
                     and_(Scheduling.final_date.between(initial_date, final_date)))
                 ))

    def get_all(self):
        return Scheduling.query.all()
