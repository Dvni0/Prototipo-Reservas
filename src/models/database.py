import sqlite3
import os

# Define o caminho absoluto para a pasta data/ (evita erros ao rodar o arquivo de lugares diferentes)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'dados_agendamentos_fiap.db')

def configurar_banco_dados():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conexao_bd = sqlite3.connect(DB_PATH)
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