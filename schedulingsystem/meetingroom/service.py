# -*- coding: utf-8 -*-

from schedulingsystem import db
from schedulingsystem.errors.schedulingexception import SchedulingException
from schedulingsystem.meetingroom.models import MeetingRoom
import schedulingsystem.meetingroom.repository as meeting_room_rep
import schedulingsystem.scheduling.repository as scheduling_repository


def get_by_id(id):
    meeting_room = meeting_room_rep.get_by_id(id)
    if not meeting_room:
        raise SchedulingException('Sala de reunião não encontrada.', 404)
    
    return meeting_room

def get_all():
    meeting_rooms = meeting_room_rep.get_all()
    return meeting_rooms

def create(name, description):
    meeting_room = MeetingRoom(name, description)
    validate(meeting_room)

    existing_meeting_room = meeting_room_rep.get_by_name(meeting_room.name)
    if existing_meeting_room is not None:
        raise SchedulingException('Já existe uma sala de reunião com esse nome.')

    db.session.add(meeting_room)
    db.session.commit()

def edit(id, meeting_room):
    edited_meeting_room = get_by_id(id)

    if meeting_room is None:
        raise SchedulingException("Dados da sala de reunião inválidos")

    existing_meeting_room = meeting_room_rep.get_by_name(meeting_room.name)
    if existing_meeting_room is not None and existing_meeting_room.id != id:
        raise SchedulingException('Já existe uma sala de reunião com esse nome.')

    validate(meeting_room)
    edited_meeting_room.name = meeting_room.name
    edited_meeting_room.description = meeting_room.description
    
    db.session.commit()

def delete(id):
    if can_be_deleted(id):
        meeting_room = get_by_id(id)
        db.session.delete(meeting_room)
        db.session.commit()
    else:
        raise SchedulingException('Sala de reunião não pode ser deletada pois possuí agendamentos.')

def can_be_deleted(id):
    exists_scheduling = scheduling_repository.get_by_meeting_room_id(id)

    if len(exists_scheduling) > 0:
        return False

    return True    

def validate(meeting_room):
    if not meeting_room.name or len(meeting_room.name) > 100:
        raise SchedulingException('Nome da sala de reunião inválido. Não deve ser vazio, e deve conter no máximo 100 caracteres.')

    if meeting_room.description and len(meeting_room.description) > 255:
        raise SchedulingException('Descrição da sala de reunião deve conter no máximo 255 caracteres.')

