from flask import Flask, request, json
from service import TimeService as timeService
#https://pynative.com/python-convert-json-data-into-custom-python-object/


def criarTime():
    req_data = request.get_json()
    print(req_data)
    result = timeService.createTime(req_data)
    return json.dumps(result, default=lambda x: x.__dict__)


def obterTimes():
    times = timeService.getTimes()
    return json.dumps(times, default=lambda x: x.__dict__)


def obterTimePorId(id):
    time = timeService.getTimeById(id)
    return json.dumps(time, default=lambda x: x.__dict__)


def delete(id):
    time = timeService.deleteTimeById(id)
    return json.dumps(time, default=lambda x: x.__dict__)


def atualizar(id):
    req_data = request.get_json()
    time = timeService.updateTime(req_data, id)
    return json.dumps(time, default=lambda x: x.__dict__)




def registrarApi(app: Flask):
    app.add_url_rule("/time", "obterTimes", obterTimes,methods=["GET"] )
    app.add_url_rule("/time", "criarTime", criarTime, methods=["POST"])
    app.add_url_rule("/time/<id>", "obterTimePorId", obterTimePorId)
    app.add_url_rule("/time/<id>", "atualizarTime", atualizar, methods=["PUT"])
    app.add_url_rule("/time/<id>", "deleteTime", delete, methods=["DELETE"])