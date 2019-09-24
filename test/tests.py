import sys
sys.path.insert(1, '')
from config import Config, DevelopmentConfig
from flask import Flask
from mongoengine import disconnect, connect
from mongoengine.connection import _get_db
from planet_api.views import planetapi
import unittest
import json

api_test = Flask(__name__)
api_test.register_blueprint(planetapi)
api = api_test.test_client()

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        disconnect()
        connect('planetapitest', host=Config.MONGODB_HOST )


    def teste_listar_planetas(self):
        self.response = api.get('/listar')
        self.assertEqual(200, self.response.status_code)


    def teste_adicionar_planeta(self):
        self.response = api.post('/adicionar', 
                                data = json.dumps(dict(nome="Sol", clima="temperate", terreno="grasslands, mountains" )), 
                                content_type='application/json')
        self.assertEqual(200, self.response.status_code)

    def teste_adicionar_planeta_repetido(self):
        self.response = api.post('/adicionar', 
                                data = json.dumps(dict(nome="Sol", clima="temperate", terreno="grasslands, mountains" )), 
                                content_type='application/json')
        self.assertEqual(500, self.response.status_code)

    def teste_busca_por_id(self):
        self.response = api.get('/buscar_id/1')
        self.assertEqual(200, self.response.status_code)

    def teste_buscar_por_id_inexistente(self):
        self.response = api.get('/buscar_id/1000000')
        self.assertEqual(404, self.response.status_code)

    
    def teste_buscar_por_nome(self):
        self.response = api.get('/buscar_nome/Sol')
        self.assertEqual(200, self.response.status_code)


    def teste_buscar_por_nome_inexistente(self):
        self.response = api.get('/buscar_nome/Terra')
        self.assertEqual(404, self.response.status_code)


    def teste_excluir_planeta_inexistente(self):
        self.response = api.delete('/excluir/1000000')
        self.assertEqual(404, self.response.status_code)


    def teste_excluir_planeta(self):
        self.response = api.delete('/excluir/1')
        self.assertEqual(200, self.response.status_code)

if __name__ == '__main__':
    unittest.main()
