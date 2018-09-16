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

from scheduling.meetingroom.api import MeetingRoomItemApi, MeetingRoomListApi
from scheduling.user.api import UserItemApi, UserListApi

api.add_resource(MeetingRoomListApi, '/meetingroom')
api.add_resource(MeetingRoomItemApi, '/meetingroom/<int:id>')
api.add_resource(UserListApi, '/user')
api.add_resource(UserItemApi, '/user/<int:id>')

