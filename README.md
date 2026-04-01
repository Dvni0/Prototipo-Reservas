# Protótipo Reservas FIAP

Este é um protótipo de sistema de reservas de salas para a FIAP, desenvolvido em Python com interface gráfica utilizando customtkinter.

## Funcionalidades
- Login com e-mail institucional
- Seleção de sala e data/horário
- Verificação de conflitos de reserva
- Confirmação visual integrada ao app
- Banco de dados SQLite local

## Como rodar
1. Crie um ambiente virtual Python e ative-o:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
2. Instale as dependências:
   ```sh
   pip install customtkinter tkcalendar pillow
   ```
3. Execute o sistema:
   ```sh
   python Interface Front-end.py
   ```

## Estrutura
- `Interface Front-end.py`: Interface gráfica e lógica principal
- `Servicos_Reservas.py`: Funções de banco de dados e notificações

## Observações
- O banco de dados é criado automaticamente na primeira execução.
- O arquivo `.gitignore` já está configurado para ignorar arquivos sensíveis e temporários.

---

Desenvolvido para fins acadêmicos na FIAP.