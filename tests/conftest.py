import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from schedulingsystem import create_app, db
from config import ConfigTest

from schedulingsystem.user.models import User
from schedulingsystem.meetingroom.models import MeetingRoom

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(ConfigTest)

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!
    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    user1 = User(username='rnnaugusto', name='Renan Augusto')
    user2 = User(username='joaosilva', name='João da Silva')
    db.session.add(user1)
    db.session.add(user2)

    meeting_room1 = MeetingRoom(name='Room A', description="Description A")
    meeting_room2 = MeetingRoom(name='Room B', description="Description B")
    db.session.add(meeting_room1)
    db.session.add(meeting_room2)

    db.session.commit()

    yield db 

    db.drop_all()
