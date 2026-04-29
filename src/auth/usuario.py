import sqlite3
from models.database import DB_PATH

class Usuario:
    def __init__(self, email, senha):
        # atributo é privado
        self.__email = email
        self.__senha = senha

    def registrar_usuario(self):
        conexao_bd = sqlite3.connect(DB_PATH)
        ponteiro_bd = conexao_bd.cursor()
        try:
            
            ponteiro_bd.execute('INSERT INTO usuarios (email, senha) VALUES (?, ?)', (self.__email, self.__senha))
            conexao_bd.commit()
            sucesso = True
        except sqlite3.IntegrityError:
            sucesso = False 
        finally:
            conexao_bd.close()
        return sucesso

    def validar_login(self):
        conexao_bd = sqlite3.connect(DB_PATH)
        ponteiro_bd = conexao_bd.cursor()
        
        ponteiro_bd.execute('SELECT 1 FROM usuarios WHERE email = ? AND senha = ?', (self.__email, self.__senha))
        existe = ponteiro_bd.fetchone() is not None
        conexao_bd.close()
        return existe