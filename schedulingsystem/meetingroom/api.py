# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, marshal_with, fields
from schedulingsystem.meetingroom.service import MeetingRoomService

post_put_parser = reqparse.RequestParser()
post_put_parser.add_argument('name', required=True, help='Nome da sala de reunião inválido')
post_put_parser.add_argument('description')

meeting_room_fields = {
    "name": fields.String,
    "description": fields.String
}

class MeetingRoomItemApi(Resource):

    @marshal_with(meeting_room_fields)
    def get(self, id):
        return MeetingRoomService().get_by_id(id)

    def put(self, id):
        meeting_room = post_put_parser.parse_args()
        MeetingRoomService().edit(id, meeting_room)
        return 'Sala de reunião alterada com sucessso'

    def delete(self, id):
        MeetingRoomService().delete(id)
        return 'Sala de reunião excluída com sucesso'

class MeetingRoomListApi(Resource):
    @marshal_with(meeting_room_fields)
    def get(self):
        return MeetingRoomService().get_all()

    def post(self):
        meeting_room = post_put_parser.parse_args()
        MeetingRoomService().create(meeting_room.name, meeting_room.description)
        return 'Sala de reunião criada com sucesso'