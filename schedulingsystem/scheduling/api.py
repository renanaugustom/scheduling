# -*- coding: utf-8 -*-
from datetime import datetime
from flask_restful import Resource, reqparse, marshal_with, fields
from schedulingsystem.scheduling.service import SchedulingService

scheduling_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "initial_date": fields.DateTime,
    "final_date": fields.DateTime,
    "user": fields.String,
    "meetingroom": fields.String
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

class SchedulingListApi(Resource):

    @marshal_with(scheduling_fields)
    def get(self):
        return SchedulingService().get_all()

    def post(self):
        scheduling = post_put_parser.parse_args()
        SchedulingService().create(scheduling.title, scheduling.initial_date,
                                   scheduling.final_date, scheduling.meeting_room_id, scheduling.user_id)
        return 'Agendamento criado com sucesso'
