from os import getenv
from dotenv import load_dotenv
load_dotenv()

class Config:
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    MONGODB_HOST = getenv('MONGODB_URI')


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_HOST = getenv('MONGODB_URI_PROD')

class TestingConfig(Config):
    TESTING = True
    MONGODB_HOST = getenv('MONGODB_URI')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
