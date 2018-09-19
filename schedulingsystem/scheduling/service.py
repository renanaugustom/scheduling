# -*- coding: utf-8 -*-
import datetime
from schedulingsystem import db
from schedulingsystem.errors.schedulingexception import SchedulingException
from schedulingsystem.scheduling.models import Scheduling
import schedulingsystem.scheduling.repository as scheduling_rep
import schedulingsystem.meetingroom.repository as meeting_room_repository
import schedulingsystem.user.repository as user_repository

def get_all(filters):
    schedules = scheduling_rep.get_all(filters)
    return schedules

def get_by_id(id):
    scheduling = scheduling_rep.get_by_id(id)
    if not scheduling:
        raise SchedulingException('Agendamento não encontrado.', 404)

    return scheduling

def get_by_user_id(user_id):
    schedules = scheduling_rep.get_by_user_id(user_id)
    return schedules

def create(title, initial_date, final_date, id_meeting_room, id_user):
    scheduling = Scheduling(title, initial_date,
                            final_date, id_meeting_room, id_user)
    validate(scheduling)

    filters = {
        'meetingroomid': scheduling.meeting_room_id, 
        'initial_date': scheduling.initial_date, 
        'final_date': scheduling.final_date
    }
    existing_schedules = scheduling_rep.get_all(filters)

    if len(existing_schedules) > 0:
        raise SchedulingException(
            "Já existe agendamento para a sala e o horário desejado.")

    db.session.add(scheduling)
    db.session.commit()

def edit(id, scheduling):
    edited_scheduling = get_by_id(id)

    if scheduling is None:
        raise SchedulingException("Dados do agendamento inválidos")

    validate(scheduling)

    edited_scheduling.title = scheduling.title
    edited_scheduling.initial_date = scheduling.initial_date
    edited_scheduling.final_date = scheduling.final_date
    edited_scheduling.meeting_room_id = scheduling.meeting_room_id
    edited_scheduling.user_id = scheduling.user_id

    filters = {
        'meetingroomid': edited_scheduling.meeting_room_id, 
        'initial_date': edited_scheduling.initial_date, 
        'final_date': edited_scheduling.final_date
    }

    existing_schedules = scheduling_rep.get_all(filters)

    if len([schedule for schedule in existing_schedules if schedule.id != id]):
        raise SchedulingException(
            "Já existe agendamento para a sala e o horário desejado.")
    
    db.session.commit()

def delete(id):
    user = get_by_id(id)
    db.session.delete(user)
    db.session.commit()

def validate(scheduling):
    if not scheduling.title or len(scheduling.title) > 80:
        raise SchedulingException(
            'Título do agendamento inválido. Não deve ser vazio, e deve conter no máximo 80 caracteres.')

    if not scheduling.initial_date:
        raise SchedulingException(
            'É obrigatório informar a data inicial do agendamento.')

    if not scheduling.final_date:
        raise SchedulingException(
            'É obrigatório informar a data final do agendamento.')

    if not isinstance(scheduling.initial_date, datetime.datetime):
        raise SchedulingException('Data inicial do agendamento inválida')

    if not isinstance(scheduling.final_date, datetime.datetime):
        raise SchedulingException('Data final do agendamento inválida')

    if scheduling.initial_date > scheduling.final_date:
        raise SchedulingException(
            'Data inicial do agendamento não pode ser maior que a data final do agendamento')

    meeting_room = meeting_room_repository.get_by_id(scheduling.meeting_room_id)
    user = user_repository.get_by_id(scheduling.user_id)
