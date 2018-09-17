from schedulingsystem.user.models import User


def get_by_id(id):
    return User.query.filter_by(id=int(id)).first()

def get_all():
    return User.query.all()

def get_by_username(username):
    return User.query.filter_by(username=username).first()
