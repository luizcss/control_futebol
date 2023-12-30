from flask import Flask, request, json
from service import EstadioService as estadioService
#https://pynative.com/python-convert-json-data-into-custom-python-object/


def criarEstadio():
    req_data = request.get_json()
    print(req_data)
    result = estadioService.createEstadio(req_data)
    return json.dumps(result, default=lambda x: x.__dict__)


def obterEstadios():
    estadios = estadioService.getEstadios()
    return json.dumps(estadios, default=lambda x: x.__dict__)


def obterEstadioPorId(id):
    estadio = estadioService.getEstadioById(id)
    return json.dumps(estadio, default=lambda x: x.__dict__)


def delete(id):
    estadio = estadioService.deleteEstadioById(id)
    return json.dumps(estadio, default=lambda x: x.__dict__)


def atualizar(id):
    req_data = request.get_json()
    estadio = estadioService.updateEstadio(req_data, id)
    return json.dumps(estadio, default=lambda x: x.__dict__)



def registrarApi(app: Flask):
    app.add_url_rule("/estadio", "obterEstadios", obterEstadios)
    app.add_url_rule("/estadio", "criarEstadio", criarEstadio, methods=["POST"])
    app.add_url_rule("/estadio/<id>", "obterEstadioPorId", obterEstadioPorId)
    app.add_url_rule("/estadio/<id>", "atualizarEstadio", atualizar)
    app.add_url_rule("/estadio/<id>", "deleteEstadio", delete)
