import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import Image
import os
import datetime

# Importações dos módulos organizados
from auth.login import validar_login
from auth.cadastro import registrar_usuario
from models.reservas import reserva_existe, inserir_registro_reserva, notificar_usuario_email

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
        # Ajustado para (0,7) para acomodar o botão extra de cadastro
        self.painel_acesso.grid_rowconfigure((0,7), weight=1)
        self.painel_acesso.grid_columnconfigure(0, weight=1)

        if self.imagem_marca:
            rotulo_marca = ctk.CTkLabel(self.painel_acesso, image=self.imagem_marca, text="")
            rotulo_marca.grid(row=1, column=0, pady=(30, 10), padx=10, sticky="ew")
        else:
            rotulo_marca = ctk.CTkLabel(self.painel_acesso, text="Reservas FIAP", font=ctk.CTkFont(size=32, weight="bold"), text_color=COR_PRINCIPAL)
            rotulo_marca.grid(row=1, column=0, pady=(30, 10), padx=10, sticky="ew")

        rotulo_boas_vindas = ctk.CTkLabel(self.painel_acesso, text="Coloque seu e-mail de aluno", font=ctk.CTkFont(size=16, weight="bold"))
        rotulo_boas_vindas.grid(row=2, column=0, pady=(0, 16), padx=10, sticky="ew")

        self.campo_identificacao = ctk.CTkEntry(self.painel_acesso, width=240, placeholder_text="Endereço (@fiap.com.br)", height=38)
        self.campo_identificacao.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="ew")

        self.campo_seguranca = ctk.CTkEntry(self.painel_acesso, width=240, placeholder_text="Chave de Segurança", show="*", height=38)
        self.campo_seguranca.grid(row=4, column=0, pady=(0, 16), padx=10, sticky="ew")

        # Botão de Autenticação atualizado
        botao_autenticar = ctk.CTkButton(self.painel_acesso, text="Realizar login", width=240, height=48, 
                         fg_color=COR_PRINCIPAL, hover_color=COR_SECUNDARIA, font=ctk.CTkFont(size=16, weight="bold"),
                         corner_radius=12, command=self.verificar_credenciais)
        botao_autenticar.grid(row=5, column=0, pady=(0, 10), padx=10, sticky="ew")

        # NOVO: Botão de cadastro
        botao_cadastrar = ctk.CTkButton(self.painel_acesso, text="Cadastrar-se", width=240, height=48, 
                         fg_color="transparent", hover_color="#fce8ef", text_color=COR_PRINCIPAL, 
                         border_width=2, border_color=COR_PRINCIPAL, font=ctk.CTkFont(size=16, weight="bold"),
                         corner_radius=12, command=self.registrar_nova_conta)
        botao_cadastrar.grid(row=6, column=0, pady=(0, 30), padx=10, sticky="ew")

    def verificar_credenciais(self):
        texto_identificacao = self.campo_identificacao.get().strip().lower()
        texto_seguranca = self.campo_seguranca.get()

        if not texto_identificacao or not texto_seguranca:
            messagebox.showwarning("Atenção", "Forneça os dados de acesso completos!")
            return

        # Verifica se o e-mail pertence à FIAP
        if not texto_identificacao.endswith("@fiap.com.br"):
            messagebox.showerror("Falha na Autenticação", "Utilize uma credencial válida da instituição (@fiap.com.br).")
            return

        # Verifica no banco de dados se a senha bate com o e-mail
        if validar_login(texto_identificacao, texto_seguranca):
            self.conta_ativa = texto_identificacao
            self.exibir_painel_salas()
        else:
            messagebox.showerror("Falha na Autenticação", "E-mail não cadastrado ou senha incorreta.")

    # NOVA FUNÇÃO: Lida com o cadastro do usuário
    def registrar_nova_conta(self):
        texto_identificacao = self.campo_identificacao.get().strip().lower()
        texto_seguranca = self.campo_seguranca.get()

        if not texto_identificacao or not texto_seguranca:
            messagebox.showwarning("Atenção", "Preencha o e-mail e a senha que deseja cadastrar!")
            return

        if not texto_identificacao.endswith("@fiap.com.br"):
            messagebox.showerror("Erro no Cadastro", "Apenas e-mails institucionais (@fiap.com.br) são permitidos.")
            return

        # Tenta registrar no banco
        sucesso = registrar_usuario(texto_identificacao, texto_seguranca)
        
        if sucesso:
            self.mostrar_mensagem("Conta criada com sucesso! Você já pode fazer o login.", tipo="info")
            self.campo_seguranca.delete(0, 'end') # Limpa a senha por segurança
        else:
            messagebox.showerror("Erro no Cadastro", "Este e-mail já possui cadastro no sistema.")

    def exibir_painel_salas(self):
        self.apagar_elementos_tela()

        # Mobile-first: barra superior simples
        barra_superior = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="white")
        barra_superior.grid(row=0, column=0, columnspan=2, sticky="ew")
        barra_superior.grid_columnconfigure(0, weight=1)
        barra_superior.grid_columnconfigure(1, weight=1)
        if self.imagem_marca:
            marca_topo = ctk.CTkLabel(barra_superior, image=self.imagem_marca, text="")
            marca_topo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        else:
            marca_topo = ctk.CTkLabel(barra_superior, text="FIAP", font=ctk.CTkFont(size=22, weight="bold"), text_color=COR_PRINCIPAL)
            marca_topo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        indicador_conta = ctk.CTkLabel(barra_superior, text=f"{self.conta_ativa}", font=ctk.CTkFont(size=12))
        indicador_conta.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        area_conteudo = ctk.CTkFrame(self, corner_radius=0, fg_color=COR_FUNDO)
        area_conteudo.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        cabecalho_conteudo = ctk.CTkLabel(area_conteudo, text="Escolha a Sala Pretendida", font=ctk.CTkFont(size=18, weight="bold"))
        cabecalho_conteudo.pack(pady=(18, 10), padx=10, anchor="center")

        area_rolagem = ctk.CTkScrollableFrame(area_conteudo, fg_color="transparent")
        area_rolagem.pack(fill="both", expand=True, padx=0, pady=0)

        lista_espacos = []
        for piso in range(2, 10):
            for identificador in range(1, 4):
                lista_espacos.append(f"{piso}0{identificador}")

        # Centralizar os botões de sala
        for idx, espaco_atual in enumerate(lista_espacos):
            frame_central = ctk.CTkFrame(area_rolagem, fg_color="transparent")
            frame_central.grid(row=idx, column=0, sticky="ew")
            frame_central.grid_columnconfigure(0, weight=1)
            botao_espaco = ctk.CTkButton(frame_central, text=f"Sala {espaco_atual}", width=220, height=54,
                                         font=ctk.CTkFont(size=15, weight="bold"),
                                         fg_color="white", text_color="black", hover_color="#fce8ef",
                                         border_width=2, border_color=COR_PRINCIPAL,
                                         corner_radius=12,
                                         command=lambda e=espaco_atual: self.mostrar_seletor_data(e))
            botao_espaco.grid(row=0, column=0, padx=0, pady=7)
            # Adiciona espaçamento lateral para centralizar
            area_rolagem.grid_columnconfigure(0, weight=1)

        botao_encerrar = ctk.CTkButton(area_conteudo, text="Terminar Sessão", fg_color=COR_PRINCIPAL, hover_color=COR_SECUNDARIA,
                                       text_color="white", font=ctk.CTkFont(size=14, weight="bold"), corner_radius=12,
                                       command=self.exibir_tela_acesso)
        botao_encerrar.pack(pady=(10, 16), padx=10, fill="x")

    def mostrar_seletor_data(self, espaco_alvo):
        self.apagar_elementos_tela()
        # Barra superior
        barra_superior = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="white")
        barra_superior.grid(row=0, column=0, columnspan=2, sticky="ew")
        barra_superior.grid_columnconfigure(0, weight=1)
        barra_superior.grid_columnconfigure(1, weight=1)
        if self.imagem_marca:
            marca_topo = ctk.CTkLabel(barra_superior, image=self.imagem_marca, text="")
            marca_topo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        else:
            marca_topo = ctk.CTkLabel(barra_superior, text="FIAP", font=ctk.CTkFont(size=22, weight="bold"), text_color=COR_PRINCIPAL)
            marca_topo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        indicador_conta = ctk.CTkLabel(barra_superior, text=f"{self.conta_ativa}", font=ctk.CTkFont(size=12))
        indicador_conta.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        area_conteudo = ctk.CTkFrame(self, corner_radius=0, fg_color=COR_FUNDO)
        area_conteudo.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        cabecalho_conteudo = ctk.CTkLabel(area_conteudo, text=f"Agendar Sala {espaco_alvo}", font=ctk.CTkFont(size=18, weight="bold"))
        cabecalho_conteudo.pack(pady=(18, 10), padx=10, anchor="center")

        # Calendário
        data_atual = datetime.date.today()
        frame_calendario = ctk.CTkFrame(area_conteudo, fg_color="white")
        frame_calendario.pack(pady=10)
        componente_calendario = Calendar(frame_calendario, selectmode='day', 
                                         year=data_atual.year, month=data_atual.month, day=data_atual.day,
                                         background=COR_PRINCIPAL, bordercolor=COR_PRINCIPAL, 
                                         headersbackground='white', normalbackground='white', foreground='white', 
                                         normalforeground='black', headersforeground=COR_PRINCIPAL)
        componente_calendario.pack()

        # Seleção de horário
        label_horario = ctk.CTkLabel(area_conteudo, text="Horário da reserva:", font=ctk.CTkFont(size=14), text_color=COR_PRINCIPAL)
        label_horario.pack(pady=(10, 2))
        horarios = [f"{h:02d}:00" for h in range(7, 23)]
        var_horario = tk.StringVar(value=horarios[0])
        combo_horario = tk.OptionMenu(area_conteudo, var_horario, *horarios)
        combo_horario.config(font=("Arial", 12), width=10)
        combo_horario.pack(pady=(0, 10))

        def registrar_escolha():
            dia_marcado = componente_calendario.get_date()
            horario_marcado = var_horario.get()
            data_hora = f"{dia_marcado} {horario_marcado}"
            if reserva_existe(espaco_alvo, data_hora):
                self.mostrar_mensagem(f"A sala {espaco_alvo} já está reservada para {data_hora}.", tipo="erro")
                return
            self.processar_agendamento(espaco_alvo, dia_marcado, horario_marcado, None)

        botao_concluir = ctk.CTkButton(area_conteudo, text="Concluir Agendamento", font=ctk.CTkFont(size=14, weight="bold"),
                                       fg_color=COR_PRINCIPAL, hover_color=COR_SECUNDARIA, text_color="white",
                                       corner_radius=12, command=registrar_escolha)
        botao_concluir.pack(pady=15, padx=10, fill="x")

        botao_voltar = ctk.CTkButton(area_conteudo, text="Voltar", font=ctk.CTkFont(size=12),
                                     fg_color=COR_SECUNDARIA, hover_color=COR_PRINCIPAL, text_color="white",
                                     corner_radius=12, command=self.exibir_painel_salas)
        botao_voltar.pack(pady=(0, 10), padx=10, fill="x")

    def processar_agendamento(self, espaco_alvo, dia_marcado, horario_marcado, janela_referencia):
        data_hora = f"{dia_marcado} {horario_marcado}"
        inserir_registro_reserva(self.conta_ativa, espaco_alvo, data_hora)
        if janela_referencia:
            janela_referencia.destroy()
        self.mostrar_mensagem(f"Agendamento da Sala {espaco_alvo} para {data_hora} efetuado!", tipo="info")
        notificar_usuario_email(self.conta_ativa, espaco_alvo, data_hora)

    def apagar_elementos_tela(self):
        for elemento_visual in self.winfo_children():
            elemento_visual.destroy()

if __name__ == "__main__":
    # Garante que o banco e as tabelas estejam criados ao abrir o sistema
    configurar_banco_dados()
    sistema_principal = ReservasFIAP()
    sistema_principal.mainloop()