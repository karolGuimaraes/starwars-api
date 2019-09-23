from flask import Flask, Blueprint
from config import Config, DevelopmentConfig
from planetapi.views import planetapi
from mongoengine import connect, disconnect

api = Flask(__name__)

with api.app_context():
    disconnect()
    host = Config.MONGODB_HOST 
    connect('planetapi', host=host)
    api.register_blueprint(planetapi)
