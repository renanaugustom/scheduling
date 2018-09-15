# -*- coding: utf-8 -*-

from werkzeug.exceptions import NotFound
from flask import abort
from scheduling import db
from scheduling.meetingroom.repository import MeetingRoomRepository
from scheduling.meetingroom.models import MeetingRoom

class MeetingRoomService():

    def get_by_id(self, id):
        meetingRoom = MeetingRoomRepository().get_by_id(id)
        if not meetingRoom:
            abort(404, u'Sala de reunião não encontrada.')
        
        return meetingRoom

    def get_all(self):
        meetingRooms = MeetingRoomRepository().get_all()
        return meetingRooms

    def create(self, name, description):
        meetingRoom = MeetingRoom(name, description)
        validate(meetingRoom)
        db.session.add(meetingRoom)
        db.session.commit()


    def validate(meetingroom):
        if meetingroom is None:
            raise Exception('Dados da Sala de Reunião não encontrados.')

        if not meetingroom.name or len(meetingroom.name) > 80:
            raise Exception('Nome da sala de reunião inválido. Não deve ser vazio, e deve conter no máximo 80 caracteres.')

        if meetingroom.description and len(meetingroom.description) > 255:
            raise Exception('Descrição da sala de reunião deve conter no máximo 255 caracteres.')