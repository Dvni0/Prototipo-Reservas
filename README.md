# **🏫 Sistema de Reservas FIAP**

### **Aplicativo Desktop para Gestão de Espaços Acadêmicos**

O sistema **Reservas FIAP** é uma solução desktop desenvolvida para otimizar o agendamento de salas de aula e espaços acadêmicos. Com foco em usabilidade e uma abordagem *Mobile-first* adaptada para o desktop, o aplicativo centraliza a gestão de infraestrutura, eliminando conflitos de horários e automatizando a confirmação via e-mail.

## **👥 Integrantes - Grupo 1º Checkpoint**

* **Guilherme Torres da Silva** * **Luis Fernando Picarelli Gonçalves Guariglia** * **Vinícius Barros Souza** * **Alexandre Caus Haddade** * **Mário Secundino Santana Lopes Portella** ## **✨ Funcionalidades**

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