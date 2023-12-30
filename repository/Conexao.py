import sqlite3
import os

#https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html


def criarTabelas(nomeScript):
    conn = abrirConexao()
    cursor = conn.cursor()
    caminho_relativo = '..\\scripts\\'+nomeScript
    caminho_absoluto = os.path.join(os.path.dirname(__file__), caminho_relativo)
    try:
        with open(caminho_absoluto, 'r') as arquivo:
            conteudo = arquivo.read()
            cursor.execute(conteudo)
    except FileNotFoundError:
        print(f'O arquivo {caminho_absoluto} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    finally:
        print(f'Script executado {nomeScript}.')
    
    cursor.close()
    fecharConexao(conn)

def abrirConexao():
    conn = sqlite3.connect('futebol.db')
    return conn

def fecharConexao(conn):
    if conn:
        conn.close()
        print("Conexão fechada.")    


def start():
    for filename in os.listdir("./scripts"):
       print(filename)
       criarTabelas(filename)

