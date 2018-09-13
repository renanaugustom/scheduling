from flask import Flask
from flask_restful import Api

from scheduling.resources.meetingroom import MeetingRoom

app = Flask(__name__)
api = Api(app)

api.add_resource(MeetingRoom, '/meetingroom')