from repository import Conexao as conexao
from collections import namedtuple
import json
from flask import Flask
#https://medium.com/@hedgarbezerra35/api-rest-com-flask-autenticacao-25d99b8679b6
#//ADICIONAR autenticação

from controllers import EstadioController as estadioController
from controllers import CampeonatoController as campeonatoController
from controllers import TimeController as timeController

def parseJsonObejct(jsonEntrada):
    jsonAux = json.dumps(jsonEntrada)
    object = json.loads(jsonAux, object_hook=customObejctDecoder)
    return object


def customObejctDecoder(estruturaDict):
    return namedtuple('X', estruturaDict.keys())(*estruturaDict.values())


def initComponentes(app: Flask):
    initRotas(app)
    conexao.start()

def initRotas(app: Flask):
    estadioController.registrarApi(app)
    campeonatoController.registrarApi(app)    
    timeController.registrarApi(app)
    

