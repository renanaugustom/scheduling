# -*- coding: utf-8 -*-
from schedulingsystem import db
from schedulingsystem.errors.schedulingexception import SchedulingException
from schedulingsystem.user.models import User
import schedulingsystem.scheduling.repository as scheduling_repository
import schedulingsystem.user.repository as user_repository

def get_by_id(id):
    user = user_repository.get_by_id(id)

    if user is None:
        raise SchedulingException('Usuário não encontrado.', 404)

    return user

def get_all():
    users = user_repository.get_all()
    return users

def create(username, name):
    user = User(username, name)
    validate(user)

    existing_user = user_repository.get_by_username(user.username)
    if existing_user is not None:
        raise SchedulingException("Usuário já existente")

    db.session.add(user)
    db.session.commit()

def edit(id, user):
    edited_user = get_by_id(id)

    if user is None:
        raise SchedulingException("Dados do usuário inválidos")

    existing_user = user_repository.get_by_username(user.username)
    if existing_user is not None and existing_user.id != id:
        raise SchedulingException("Usuário já existente")

    validate(user)

    edited_user.username = user.username
    edited_user.name = user.name

    db.session.commit()

def delete(id):
    if can_be_deleted(id):
        user = get_by_id(id)
        db.session.delete(user)
        db.session.commit()
    else:
        raise SchedulingException('Usuário não pode ser deletado pois possuí agendamentos')

def validate(user):
    if not user.username or len(user.username) > 40:
        raise SchedulingException(
            'Usuário inválido. Não deve ser vazio e deve conter no máximo 40 caracteres.')

    if not user.name or len(user.name) > 100:
        raise SchedulingException(
            'Nome do usuário inválido. Não deve ser vazio e deve conter no máximo 100 caracteres.')

def can_be_deleted(id):
    exists_scheduling = scheduling_repository.get_by_user_id(id)

    if len(exists_scheduling) > 0:
        return False

    return True
