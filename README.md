# **🏫 Sistema de Reservas FIAP**

### **Aplicativo Desktop para Gestão de Espaços Acadêmicos**

O sistema **Reservas FIAP** é uma solução desktop desenvolvida para otimizar o agendamento de salas de aula e espaços acadêmicos. Com foco em usabilidade e uma abordagem *Mobile-first* adaptada para o desktop, o aplicativo centraliza a gestão de infraestrutura, eliminando conflitos de horários e automatizando a confirmação via e-mail.

## **👥 Integrantes \- Grupo 1º Checkpoint**

* **Guilherme Torres da Silva** 
* **Luis Fernando Picarelli Gonçalves Guariglia** 
* **Vinícius Barros Souza**  
* **Alexandre Caus Haddade** 
* **Mário Secundino Santana Lopes Portella** 

## **✨ Funcionalidades**

* 🔐 **Autenticação Segura:** Login validado apenas para domínios @fiap.com.br.  
* 📅 **Agendamento Visual:** Calendário interativo para seleção de datas e horários (07:00 às 22:00).  
* 🏢 **Grade de Salas:** Gestão de espaços do 2º ao 9º andar (salas 201 a 903).  
* 🛡️ **Prevenção de Conflitos:** Validação em tempo real para evitar reservas duplicadas no mesmo horário/sala.  
* 📧 **Notificação Automática:** Envio de e-mail de confirmação via protocolo SMTP.  
* 🎨 **Interface Moderna:** UI construída com customtkinter seguindo a identidade visual da FIAP.

## **🛠️ Tecnologias e Arquitetura**

O projeto segue um padrão de separação de responsabilidades (Front-end e Back-end):

* **Linguagem:** Python 3.10+  
* **Interface Gráfica:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), tkcalendar, Pillow.  
* **Banco de Dados:** SQLite3 (Persistência local).  
* **Comunicação:** smtplib (Protocolo de e-mail).

## **🚀 Como Executar o Projeto**

### **1\. Preparar Ambiente**

Recomendamos o uso de um ambiente virtual para isolar as dependências:

\# Criar ambiente virtual  
python \-m venv .venv

\# Ativar no Windows  
.venv\\Scripts\\activate

\# Ativar no Linux/Mac  
source .venv/bin/activate

### **2\. Instalar Dependências**

pip install customtkinter tkcalendar pillow

### **3\. Rodar a Aplicação**

python interface\_reservas.py

*(Nota: O banco de dados SQLite será criado automaticamente na primeira execução).*

## **📂 Estrutura do Projeto**

* interface\_reservas.py: Contém a classe principal da interface, lógica de navegação e modais de feedback.  
* Servicos\_Reservas.py: Camada de serviço responsável pelas queries SQL, validação de disponibilidade e envio de e-mails.  
* dados\_agendamentos\_fiap.db: Banco de dados gerado localmente.

## **🗄️ Estrutura da Tabela de Dados (agendamentos)**

| Campo | Tipo | Descrição |
| :---- | :---- | :---- |
| identificador | INTEGER | Chave Primária (Auto-incremento). |
| conta\_usuario | TEXT | E-mail do solicitante. |
| numero\_sala | TEXT | Número da sala reservada. |
| data\_horario | TEXT | Concatenação de Data e Hora da reserva. |
| registro\_tempo | TIMESTAMP | Data/hora de criação do registro. |

## **📝 Licença**

Este projeto foi desenvolvido para fins estritamente acadêmicos como parte da disciplina de **Engenharia de Software** na FIAP.
