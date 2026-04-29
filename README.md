# **🏫 Sistema de Reservas FIAP**

### **Aplicativo Desktop para Gestão de Espaços Acadêmicos**

O sistema **Reservas FIAP** é uma solução desktop desenvolvida para otimizar o agendamento de salas de aula e espaços acadêmicos. Com foco em usabilidade e uma abordagem *Mobile-first* adaptada para o desktop, o aplicativo centraliza a gestão de infraestrutura, eliminando conflitos de horários e automatizando a confirmação via e-mail.

## **👥 Integrantes - Grupo 1º Checkpoint**

* **Guilherme Torres da Silva**
* **Luis Fernando Picarelli Gonçalves Guariglia**
* **Vinícius Barros Souza**
* **Alexandre Caus Haddade**
* **Mário Secundino Santana Lopes Portella**

## **✨ Funcionalidades**

* 🔐 **Autenticação Segura:** Sistema de cadastro e login com senhas validadas em banco de dados, restrito a e-mails institucionais (@fiap.com.br).
* 📅 **Agendamento Visual:** Calendário interativo para seleção de datas e horários (07:00 às 22:00).  
* 🏢 **Grade de Salas:** Gestão de espaços do 2º ao 9º andar (salas 201 a 903).  
* 🛡️ **Prevenção de Conflitos:** Validação em tempo real para evitar reservas duplicadas no mesmo horário/sala.  
* 📧 **Notificação Automática:** Envio de e-mail de confirmação via protocolo SMTP.  
* 🎨 **Interface Moderna:** UI construída com CustomTkinter seguindo a identidade visual da FIAP.

## **🛠️ Tecnologias e Arquitetura**

O projeto foi refatorado para seguir uma arquitetura modular baseada na separação de responsabilidades (MVC/Services):

* **Linguagem:** Python 3.10+  
* **Interface Gráfica (Views):** CustomTkinter, tkcalendar, Pillow.  
* **Banco de Dados (Models):** SQLite3 (Persistência local).  
* **Comunicação:** smtplib (Protocolo de e-mail).

## **🚀 Como Executar o Projeto**

### **1. Preparar o Sistema (Para usuários Linux/Mint)**

Certifique-se de que o sistema possui os pacotes base do Tkinter e do venv:

```bash
sudo apt update
sudo apt install python3-tk python3-venv -y
```

### **2. Criar e Ativar o Ambiente Virtual**

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar no Linux/Mac
source venv/bin/activate

# Ativar no Windows (se aplicável)
venv\Scripts\activate
```

### **3. Instalar Dependências**

Em vez de instalar manualmente, utilize o arquivo de configuração para garantir as versões corretas:

```bash
pip install -r requirements.txt
```

### **4. Rodar a Aplicação**

A partir da raiz do projeto, execute o arquivo principal:

```bash
python3 src/main.py
```

*(Nota: O banco de dados SQLite e as tabelas necessárias serão criados automaticamente na pasta `src/data/` durante a primeira execução).*

## **📂 Estrutura do Projeto**

```text
/
├── README.md
├── requirements.txt
├── docs/
└── src/
    ├── main.py             # Arquivo inicializador do sistema
    ├── auth/               # Módulos de autenticação (cadastro e login)
    │   ├── cadastro.py
    │   └── login.py
    ├── models/             # Regras de negócio e conexão com o banco
    │   ├── database.py
    │   └── reservas.py
    ├── views/              # Interface gráfica (Front-end)
    │   └── interface.py
    └── data/               # Arquivos estáticos e banco local
        ├── 1000018404.jpg
        └── dados_agendamentos_fiap.db
```

## **🗄️ Estrutura do Banco de Dados**

### **Tabela: `usuarios`**

| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| identificador | INTEGER | Chave Primária (Auto-incremento). |
| email | TEXT | E-mail do solicitante (Único). |
| senha | TEXT | Senha cadastrada para login. |

### **Tabela: `agendamentos`**

| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| identificador | INTEGER | Chave Primária (Auto-incremento). |
| conta_usuario | TEXT | E-mail do usuário que fez a reserva. |
| numero_sala | TEXT | Número da sala reservada. |
| data_horario | TEXT | Concatenação de Data e Hora da reserva. |
| registro_tempo | TIMESTAMP | Data/hora de criação do registro. |

## **📝 Licença**

Este projeto foi desenvolvido para fins estritamente acadêmicos como parte da disciplina de **Engenharia de Software** na FIAP.