from flask_restful import Resource, reqparse
from scheduling.meetingroom.service import MeetingRoomService

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', dest='name', location='form', required=True, help='Meeting room name')
post_parser.add_argument('description', dest='description')

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', dest='name', location='form', required=True, help='Meeting room name')
post_parser.add_argument('description', dest='description')

class MeetingRoomApi(Resource):

    def get(self, id):
        return MeetingRoomService().get_by_id(id)

    def put(self, id):
        return {'message': 'put'}

    def delete(self, id):
        return {'message': 'delete'}

class MeetingRoomApiList(Resource):
    def get(self):
        return MeetingRoomService().get_all()

    def post(self):
        return {'message': 'post'}