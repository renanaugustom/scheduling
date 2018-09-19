# -*- coding: utf-8 -*-
import sys, os, json
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from schedulingsystem.errors.schedulingexception import SchedulingException
from schedulingsystem.user.models import User
import schedulingsystem.user.service as service

def test_create_success(test_client, init_database):
    service.create('pedrosilva', 'Pedro Silva')
    users = service.get_all()
    assert len(users) == 3
    assert users[2].username == 'pedrosilva'
    assert users[2].name == 'Pedro Silva'

def test_create_error_user_already_exists(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        service.create('pedrosilva', 'Pedro José Silva')
    assert e_info.value.message == "Usuário já existente"

def test_create_error_username_invalid(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        invalid_username = ''.join('a' for _ in range(90))
        service.create(invalid_username, 'Pedro José Silva')
    assert e_info.value.message == "Usuário inválido. Não deve ser vazio e deve conter no máximo 40 caracteres."

def test_create_error_name_invalid(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        invalid_name = ''.join('a' for _ in range(101))
        service.create('pedrosilva', invalid_name)
    assert e_info.value.message == "Nome do usuário inválido. Não deve ser vazio e deve conter no máximo 100 caracteres."

def test_edit_error_user_in_use(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        user = User('rnnaugusto', 'renan')
        service.edit(3, user)
    assert e_info.value.message == "Usuário já existente"

def test_delete_error_user_in_use(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        service.delete(1)
    assert e_info.value.message == "Usuário não pode ser deletado pois possuí agendamentos"

def test_delete_success(test_client, init_database):
    service.delete(3)
    users = service.get_all()
    assert len(users) == 2


    
    