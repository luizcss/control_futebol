from repository import Conexao as conexao
import sqlite3
from entity.Time import Time

# https://www.freecodecamp.org/news/typeerror-module-object-is-not-callable-python-error-solved/

SCRIPT_INSERT = "INSERT INTO TIME (NOME, ID_ESTADIO, SIGLA, DATA_FUNDACAO) VALUES(?, ?, ?, ?);"
SCRIPT_UPDATE = "UPDATE TIME SET NOME=?, ID_ESTADIO=?, SIGLA=?, DATA_FUNDACAO=? WHERE ID = filtro;"
SCRIPT_SELECT_ALL = "SELECT  TM.ID,  TM.NOME,  TM.ID_ESTADIO, TM.SIGLA, TM.DATA_FUNDACAO, EST.NOME FROM TIME TM LEFT JOIN ESTADIO EST ON TM.ID_ESTADIO = EST.ID;"
SCRIPT_SELECT_BY_ID = "SELECT  TM.ID,  TM.NOME,  TM.ID_ESTADIO, TM.SIGLA, TM.DATA_FUNDACAO, EST.NOME FROM TIME TM LEFT JOIN ESTADIO EST ON TM.ID_ESTADIO = EST.ID WHERE TM.ID =?;"
SCRIPT_DELETE = "DELETE FROM TIME WHERE ID = ? ;"


def save(time: Time):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_INSERT, time)
        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Falha ao criar o time.", error)
    finally:
        conexao.fecharConexao(conn)


def update(time: Time, id: int):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        script = SCRIPT_UPDATE.replace("filtro", id)
        print(script)
        cursor.execute(script, time)
        conn.commit()
        cursor.close()
        print(f'Registro id {id} atualizado com sucesso')
    except sqlite3.Error as error:
        print(f'Falha ao atualizar o time {id}.', error)
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
        print(f'Falha ao deletar o time {id}.', error)
    finally:
        conexao.fecharConexao(conn)


def saveAll(times):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.executemany(SCRIPT_INSERT, times)
        conn.commit()
    except sqlite3.Error as error:
        print(f'Falha ao criar os times em lote.', error)
    finally:
        conexao.fecharConexao(conn)


def getById(id):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_SELECT_BY_ID, id)

        time = None
        for linha in cursor.fetchall():
            print(linha)
            time = Time(linha[0], linha[1], linha[2],
                        linha[3], linha[4], linha[5])
    except sqlite3.Error as error:
        print(f'Falha na consulta do time {id}', error)
    finally:
        conexao.fecharConexao(conn)
    return time


def getAll():
    times = []
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_SELECT_ALL)
        for linha in cursor.fetchall():
            print(linha)
            times.append(
                Time(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5]))
        cursor.close()
    except sqlite3.Error as error:
        print("Falha na consulta dos times", error)
    finally:
        conexao.fecharConexao(conn)
    return times
