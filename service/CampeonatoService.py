from repository import CampeonatoRepository as repository
from utils import MethodsUtils as methodsUtils


def getCampeonatos():
    return repository.getAll()


def getCampeonatoById(id):
    return repository.getById(id)


def deleteCampeonatoById(id):
    repository.delete(id)
    return True


def createCampeonato(jsonCampeonato):
    campeonato = methodsUtils.parseJsonObejct(jsonCampeonato)
    repository.save(campeonato)
    return True


def updateCampeonato(jsonCampeonato, id):
    campeonato = methodsUtils.parseJsonObejct(jsonCampeonato)
    repository.update(campeonato, id)
    return campeonato
