# -*- coding: utf-8 -*-
import sys, os, json
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from datetime import datetime
import pytest
from schedulingsystem.scheduling.models import Scheduling
import schedulingsystem.scheduling.repository as repository

def test_get_by_id_success(test_client, init_database):
    scheduling = repository.get_by_id(1)
    assert scheduling is not None
    assert scheduling.title == 'PyTalks'

def test_get_by_id_notfound(test_client, init_database):
    scheduling = repository.get_by_id(9999)
    assert scheduling is None

def test_get_all_no_parameters(test_client, init_database):
    schedules = repository.get_all(None)
    assert len(schedules) == 3
    assert schedules[0].title == 'PyTalks'
    assert schedules[1].title == 'Python Brasil'
    assert schedules[2].title == 'Python para zumbis'    

def test_get_all_with_param_meetingroomid(test_client, init_database):
    filters = {
        'meetingroomid': 1
    }
    schedules = repository.get_all(filters)
    assert len(schedules) == 1
    assert schedules[0].title == 'PyTalks'

def test_get_all_with_params_dates(test_client, init_database):
    filters = {
        'initial_date': datetime(2018, 9, 1, 10, 0),
        'final_date': datetime(2018, 9, 1, 12, 0)
    }
    schedules = repository.get_all(filters)
    assert len(schedules) == 1
    assert schedules[0].title == 'PyTalks'

def test_get_all_with_params_dates_and_meetingroomid(test_client, init_database):
    filters = {
        'initial_date': datetime(2018, 9, 1, 10, 0),
        'final_date': datetime(2018, 9, 5, 23, 59),
        'meetingroomid': 2
    }
    schedules = repository.get_all(filters)
    assert len(schedules) == 2
    assert schedules[0].title == 'Python Brasil'

def test_get_by_user_id(test_client, init_database):
    schedules = repository.get_by_user_id(2)
    assert len(schedules) == 2