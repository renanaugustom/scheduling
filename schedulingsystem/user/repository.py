from schedulingsystem.user.models import User


class UserRepository:

    def get_by_id(self, id):
        return User.query.filter_by(id=int(id)).first()

    def get_all(self):
        return User.query.all()

    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()
