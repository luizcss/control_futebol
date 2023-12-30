from repository import TimeRepository as repository
from repository import EstadioRepository as estadioRepository
from utils import MethodsUtils as methodsUtils


def getTimes():
    times = repository.getAll()
    return times


def getTimeById(id):
    time  = repository.getById(id)
    return time


def deleteTimeById(id):
    repository.delete(id)
    return True


def createTime(jsonTime):
    time = methodsUtils.parseJsonObejct(jsonTime)
    repository.save(time)
    return True


def updateTime(jsonTime, id):
    time = methodsUtils.parseJsonObejct(jsonTime)
    repository.update(time, id)
    return time
