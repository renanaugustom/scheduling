# -*- coding: utf-8 -*-
import sys, os, json
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from schedulingsystem.errors.schedulingexception import SchedulingException
from schedulingsystem.meetingroom.models import MeetingRoom
import schedulingsystem.meetingroom.service as service

def test_create_success(test_client, init_database):
    service.create('Room C', 'Description C')
    meeting_rooms = service.get_all()
    assert len(meeting_rooms) == 3
    assert meeting_rooms[2].name == 'Room C'
    assert meeting_rooms[2].description == 'Description C'

def test_create_error_meeting_room_already_exists(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        service.create('Room C', '')
    assert e_info.value.message == "Já existe uma sala de reunião com esse nome."

def test_create_error_name_invalid(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        invalid_name = ''.join('a' for _ in range(101))
        service.create(invalid_name, '')
    assert e_info.value.message == "Nome da sala de reunião inválido. Não deve ser vazio, e deve conter no máximo 100 caracteres."

def test_create_error_description_invalid(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        invalid_description = ''.join('a' for _ in range(256))
        service.create('Room D', invalid_description)
    assert e_info.value.message == "Descrição da sala de reunião deve conter no máximo 255 caracteres."

def test_edit_error_meeting_room_in_use(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        meeting_room = MeetingRoom('Room A', '')
        service.edit(3, meeting_room)
    assert e_info.value.message == "Já existe uma sala de reunião com esse nome."

def test_delete_error_meeting_room_in_use(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        service.delete(1)
    assert e_info.value.message == "Sala de reunião não pode ser deletada pois possuí agendamentos."

def test_delete_success(test_client, init_database):
    service.delete(3)
    meeting_rooms = service.get_all()
    assert len(meeting_rooms) == 2
