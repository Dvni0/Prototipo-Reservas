import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import Image
import os
import datetime

# Importações dos módulos organizados
from auth.usuario import Usuario
from models.reservas import Reserva

COR_PRINCIPAL = "#ED145B"
COR_SECUNDARIA = "#C20D47"
COR_FUNDO = "#F2F2F2"

class ReservasFIAP(ctk.CTk):
    def mostrar_mensagem(self, texto, tipo="info"):
        cor = "#43B581" if tipo == "info" else "#ED145B"
        popup = ctk.CTkToplevel(self)
        popup.title("Mensagem")
        popup.geometry("320x140")
        popup.grab_set()
        popup.configure(fg_color="white")
        frame = ctk.CTkFrame(popup, fg_color=cor, corner_radius=16)
        frame.pack(expand=True, fill="both", padx=18, pady=18)
        label = ctk.CTkLabel(frame, text=texto, font=ctk.CTkFont(size=15, weight="bold"), text_color="white", fg_color=cor, wraplength=260)
        label.pack(pady=(18, 10), padx=10)
        botao = ctk.CTkButton(frame, text="OK", fg_color="white", text_color=cor, corner_radius=10, width=80, command=popup.destroy)
        botao.pack(pady=(0, 10))

    def __init__(self):
        super().__init__()
        self.title("Reservas FIAP")
        self.geometry("380x700")
        ctk.set_appearance_mode("Light")
        self.conta_ativa = None
        self.imagem_marca = None
        
        try:
            # Caminho atualizado para buscar a imagem na pasta data/
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            caminho_imagem = os.path.join(BASE_DIR, 'data', '1000018404.jpg')
            if os.path.exists(caminho_imagem):
                imagem_carregada = Image.open(caminho_imagem)
                self.imagem_marca = ctk.CTkImage(light_image=imagem_carregada, size=(250, 75))
        except Exception:
            pass

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.exibir_tela_acesso()

    
    def exibir_tela_acesso(self):
        self.apagar_elementos_tela()
        self.painel_acesso = ctk.CTkFrame(self, corner_radius=20, fg_color="white")
        self.painel_acesso.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.painel_acesso.grid_rowconfigure((0,7), weight=1)
        self.painel_acesso.grid_columnconfigure(0, weight=1)

        if self.imagem_marca:
            rotulo_marca = ctk.CTkLabel(self.painel_acesso, image=self.imagem_marca, text="")
            rotulo_marca.grid(row=1, column=0, pady=(30, 10), padx=10, sticky="ew")
        else:
            rotulo_marca = ctk.CTkLabel(self.painel_acesso, text="Reservas FIAP", font=ctk.CTkFont(size=32, weight="bold"), text_color=COR_PRINCIPAL)
            rotulo_marca.grid(row=1, column=0, pady=(30, 10), padx=10, sticky="ew")
           
        ctk.CTkLabel(self.painel_acesso, text="Coloque seu e-mail de aluno", font=ctk.CTkFont(size=16, weight="bold")).grid(row=2, column=0, pady=(0, 16), padx=10, sticky="ew")
        self.campo_identificacao = ctk.CTkEntry(self.painel_acesso, width=240, placeholder_text="Endereço (@fiap.com.br)", height=38)
        self.campo_identificacao.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="ew")
        self.campo_seguranca = ctk.CTkEntry(self.painel_acesso, width=240, placeholder_text="Chave de Segurança", show="*", height=38)
        self.campo_seguranca.grid(row=4, column=0, pady=(0, 16), padx=10, sticky="ew")

        ctk.CTkButton(self.painel_acesso, text="Realizar login", width=240, height=48, fg_color=COR_PRINCIPAL, hover_color=COR_SECUNDARIA, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=12, command=self.verificar_credenciais).grid(row=5, column=0, pady=(0, 10), padx=10, sticky="ew")
        ctk.CTkButton(self.painel_acesso, text="Cadastrar-se", width=240, height=48, fg_color="transparent", hover_color="#fce8ef", text_color=COR_PRINCIPAL, border_width=2, border_color=COR_PRINCIPAL, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=12, command=self.registrar_nova_conta).grid(row=6, column=0, pady=(0, 30), padx=10, sticky="ew")

    def verificar_credenciais(self):
        email = self.campo_identificacao.get().strip().lower()
        senha = self.campo_seguranca.get()

        if not email or not senha:
            messagebox.showwarning("Atenção", "Forneça os dados de acesso completos!")
            return

        if not email.endswith("@fiap.com.br"):
            messagebox.showerror("Falha na Autenticação", "Utilize uma credencial válida da instituição (@fiap.com.br).")
            return

        # Classe Usuario
        usuario = Usuario(email, senha)
        if usuario.validar_login():
            self.conta_ativa = email
            self.exibir_painel_salas()
        else:
            messagebox.showerror("Falha na Autenticação", "E-mail não cadastrado ou senha incorreta.")

    def registrar_nova_conta(self):
        email = self.campo_identificacao.get().strip().lower()
        senha = self.campo_seguranca.get()

        if not email or not senha:
            messagebox.showwarning("Atenção", "Preencha o e-mail e a senha que deseja cadastrar!")
            return

        if "@" not in email or not email.endswith("@fiap.com.br"):
            messagebox.showerror("Erro de Cadastro", "Utilize uma credencial válida da instituição (@fiap.com.br).")
            return

        #Classe usuario
        usuario = Usuario(email, senha)
        if usuario.registrar_usuario():
            self.mostrar_mensagem("Conta criada com sucesso!", tipo="info")
            self.campo_seguranca.delete(0, 'end')
        else:
            messagebox.showerror("Erro", "Este e-mail já possui cadastro ou domínio inválido.")

    def exibir_painel_salas(self):
        self.apagar_elementos_tela()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        area_conteudo = ctk.CTkFrame(self, corner_radius=0, fg_color=COR_FUNDO)
        area_conteudo.grid(row=0, column=0, columnspan=2, sticky="nsew")
        

        lista_espacos = [f"{p}{i:02d}" for p in range(2, 10) for i in range(1, 4)]
        area_rolagem = ctk.CTkScrollableFrame(area_conteudo, fg_color="transparent")
        area_rolagem.pack(fill="both", expand=True, padx=0, pady=0)

        for idx, sala in enumerate(lista_espacos):
            ctk.CTkButton(area_rolagem, text=f"Sala {sala}", width=220, height=54, fg_color="white", text_color="black", border_width=2, border_color=COR_PRINCIPAL, command=lambda s=sala: self.mostrar_seletor_data(s)).grid(row=idx, column=0, pady=7, padx=70)

    def mostrar_seletor_data(self, espaco_alvo):
        self.apagar_elementos_tela()
        area_conteudo = ctk.CTkFrame(self, corner_radius=0, fg_color=COR_FUNDO)
        area_conteudo.pack(fill="both", expand=True)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        cal = Calendar(area_conteudo, selectmode='day', background=COR_PRINCIPAL)
        cal.pack(pady=20)

        horarios = [f"{h:02d}:00" for h in range(7, 23)]
        var_h = tk.StringVar(value=horarios[0])
        tk.OptionMenu(area_conteudo, var_h, *horarios).pack()

        def confirmar():
            dt_hr = f"{cal.get_date()} {var_h.get()}"
            # Utilizando a Classe Reserva (POO)
            reserva = Reserva(espaco_alvo, dt_hr)
            if reserva.reserva_existe():
                self.mostrar_mensagem("Sala ocupada!", tipo="erro")
            else:
                self.processar_agendamento(espaco_alvo, cal.get_date(), var_h.get())

        ctk.CTkButton(area_conteudo, text="Confirmar", command=confirmar, fg_color=COR_PRINCIPAL).pack(pady=20)

    def processar_agendamento(self, sala, data, hora):
        data_hora = f"{data} {hora}"
        reserva = Reserva(sala, data_hora, self.conta_ativa)
        reserva.inserir_registro_reserva()
        reserva.notificar_usuario_email()
        self.exibir_painel_salas()
        self.mostrar_mensagem(f"Sala {sala} reservada!", tipo="info")
        

    def apagar_elementos_tela(self):
        for child in self.winfo_children(): child.destroy()
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)