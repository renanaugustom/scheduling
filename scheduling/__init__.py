from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduling.db'
app.config['ERROR_404_HELP'] = False
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from scheduling.meetingroom.api import MeetingRoomApi, MeetingRoomApiList

api.add_resource(MeetingRoomApiList, '/meetingroom')
api.add_resource(MeetingRoomApi, '/meetingroom/<int:id>')