# -*- coding: utf-8 -*-
import sys, os, json
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from schedulingsystem.scheduling.models import Scheduling

def test_get_success(test_client, init_database):
    response = test_client.get('/scheduling/1')
    assert response.status_code == 200

def test_get_not_found(test_client, init_database):
    response = test_client.get('/scheduling/10')
    assert response.status_code == 404

def test_get_all_success(test_client, init_database):
    response = test_client.get('scheduling')
    assert response.status_code == 200
    assert len(response.json) == 3

def test_post_success(test_client, init_database):
    response = test_client.post('/scheduling', 
        data=json.dumps(dict(title='Python para iniciantes', initial_date='2018-09-18T04:00:00', 
             final_date='2018-09-18T05:00:00', meeting_room_id=1, user_id=1)),
        content_type='application/json')
    assert response.status_code == 200
    assert response.json == 'Agendamento criado com sucesso'

def test_put_success(test_client, init_database):
    response = test_client.put('/scheduling/3', 
        data=json.dumps(dict(title='Python para iniciantes', initial_date='2018-09-18T04:00:00', 
             final_date='2018-09-18T08:00:00', meeting_room_id=2, user_id=2)),
        content_type='application/json')
    assert response.status_code == 200

def test_put_not_found(test_client, init_database):
    response = test_client.put('/scheduling/20', 
        data=json.dumps(dict(title='Python para iniciantes', initial_date='2018-09-18T04:00:00', 
             final_date='2018-09-18T08:00:00', meeting_room_id=2, user_id=2)),
        content_type='application/json')
    assert response.status_code == 404

def test_delete_success(test_client, init_database):
    response = test_client.delete('/scheduling/3')
    assert response.status_code == 200

def test_delete_not_found(test_client, init_database):
    response = test_client.delete('/scheduling/100')
    assert response.status_code == 404