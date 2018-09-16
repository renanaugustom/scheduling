import os

class ConfigTest:
    ERROR_404_HELP = False
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
