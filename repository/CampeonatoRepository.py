from repository import Conexao as conexao
import sqlite3
from entity.Campeonato import Campeonato

# https://www.freecodecamp.org/news/typeerror-module-object-is-not-callable-python-error-solved/

SCRIPT_INSERT = "INSERT INTO CAMPEONATO (CODIGO, DESCRICAO, DATA_INICIO, DATA_TERMINO) VALUES(?, ?, ?, ?);"
SCRIPT_UPDATE = "UPDATE CAMPEONATO SET CODIGO=?, DESCRICAO=?, DATA_INICIO=?, DATA_TERMINO=? WHERE ID = filtro;"
SCRIPT_SELECT_ALL = "SELECT ID, CODIGO,  NOME, DESCRICAO, DATA_INICIO, DATA_TERMINO FROM CAMPEONATO "
SCRIPT_SELECT_BY_ID = "SELECT ID, CODIGO,  NOME, DESCRICAO, DATA_INICIO, DATA_TERMINO FROM CAMPEONATO WHERE ID =?;"
SCRIPT_DELETE = "DELETE FROM CAMPEONATO WHERE ID = ? ;"


def save(campeonato: Campeonato):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_INSERT, campeonato)
        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Falha ao criar o campeonato.", error)
    finally:
        conexao.fecharConexao(conn)


def update(campeonato: Campeonato, id: int):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        script = SCRIPT_UPDATE.replace("filtro", id)
        print(script)
        cursor.execute(script, campeonato)
        conn.commit()
        cursor.close()
        print(f'Registro id {id} atualizado com sucesso')
    except sqlite3.Error as error:
        print(f'Falha ao atualizar o campeonato {id}.', error)
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
        print(f'Falha ao deletar o campeonato {id}.', error)
    finally:
        conexao.fecharConexao(conn)


def saveAll(campeonatos):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.executemany(SCRIPT_INSERT, campeonatos)
        conn.commit()
    except sqlite3.Error as error:
        print(f'Falha ao criar os campeonatos em lote.', error)
    finally:
        conexao.fecharConexao(conn)


def getById(id):
    try:
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_SELECT_BY_ID, id)

        campeonato = None
        for linha in cursor.fetchall():
            print(linha)
            campeonato = Campeonato(linha[0], linha[1], linha[2], linha[3], linha[4])
    except sqlite3.Error as error:
        print(f'Falha na consulta do campeonato {id}', error)
    finally:
        conexao.fecharConexao(conn)
    return campeonato


def getAll():
    try:
        campeonatos = []
        conn = conexao.abrirConexao()
        cursor = conn.cursor()
        cursor.execute(SCRIPT_SELECT_ALL)
        for linha in cursor.fetchall():
            print(linha)
            campeonatos.append(Campeonato(linha[0], linha[1], linha[2], linha[3], linha[4]))
        cursor.close()
    except sqlite3.Error as error:
        print("Falha na consulta dos campeonatos", error)
    finally:
        conexao.fecharConexao(conn)
    return campeonatos
