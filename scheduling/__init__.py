from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from scheduling.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api = Api(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from scheduling.meetingroom.api import MeetingRoomItemApi, MeetingRoomListApi
    from scheduling.user.api import UserItemApi, UserListApi

    api.add_resource(MeetingRoomListApi, '/meetingroom')
    api.add_resource(MeetingRoomItemApi, '/meetingroom/<int:id>')
    api.add_resource(UserListApi, '/user')
    api.add_resource(UserItemApi, '/user/<int:id>')

    return app

