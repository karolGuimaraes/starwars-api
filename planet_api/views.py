from flask import request, jsonify, Blueprint
from .models import Planet
import json
import requests
from mongoengine import NotUniqueError 

planetapi = Blueprint('planetapi', __name__)


@planetapi.route('/')
@planetapi.route('/listar', methods=['GET'])
def listar_planetas():
    try:
        planetas = Planet.objects()
        return jsonify({'data': [planeta.json() for planeta in planetas ] }), 200
    except:
        return jsonify({'Error': 'Internal server error :('}), 500

@planetapi.route('/adicionar', methods=['POST'])
def adicionar_planeta():
    try:
        data = request.get_json()
        teste = Planet(nome=data['nome'], clima=data['clima'], terreno=data['terreno'], _id=Planet.objects.count() + 1).save()
        teste.save()
        return jsonify({ 'data': "Planeta criado " }), 200
    except (NotUniqueError) as error:
        return jsonify({'Error': "Já  existe um planeta com esse nome" }), 500
    except Exception as error:
        return jsonify({'Error': str(error) }), 500


@planetapi.route('/buscar_nome/<string:name>', methods=['GET'])
def buscar_por_nome(name):
    try:
        if Planet.objects( nome = name):
            planet_obj = Planet.objects.get(nome=name)
            planeta = planet_obj.json()
            planeta.update({"aparicoes": aparicoes(planet_obj) })
            return jsonify({'data': [ planeta ] }), 200
        else:
            return jsonify({ 'mensagem': "Planeta não foi encontrado pelo nome" }), 404
    except:
        return jsonify({'Error': 'Internal server error :('}), 500


@planetapi.route('/buscar_id/<int:id>', methods=['GET'])
def buscar_por_id(id=None):
    try:
        if Planet.objects( _id = id ):
            planet_obj = Planet.objects.get(_id=id)
            planeta = planet_obj.json()
            planeta.update({"aparicoes": aparicoes(planet_obj) })
            return jsonify({'data': [ planeta ] }), 200
        else:
            return jsonify({ 'mensagem': "Planeta não foi encontrado pelo id" }), 404
    except:
        return jsonify({'Error': 'Internal server error :('}), 500


@planetapi.route('/excluir/<int:id>', methods=['DELETE'])
def remover_planeta(id):
    try:
        if Planet.objects.filter(_id=id):
            planeta = Planet.objects.get(_id=id)
            planeta.delete()
            return jsonify({ 'mensagem': "Planeta foi excluído com sucesso" }), 200
        else:
            return jsonify({ 'mensagem': "Planeta não foi encontrado pelo id" }), 404
    except:
        return jsonify({'Error': 'Internal server error :('}), 500


def aparicoes(planeta):
    try:
        response = requests.get('https://swapi.co/api/planets/')
        planetas = response.json()
        for p in planetas['results']:
            if planeta['nome'].upper() == p['name'].upper():
                return len(p['films'])
        return 0
    except:
        return 0