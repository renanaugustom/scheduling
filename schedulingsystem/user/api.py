# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, marshal_with, fields
import schedulingsystem.user.service as user_service

post_put_parser = reqparse.RequestParser()
post_put_parser.add_argument(
    'username', required=True, help='Usuário inválido')
post_put_parser.add_argument(
    'name', required=True, help='Nome do usuário inválido')

user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "name": fields.String
}


class UserItemApi(Resource):

    @marshal_with(user_fields)
    def get(self, id):
        return user_service.get_by_id(id)

    def put(self, id):
        user = post_put_parser.parse_args()
        user_service.edit(id, user)
        return 'Usuário alterado com sucessso'

    def delete(self, id):
        user_service.delete(id)
        return 'Usuário excluído com sucesso'


class UserListApi(Resource):
    @marshal_with(user_fields)
    def get(self):
        return user_service.get_all()

    def post(self):
        user = post_put_parser.parse_args()
        user_service.create(user.username, user.name)
        return 'Usuário criado com sucesso'
