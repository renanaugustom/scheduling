# -*- coding: utf-8 -*-

from werkzeug.exceptions import NotFound, BadRequest
from scheduling import db
from scheduling.user.repository import UserRepository
from scheduling.user.models import User

class UserService():

    def get_by_id(self, id):
        user = UserRepository().get_by_id(id)
        if not user:
            raise NotFound('Usuário não encontrado.')
        
        return user

    def get_all(self):
        users = UserRepository().get_all()
        return users

    def create(self, username, name):
        user = User(username, name)
        self.validate(user)
        db.session.add(user)
        db.session.commit()

    def edit(self, id, user):
        if user is None:
            raise BadRequest("Dados do usuário inválidos")

        edited_user = self.get_by_id(id)
        edited_user.username = user.username
        edited_user.name = user.name
        
        self.validate(edited_user)
        db.session.commit()

    def delete(self, id):
        user = self.get_by_id(id)
        db.session.delete(user)
        db.session.commit()
    
    def validate(self, user):
        if not user.username or len(user.username) > 40:
            raise BadRequest('Usuário inválido. Não deve ser vazio e deve conter no máximo 40 caracteres.')

        if not user.name or len(user.name) > 100:
            raise BadRequest('Nome do usuário inválido. Não deve ser vazio e deve conter no máximo 100 caracteres.')

        if self.exists_same_username(user):
            raise BadRequest('Usuário já existente.')

    def exists_same_username(self, user):
        existing_user = UserRepository().get_by_username(user.username)
        
        if existing_user and existing_user.id != user.id:
            return True
        
        return False