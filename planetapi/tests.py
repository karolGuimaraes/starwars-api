import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))
from flask import Flask
# from starwars_api.config import Config, DevelopmentConfig
from mongoengine import *
from views import *
from models import Planet
import unittest
import json


api_test = Flask(__name__)
api_test.register_blueprint(planetapi)

api = api_test.test_client()


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        disconnect()
        host = 'mongodb://127.0.0.1:27017/'
        host2 = 'mongodb://userapi:VPIp5KCz5pMySlVM@planetapi-shard-00-00-ybuif.mongodb.net:27017,planetapi-shard-00-01-ybuif.mongodb.net:27017,planetapi-shard-00-02-ybuif.mongodb.net:27017/test?ssl=true&replicaSet=planetapi-shard-0&authSource=admin&retryWrites=true&w=majority'
        c = connect('planetapitest', host=host2)


    def test_listar_planetas(self):
        self.response = api.get('/listar')
        self.assertEqual(200, self.response.status_code)


    def test_adicionar(self):
        self.response = api.post('/adicionar', 
                                data = json.dumps(dict(nome="Sol", clima="temperate", terreno="grasslands, mountains" )), 
                                content_type='application/json')
        self.assertEqual(200, self.response.status_code)

    def test_adicionar_repetido(self):
        self.response = api.post('/adicionar', 
                                data = json.dumps(dict(nome="Sol", clima="temperate", terreno="grasslands, mountains" )), 
                                content_type='application/json')
        self.assertEqual(500, self.response.status_code)

    def test_buscar_id(self):
        self.response = api.get('/buscar_id', 
                                data = json.dumps(dict(id="1")), 
                                content_type='application/json')
        self.assertEqual(200, self.response.status_code)

    def test_buscar_id_inexistente(self):
        self.response = api.get('/buscar_id', 
                                data = json.dumps(dict(id="1000000")), 
                                content_type='application/json')
        self.assertEqual(404, self.response.status_code)

    
    def test_buscar_nome(self):
        self.response = api.get('/buscar_nome', 
                                data = json.dumps(dict(nome="Sol")), 
                                content_type='application/json')
        self.assertEqual(200, self.response.status_code)


    def test_buscar_nome_inexistente(self):
        self.response = api.get('/buscar_nome', 
                                data = json.dumps(dict(nome="Terra")), 
                                content_type='application/json')
        self.assertEqual(404, self.response.status_code)


    def test_remove_invalid_planet(self):
        self.response = api.delete('/excluir', 
                                data = json.dumps(dict(id="10000")), 
                                content_type='application/json')
        self.assertEqual(404, self.response.status_code)


    def test_excluir(self):
        self.response = api.delete('/excluir', 
                                data = json.dumps(dict(id="1")), 
                                content_type='application/json')
        self.assertEqual(200, self.response.status_code)


if __name__ == '__main__':
    unittest.main()
