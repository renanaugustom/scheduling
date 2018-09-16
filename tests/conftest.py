import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from scheduling import create_app, db
from config import ConfigTest
from scheduling.user.models import User

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

    # Insert user data
    user1 = User(username='rnnaugusto', name='Renan Augusto')
    user2 = User(username='joaosilva', name='João da Silva')
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    yield db 

    db.drop_all()
