from repository import Conexao as conexao
import sqlite3
from entity.Estadio import Estadio

# https://www.freecodecamp.org/news/typeerror-module-object-is-not-callable-python-error-solved/

SCRIPT_INSERT = "INSERT INTO ESTADIO (NOME, CIDADE, DATA_FUNDACAO) VALUES(?, ?, ?);"
SCRIPT_UPDATE = "UPDATE ESTADIO SET NOME=?, CIDADE=?, DATA_FUNDACAO=? WHERE ID = filtro;"
SCRIPT_SELECT_ALL = "SELECT ID, NOME, CIDADE, DATA_FUNDACAO FROM ESTADIO"
SCRIPT_SELECT_BY_ID = "SELECT ID, NOME, CIDADE, DATA_FUNDACAO FROM ESTADIO WHERE ID =?;"
SCRIPT_SELECT_BY_ID_TIME = "SELECT EST.ID, EST.NOME, EST.CIDADE, EST.DATA_FUNDACAO FROM ESTADIO EST INNER JOIN TIME TIM ON EST.ID = TIM.ID_ESTADIO WHERE TIM.ID =?;"
SCRIPT_DELETE = "DELETE FROM ESTADIO WHERE ID = ? ;"


def save(estadio: Estadio):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_INSERT, estadio)
        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Falha ao criar o estadio.", error)
    finally:
        conexao.fecharConexao(conn)


def update(estadio: Estadio, id: int):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        script = SCRIPT_UPDATE.replace("filtro", id)
        print(script)
        cursor.execute(script, estadio)
        conn.commit()
        cursor.close()
        print(f'Registro id {id} atualizado com sucesso')
    except sqlite3.Error as error:
        print(f'Falha ao atualizar o estadio {id}.', error)
    finally:
        conexao.fecharConexao(conn)


def delete(id):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_DELETE, id)
        conn.commit()
        cursor.close()
        print(f'Registro id {id} deletado com sucesso')
    except sqlite3.Error as error:
        print(f'Falha ao deletar o estadio {id}.', error)
    finally:
        conexao.fecharConexao(conn)


def saveAll(estadios):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.executemany(SCRIPT_INSERT, estadios)
        conn.commit()
    except sqlite3.Error as error:
        print(f'Falha ao criar os estadios em lote.', error)
    finally:
        conexao.fecharConexao(conn)


def getById(id):
    estadio = None
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_SELECT_BY_ID, id)
       
        for linha in cursor.fetchall():
            print(linha)
            estadio = Estadio(linha[0], linha[1], linha[2], linha[3])
    except sqlite3.Error as error:
        print(f'Falha na consulta do estadio {id}', error)
    finally:
        conexao.fecharConexao(conn)

    return estadio

def getByIdTime(id):
    estadio = None
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_SELECT_BY_ID_TIME, id)

        for linha in cursor.fetchall():
            print(linha)
            estadio = Estadio(linha[0], linha[1], linha[2], linha[3])
    except sqlite3.Error as error:
        print(f'Falha na consulta do estadio {id}', error)
    finally:
        conexao.fecharConexao(conn)

    return estadio


def getAll():
    estadios = []
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_SELECT_ALL)
        for linha in cursor.fetchall():
            print(linha)
            estadios.append(Estadio(linha[0], linha[1], linha[2], linha[3]))
        cursor.close()
    except sqlite3.Error as error:
        print("Falha na consulta dos estadios", error)
    finally:
        conexao.fecharConexao(conn)
    return estadios
