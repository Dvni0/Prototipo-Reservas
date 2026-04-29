import sqlite3
from models.database import DB_PATH

def validar_login(email, senha):
    conexao_bd = sqlite3.connect(DB_PATH)
    ponteiro_bd = conexao_bd.cursor()
    ponteiro_bd.execute('SELECT 1 FROM usuarios WHERE email = ? AND senha = ?', (email, senha))
    existe = ponteiro_bd.fetchone() is not None
    conexao_bd.close()
    return existe