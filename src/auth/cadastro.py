import sqlite3
from models.database import DB_PATH

def registrar_usuario(email, senha):
    conexao_bd = sqlite3.connect(DB_PATH)
    ponteiro_bd = conexao_bd.cursor()
    try:
        ponteiro_bd.execute('INSERT INTO usuarios (email, senha) VALUES (?, ?)', (email, senha))
        conexao_bd.commit()
        sucesso = True
    except sqlite3.IntegrityError:
        sucesso = False 
    finally:
        conexao_bd.close()
    return sucesso