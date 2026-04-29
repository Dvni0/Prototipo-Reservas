import sqlite3
import os

class BancoDados:
    def __init__(self):
        # Atributos privados
        self.__base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.__db_path = os.path.join(self.__base_dir, 'data', 'dados_agendamentos_fiap.db')

    def obter_caminho(self):
        return self.__db_path

    def configurar_banco_dados(self):
        os.makedirs(os.path.dirname(self.__db_path), exist_ok=True)
        conexao_bd = sqlite3.connect(self.__db_path)
        ponteiro_bd = conexao_bd.cursor()
        
        ponteiro_bd.execute('''
            CREATE TABLE IF NOT EXISTS agendamentos (
                identificador INTEGER PRIMARY KEY AUTOINCREMENT,
                conta_usuario TEXT NOT NULL,
                numero_sala TEXT NOT NULL,
                data_horario TEXT NOT NULL,
                registro_tempo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        ponteiro_bd.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                identificador INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            )
        ''')
        conexao_bd.commit()
        conexao_bd.close()
    
# Isso só serve para não quebrar os outros arquivos instantaneamente
DB_PATH = BancoDados().obter_caminho()