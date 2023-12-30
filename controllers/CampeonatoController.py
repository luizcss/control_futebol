from flask import Flask, request, json
from service import CampeonatoService as campeonatoService


def criarCampeonato():
    req_data = request.get_json()
    print(req_data)
    result = campeonatoService.createCampeonato(req_data)
    return json.dumps(result, default=lambda x: x.__dict__)


def obterCampeonatos():
    campeonatos = campeonatoService.getCampeonatos()
    return json.dumps(campeonatos, default=lambda x: x.__dict__)


def obterCampeonatoPorId(id):
    campeonato = campeonatoService.getCampeonatoById(id)
    return json.dumps(campeonato, default=lambda x: x.__dict__)


def delete(id):
    campeonato = campeonatoService.deleteCampeonatoById(id)
    return json.dumps(campeonato, default=lambda x: x.__dict__)


def atualizar(id):
    req_data = request.get_json()
    campeonato = campeonatoService.updateCampeonato(req_data, id)
    return json.dumps(campeonato, default=lambda x: x.__dict__)


def registrarApi(app: Flask):
    app.add_url_rule("/campeonato", "obterCampeonatos", obterCampeonatos) 
    app.add_url_rule("/campeonato", "criarCampeonato", criarCampeonato) 
    app.add_url_rule("/campeonato/<id>", "obterCampeonatoPorId", obterCampeonatoPorId) 
    app.add_url_rule("/campeonato/<id>", "atualizarCampeonato", atualizar) 
    app.add_url_rule("/campeonato/<id>", "deleteCampeonato", delete) 
