# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, marshal_with, fields
from schedulingsystem.user.service import UserService

post_put_parser = reqparse.RequestParser()
post_put_parser.add_argument('username', required=True, help='Usuário inválido')
post_put_parser.add_argument('name', required=True, help='Nome do usuário inválido')

user_fields = {
    "username": fields.String,
    "name": fields.String
}

class UserItemApi(Resource):

    @marshal_with(user_fields)
    def get(self, id):
        return UserService().get_by_id(id)

    def put(self, id):
        user = post_put_parser.parse_args()
        UserService().edit(id, user)
        return 'Usuário alterado com sucessso'

    def delete(self, id):
        UserService().delete(id)
        return 'Usuário excluído com sucesso'

class UserListApi(Resource):
    @marshal_with(user_fields)
    def get(self):
        return UserService().get_all()

    def post(self):
        user = post_put_parser.parse_args()
        UserService().create(user.username, user.name)
        return 'Usuário criado com sucesso'