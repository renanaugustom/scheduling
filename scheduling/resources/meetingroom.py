from flask_restful import Resource, reqparse

meetingrooms = []

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', dest='name', location='form', required=True, help='Meeting room name')
post_parser.add_argument('description', dest='description')

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', dest='name', location='form', required=True, help='Meeting room name')
post_parser.add_argument('description', dest='description')

class MeetingRoom(Resource):

    def get(self):
        return {'meetingRooms': meetingrooms}

    def post(self):
        args = post_parser.parse_args()
        meetingrooms.append(args)
        return {'meetingRooms' : meetingrooms}

    def put(self):
        return {'message': 'put'}

    def delete(self):
        return {'message': 'delete'}