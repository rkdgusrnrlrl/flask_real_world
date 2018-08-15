import os

class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = APP_DIR

class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///realworld.db"

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///realworld.db"


class TestConfig(Config):
    ENV = "TEST"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"