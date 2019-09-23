from planet_api import api
from config import Config, DevelopmentConfig

if __name__ == '__main__':
    host = '0.0.0.0'
    debug = Config.DEBUG
    port = Config.APP_PORT
    api.run(host=host, port=port, debug=debug)
