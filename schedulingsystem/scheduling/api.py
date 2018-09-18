# -*- coding: utf-8 -*-
from datetime import datetime
from flask_restful import Resource, reqparse, marshal_with, fields
import schedulingsystem.scheduling.service as scheduling_service

scheduling_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "initial_date": fields.DateTime,
    "final_date": fields.DateTime,
    "user": fields.String,
    "user_id": fields.Integer,
    "meetingroom": fields.String,
    "meeting_room_id": fields.Integer,
}

post_put_parser = reqparse.RequestParser()
post_put_parser.add_argument(
    'title', required=True, help='Título do agendamento')
post_put_parser.add_argument('initial_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
                             required=True, help="Data inicial do agendamento inválida")
post_put_parser.add_argument(
    'final_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
    required=True, help="Data final do agendamento inválida")
post_put_parser.add_argument(
    'meeting_room_id', type=int, required=True, help='Sala de reunião inválida')
post_put_parser.add_argument(
    'user_id', type=int, required=True, help='Usuário inválido')

get_parser = reqparse.RequestParser()
get_parser.add_argument('meetingroomid', type=int, location='args')
get_parser.add_argument('initial_date', type=lambda x: datetime.strptime(
    x, '%Y-%m-%dT%H:%M:%S'), location='args')
get_parser.add_argument('final_date', type=lambda x: datetime.strptime(
    x, '%Y-%m-%dT%H:%M:%S'), location='args')


class SchedulingItemApi(Resource):

    @marshal_with(scheduling_fields)
    def get(self, id):
        return scheduling_service.get_by_id(id)

    def put(self, id):
        scheduling = post_put_parser.parse_args()
        scheduling_service.edit(id, scheduling)
        return 'Agendamento alterado com sucessso'

    def delete(self, id):
        scheduling_service.delete(id)
        return 'Agendamento excluído com sucesso'


class SchedulingListApi(Resource):

    @marshal_with(scheduling_fields)
    def get(self):
        filters = get_parser.parse_args()
        return scheduling_service.get_all(filters)

    def post(self):
        scheduling = post_put_parser.parse_args()
        scheduling_service.create(scheduling.title, scheduling.initial_date,
                                  scheduling.final_date, scheduling.meeting_room_id, scheduling.user_id)
        return 'Agendamento criado com sucesso'
