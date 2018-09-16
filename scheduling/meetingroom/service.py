# -*- coding: utf-8 -*-

from werkzeug.exceptions import NotFound, BadRequest
from scheduling import db
from scheduling.meetingroom.repository import MeetingRoomRepository
from scheduling.meetingroom.models import MeetingRoom

class MeetingRoomService():

    def get_by_id(self, id):
        meeting_room = MeetingRoomRepository().get_by_id(id)
        if not meeting_room:
            raise NotFound('Sala de reunião não encontrada.')
        
        return meeting_room

    def get_all(self):
        meeting_rooms = MeetingRoomRepository().get_all()
        return meeting_rooms

    def create(self, name, description):
        meeting_room = MeetingRoom(name, description)
        self.validate(meeting_room)
        db.session.add(meeting_room)
        db.session.commit()

    def edit(self, id, meeting_room):
        if meeting_room is None:
            raise BadRequest("Dados da sala de reunião inválidos")

        edited_meeting_room = self.get_by_id(id)
        edited_meeting_room.name = meeting_room.name
        edited_meeting_room.description = meeting_room.description
        
        self.validate(edited_meeting_room)
        db.session.commit()

    def delete(self, id):
        meeting_room = self.get_by_id(id)
        db.session.delete(meeting_room)
        db.session.commit()
    
    def validate(self, meeting_room):
        if not meeting_room.name or len(meeting_room.name) > 100:
            raise BadRequest('Nome da sala de reunião inválido. Não deve ser vazio, e deve conter no máximo 80 caracteres.')

        if meeting_room.description and len(meeting_room.description) > 255:
            raise BadRequest('Descrição da sala de reunião deve conter no máximo 255 caracteres.')

        if self.exists_same_name(meeting_room):
            raise BadRequest('Já existe uma sala de reunião com esse nome.')

    def exists_same_name(self, meeting_room):
        existing_meeting_room = MeetingRoomRepository().get_by_name(meeting_room.name)
        
        if existing_meeting_room and existing_meeting_room.id != meeting_room.id:
            return True
        
        return False
