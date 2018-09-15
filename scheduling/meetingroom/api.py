# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, marshal_with, fields
from scheduling.meetingroom.service import MeetingRoomService

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', required=True, help='Nome da sala de reunião inválido')
post_parser.add_argument('description')

meeting_room_fields = {
    "name": fields.String,
    "description": fields.String
}

class MeetingRoomApi(Resource):

    def get(self, id):
        return MeetingRoomService().get_by_id(id)

    def put(self, id):
        return {'message': 'put'}

    def delete(self, id):
        return {'message': 'delete'}

class MeetingRoomApiList(Resource):
    @marshal_with(meeting_room_fields)
    def get(self):
        return MeetingRoomService().get_all()

    def post(self):
        meeting_room = post_parser.parse_args()
        MeetingRoomService().create(meeting_room.name, meeting_room.description)
        return 'Sala de reunião criada com sucesso'