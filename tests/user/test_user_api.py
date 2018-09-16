# -*- coding: utf-8 -*-
import sys, os, json
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from schedulingsystem.user.models import User

def test_get_success(test_client, init_database):
    response = test_client.get('/user/1')
    assert response.status_code == 200

def test_get_not_found(test_client, init_database):
    response = test_client.get('/user/10')
    assert response.status_code == 404

def test_get_all_success(test_client, init_database):
    response = test_client.get('user')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_post_success(test_client, init_database):
    response = test_client.post('/user', 
        data=json.dumps(dict(username='maria', name='Maria Silva')),
        content_type='application/json')
    assert response.status_code == 200

def test_put_success(test_client, init_database):
    response = test_client.put('/user/3', 
        data=json.dumps(dict(username='mariasilva', name='Maria Silva')),
        content_type='application/json')
    assert response.status_code == 200

def test_put_not_found(test_client, init_database):
    response = test_client.put('/user/100', 
        data=json.dumps(dict(username='mariasilva', name='Maria Silva')),
        content_type='application/json')
    assert response.status_code == 404

def test_delete_success(test_client, init_database):
    response = test_client.delete('/user/3')
    assert response.status_code == 200

def test_delete_not_found(test_client, init_database):
    response = test_client.delete('/user/100')
    assert response.status_code == 404