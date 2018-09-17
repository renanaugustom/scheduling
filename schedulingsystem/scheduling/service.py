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

    def create(self, title, initial_date, final_date, id_meeting_room, id_user):
        scheduling = Scheduling(title, initial_date,
                                final_date, id_meeting_room, id_user)
        self.validate(scheduling)
        
        existing_scheduling = SchedulingRepository().get_existing_by_period(
            scheduling.initial_date, scheduling.final_date).first()

        if existing_scheduling is not None:
            raise SchedulingException("Já existe agendamento para o horário desejado.")

        db.session.add(scheduling)
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