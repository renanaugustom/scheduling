from sqlalchemy import or_, and_
from schedulingsystem import db
from schedulingsystem.scheduling.models import Scheduling


def get_by_id(id):
    return Scheduling.query.filter_by(id=int(id)).first()

def get_all(filters):
    query = db.session.query(Scheduling)

    if filters is not None:

        if 'meetingroomid' in filters and filters['meetingroomid']:
            query = query.filter_by(meeting_room_id=filters['meetingroomid'])

        if 'initial_date' in filters and 'final_date' in filters and filters['initial_date'] and filters['final_date']:
            query = query.filter(or_(
                and_(Scheduling.initial_date.between(filters['initial_date'], filters['final_date'])),
                and_(Scheduling.final_date.between(filters['initial_date'], filters['final_date']))
            ))
            
    return query.all()
