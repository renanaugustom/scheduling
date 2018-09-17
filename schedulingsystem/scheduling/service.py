# -*- coding: utf-8 -*-
import datetime
from schedulingsystem import db
from schedulingsystem.errors.schedulingexception import SchedulingException
from schedulingsystem.scheduling.models import Scheduling
from schedulingsystem.scheduling.repository import SchedulingRepository
from schedulingsystem.meetingroom.service import MeetingRoomService
from schedulingsystem.user.service import UserService


class SchedulingService:
    def get_all(self):
        schedules = SchedulingRepository().get_all()
        return schedules

    def get_by_id(self, id):
        scheduling = SchedulingRepository().get_by_id(id)
        if not scheduling:
            raise SchedulingException('Agendamento não encontrado.', 404)

        return scheduling

    def get_by_meeting_room_id(self, meeting_room_id):
        return SchedulingRepository().get_by_meeting_room_id(meeting_room_id)

    def get_by_period(self, initial_date, final_date):
        return SchedulingRepository().get_by_period(initial_date, final_date)

    def create(self, title, initial_date, final_date, id_meeting_room, id_user):
        scheduling = Scheduling(title, initial_date,
                                final_date, id_meeting_room, id_user)
        self.validate(scheduling)

        existing_scheduling = SchedulingRepository().get_existing_by_meeting_room_and_period(
            scheduling.meeting_room_id, scheduling.initial_date, scheduling.final_date).first()

        if existing_scheduling is not None:
            raise SchedulingException(
                "Já existe agendamento para a sala e o horário desejado.")

        db.session.add(scheduling)
        db.session.commit()

    def edit(self, id, scheduling):
        if scheduling is None:
            raise SchedulingException("Dados do agendamento inválidos")

        existing_scheduling = SchedulingRepository().get_existing_by_meeting_room_and_period(
            scheduling.meeting_room_id, scheduling.initial_date, scheduling.final_date).first()

        if existing_scheduling is not None and existing_scheduling.id != id:
            raise SchedulingException(
                "Já existe agendamento para a sala e o horário desejado.")

        edited_scheduling = self.get_by_id(id)
        edited_scheduling.title = scheduling.title
        edited_scheduling.initial_date = scheduling.initial_date
        edited_scheduling.final_date = scheduling.final_date
        edited_scheduling.meeting_room_id = scheduling.meeting_room_id
        edited_scheduling.user_id = scheduling.user_id

        self.validate(edited_scheduling)
        db.session.commit()

    def delete(self, id):
        user = self.get_by_id(id)
        db.session.delete(user)
        db.session.commit()

    def validate(self, scheduling):
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

        meeting_room = MeetingRoomService().get_by_id(scheduling.meeting_room_id)
        user = UserService().get_by_id(scheduling.user_id)
