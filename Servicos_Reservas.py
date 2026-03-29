def reserva_existe(numero_sala, data_horario):
    conexao_bd = sqlite3.connect('dados_agendamentos_fiap.db')
    ponteiro_bd = conexao_bd.cursor()
    ponteiro_bd.execute('SELECT 1 FROM agendamentos WHERE numero_sala = ? AND data_horario = ?', (numero_sala, data_horario))
    existe = ponteiro_bd.fetchone() is not None
    conexao_bd.close()
    return existe
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def configurar_banco_dados():
    conexao_bd = sqlite3.connect('dados_agendamentos_fiap.db')
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
    conexao_bd.commit()
    conexao_bd.close()

def inserir_registro_reserva(conta_usuario, numero_sala, dia_escolhido):
    conexao_bd = sqlite3.connect('dados_agendamentos_fiap.db')
    ponteiro_bd = conexao_bd.cursor()
    ponteiro_bd.execute('INSERT INTO agendamentos (conta_usuario, numero_sala, data_horario) VALUES (?, ?, ?)', (conta_usuario, numero_sala, dia_escolhido))
    conexao_bd.commit()
    conexao_bd.close()

def notificar_usuario_email(endereco_email, numero_sala, dia_escolhido):
    servidor_envio = "smtp.gmail.com"
    porta_acesso = 587
    conta_remetente = "sistema.reservas@fiap.com.br"
    chave_acesso = "sua_palavra_passe_de_aplicacao"

    pacote_mensagem = MIMEMultipart()
    pacote_mensagem['From'] = conta_remetente
    pacote_mensagem['To'] = endereco_email
    pacote_mensagem['Subject'] = f"Reservas FIAP - Confirmação da Sala ({numero_sala})"

    conteudo_texto = f"Olá!\n\nO seu agendamento foi concluído com sucesso.\n\nDados do Agendamento:\n- Sala: {numero_sala}\n- Data e Horário: {dia_escolhido}\n- Requerente: {endereco_email}\n\nCom os melhores cumprimentos,\nEquipe Reservas FIAP"
    pacote_mensagem.attach(MIMEText(conteudo_texto, 'plain'))

    try:
        print(f"[SERVIÇOS] Simulação de notificação enviada para: {endereco_email} | Espaço: {numero_sala} | Dia: {dia_escolhido}")
        return True
    except Exception as erro_execucao:
        print(f"[SERVIÇOS] Falha na notificação: {erro_execucao}")
        return False