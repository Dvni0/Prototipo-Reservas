import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from models.database import DB_PATH

class Reserva:
    def __init__(self, numero_sala, data_horario, conta_usuario=None):
        # Atributos privados
        self.__numero_sala = numero_sala
        self.__data_horario = data_horario
        self.__conta_usuario = conta_usuario

    def reserva_existe(self):
        conexao_bd = sqlite3.connect(DB_PATH)
        ponteiro_bd = conexao_bd.cursor()
        ponteiro_bd.execute('SELECT 1 FROM agendamentos WHERE numero_sala = ? AND data_horario = ?', (self.__numero_sala, self.__data_horario))
        existe = ponteiro_bd.fetchone() is not None
        conexao_bd.close()
        return existe

    def inserir_registro_reserva(self):
        conexao_bd = sqlite3.connect(DB_PATH)
        ponteiro_bd = conexao_bd.cursor()
        ponteiro_bd.execute('INSERT INTO agendamentos (conta_usuario, numero_sala, data_horario) VALUES (?, ?, ?)', (self.__conta_usuario, self.__numero_sala, self.__data_horario))
        conexao_bd.commit()
        conexao_bd.close()

    def notificar_usuario_email(self):
        servidor_envio = "smtp.gmail.com"
        conta_remetente = "sistema.reservas@fiap.com.br"

        pacote_mensagem = MIMEMultipart()
        pacote_mensagem['From'] = conta_remetente
        pacote_mensagem['To'] = self.__conta_usuario
        pacote_mensagem['Subject'] = f"Reservas FIAP - Confirmação da Sala ({self.__numero_sala})"

        conteudo_texto = f"Olá!\n\nO seu agendamento foi concluído com sucesso.\n\nDados do Agendamento:\n- Sala: {self.__numero_sala}\n- Data e Horário: {self.__data_horario}\n- Requerente: {self.__conta_usuario}\n\nCom os melhores cumprimentos,\nEquipe Reservas FIAP"
        pacote_mensagem.attach(MIMEText(conteudo_texto, 'plain'))

        try:
            print(f"[SERVIÇOS] Simulação de notificação enviada para: {self.__conta_usuario} | Espaço: {self.__numero_sala} | Dia: {self.__data_horario}")
            return True
        except Exception as erro_execucao:
            print(f"[SERVIÇOS] Falha na notificação: {erro_execucao}")
            return False