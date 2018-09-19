# -*- coding: utf-8 -*-
import sys
import os
import json
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from datetime import datetime
import pytest
from schedulingsystem.errors.schedulingexception import SchedulingException
from schedulingsystem.scheduling.models import Scheduling
import schedulingsystem.scheduling.service as service


def test_create_title_invalid(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        service.create(None, datetime(2018, 1, 1), datetime(2018, 1, 1), 1, 1)
    assert e_info.value.message == 'Título do agendamento inválido. Não deve ser vazio, e deve conter no máximo 80 caracteres.'


def test_create_title_invalid_length(test_client, init_database):
    invalid_title = ''.join('a' for _ in range(90))
    with pytest.raises(SchedulingException) as e_info:
        service.create(invalid_title, datetime(2018, 1, 1), datetime(2018, 1, 1), 1, 1)
    assert e_info.value.message == 'Título do agendamento inválido. Não deve ser vazio, e deve conter no máximo 80 caracteres.'

def test_create_invalid_period(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        service.create('Title', datetime(2018, 1, 2), datetime(2018, 1, 1), 1, 1)
    assert e_info.value.message == 'Data inicial do agendamento não pode ser maior que a data final do agendamento'

def test_create_scheduling_same_room_invalid_period(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        service.create('Title', datetime(2018, 9, 1, 10, 0), datetime(2018, 9, 1, 11, 0), 1, 1)
    assert e_info.value.message == 'Já existe agendamento para o horário desejado.'

def test_create_scheduling_sucess():
    service.create('Title', datetime(2018, 9, 1, 10, 0), datetime(2018, 9, 1, 11, 0), 2, 1)
    schedules = service.get_all(None)
    assert len(schedules) == 4

def test_edit_scheduling_same_room_invalid_period(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        scheduling = Scheduling('Title', datetime(2018, 9, 2, 8, 0), datetime(2018, 9, 2, 12, 0), 2, 2)
        service.edit(3, scheduling)
    assert e_info.value.message == 'Já existe agendamento para o horário desejado.'

def test_edit_success(test_client, init_database):
    scheduling = Scheduling('New Title', datetime(2018, 9, 2, 10, 30), datetime(2018, 9, 2, 12, 0), 2, 2)
    service.edit(3, scheduling)
    
    edited_scheduling = service.get_by_id(3)
    assert edited_scheduling.title == 'New Title'
    assert edited_scheduling.initial_date == datetime(2018, 9, 2, 10, 30)

def test_edit_not_found(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        scheduling = Scheduling('New Title', datetime(2018, 9, 2, 10, 30), datetime(2018, 9, 2, 12, 0), 2, 2)
        service.edit(20, scheduling)
    assert e_info.value.message == 'Agendamento não encontrado.'

def test_delete_success(test_client, init_database):
    schedules = service.get_all(None)
    assert len(schedules) == 4

    service.delete(1)
    
    schedules = service.get_all(None)
    assert len(schedules) == 3
    assert schedules[0].id == 2

def test_delete_not_foud(test_client, init_database):
    with pytest.raises(SchedulingException) as e_info:
        service.delete(1000)
    assert e_info.value.message == 'Agendamento não encontrado.'

def test_get_all_without_parameters(test_client, init_database):
    schedules = service.get_all(None)
    assert len(schedules) == 3

def test_get_all_with_params_date(test_client, init_database):
    filters = {
        'initial_date': datetime(2018, 9, 1, 10, 0),
        'final_date': datetime(2018, 9, 1, 12, 0)
    }
    schedules = service.get_all(filters)
    assert len(schedules) == 1