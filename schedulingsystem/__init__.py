# -*- coding: utf-8 -*-

from flask import Flask, got_request_exception, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from schedulingsystem.config import Config

db = SQLAlchemy()
migrate = Migrate()

def handle_scheduling_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api = Api(app, catch_all_404s=True)
    api.handle_error = handle_scheduling_exception
    db.init_app(app)
    migrate.init_app(app, db)

    from schedulingsystem import models
    from schedulingsystem.meetingroom.api import MeetingRoomItemApi, MeetingRoomListApi
    from schedulingsystem.user.api import UserItemApi, UserListApi
    from schedulingsystem.scheduling.api import SchedulingListApi

    api.add_resource(MeetingRoomListApi, '/meetingroom')
    api.add_resource(MeetingRoomItemApi, '/meetingroom/<int:id>')
    api.add_resource(UserListApi, '/user')
    api.add_resource(UserItemApi, '/user/<int:id>')
    api.add_resource(SchedulingListApi, '/scheduling')
    

    return app
