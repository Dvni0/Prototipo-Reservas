# 🚀 Reservas FIAP

## 📌 Descrição do Problema
No ambiente acadêmico, a reserva de salas de aula e laboratórios muitas vezes ocorre de forma descentralizada ou informal, gerando conflitos de horários, duplicidade de reservas e falta de confirmação imediata para o solicitante. Alunos e professores perdem tempo produtivo tentando localizar espaços disponíveis ou lidando com falhas de comunicação sobre a ocupação das salas.

## 💡 Solução Proposta
O **Reservas FIAP** é uma aplicação desktop desenvolvida para centralizar e automatizar a gestão de espaços. O software oferece uma interface intuitiva (estilo mobile) que permite ao usuário visualizar salas, verificar disponibilidade em tempo real via calendário interativo, realizar o agendamento seguro e receber uma confirmação automática por e-mail, garantindo integridade e organização ao fluxo acadêmico.

## 🆕 Evoluções do Checkpoint 1 para o Checkpoint 2
Diferente da versão inicial, que possuía uma lógica simplificada e arquivos soltos, o sistema avançou para:
* **Arquitetura Modular (MVC):** Separação clara entre Interface (View), Lógica de Negócio (Models) e Autenticação (Auth).
* **Persistência de Dados Real:** Implementação de tabelas de **Usuários** e **Agendamentos** no SQLite.
* **Sistema de Contas:** Inclusão de fluxo de cadastro e login com validação de credenciais no banco de dados.
* **Gestão de Dependências:** Organização via `requirements.txt` e ambiente virtual (`venv`).
* **Estrutura de Pastas Profissional:** Organização dos ativos do projeto (imagens e banco) na pasta `data`.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **GUI:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Interface moderna)
* **Componentes:** `tkcalendar` (Calendário) e `Pillow` (Processamento de imagem)
* **Banco de Dados:** SQLite3
* **Comunicação:** `smtplib` e `email.mime` (Protocolo SMTP para notificações)

## ⚙️ Como Executar

### Pré-requisitos
* Python 3.10 ou superior.
* No Linux (Mint/Ubuntu), é necessário o suporte ao Tkinter:  
  `sudo apt install python3-tk python3-venv -y`

### Instalação
1. Clone o repositório ou baixe os arquivos.
2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux
   # venv\Scripts\activate   # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Execução
A partir da raiz do projeto, execute o arquivo principal:
```bash
python3 src/main.py
```

*(Nota: O banco de dados SQLite e as tabelas necessárias serão criados automaticamente na pasta `src/data/` durante a primeira execução).*

## 📁 Estrutura do Projeto
```text
/
├── README.md
├── requirements.txt
├── docs/               # Documentação e diagramas
└── src/
    ├── main.py         # Inicializador do sistema
    ├── auth/           # Cadastro e Login
    ├── models/         # Banco de dados e regras de reservas
    ├── views/          # Interface do usuário
    └── data/           # Banco de dados (.db) e imagens
```

## ✅ Funcionalidades Implementadas

### Cadastro e Login
* **Cadastro:** Permite criar novas contas com validação de domínio institucional.
* **Login:** Autenticação via e-mail e senha com verificação direta no SQLite.

### Casos de Uso
| Caso de Uso | Status |
| :--- | :--- |
| Criar conta de usuário (@fiap.com.br) | ✅ Implementado |
| Autenticação de usuário (Login) | ✅ Implementado |
| Visualização de grade de salas (2º ao 9º andar) | ✅ Implementado |
| Seleção de data via calendário interativo | ✅ Implementado |
| Verificação de disponibilidade (Anti-conflito) | ✅ Implementado |
| Registro de reserva no banco de dados | ✅ Implementado |
| Envio de e-mail de confirmação automático | ✅ Implementado |
| Edição/Cancelamento de reservas | ❌ Não implementado |

## ⭐ Diferencial do Projeto
### Descrição
O grande diferencial é a **experiência de usuário (UX) convergente**, que traz a facilidade de uso de apps mobile para o ambiente desktop, eliminando a curva de aprendizado. Além disso, a integração nativa com o protocolo SMTP para confirmações em tempo real transforma um simples formulário em um serviço de agendamento completo.

### Justificativa
A arquitetura modular garante que o sistema seja escalável, permitindo adicionar novos prédios ou integração com APIs de calendários externos (como Google Calendar) futuramente, sem a necessidade de reescrever o código base.

## 🎬 Demonstração
*(Espaço reservado para inclusão de vídeo/prints do sistema em funcionamento)*
[https://www.youtube.com/watch?v=Lkjn4f7PVAM&feature=youtu.be](https://www.youtube.com/watch?v=Lkjn4f7PVAM&feature=youtu.be)

## 👥 Integrantes do Grupo
* **Guilherme Torres da Silva**
* **Luis Fernando Picarelli Gonçalves Guariglia**
* **Vinícius Barros Souza**
* **Alexandre Caus Haddade**
* **Mário Secundino Santana Lopes Portella**

## 🔗 Links
* **Repositório GitHub:** [https://github.com/Dvni0/Prototipo-Reservas](https://github.com/Dvni0/Prototipo-Reservas)
* **Miro/Diagramas:** [https://miro.com/app/board/uXjVGqMH6yk=/](https://miro.com/app/board/uXjVGqMH6yk=/?share_link_id=258399336656)
