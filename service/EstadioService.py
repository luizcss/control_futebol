from repository import EstadioRepository as repository
from utils import MethodsUtils as methodsUtils


def getEstadios():
    return repository.getAll()


def getEstadioById(id):
    return repository.getById(id)


def deleteEstadioById(id):
    repository.delete(id)
    return True


def createEstadio(jsonEstadio):
    estadio = methodsUtils.parseJsonObejct(jsonEstadio)
    repository.save(estadio)
    return True


def updateEstadio(jsonEstadio, id):
    estadio = methodsUtils.parseJsonObejct(jsonEstadio)
    repository.update(estadio, id)
    return estadio
