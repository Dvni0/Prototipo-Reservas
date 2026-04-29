import sys
import os

# Adiciona a pasta 'src' ao caminho do Python para que as importações funcionem sem erro
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.database import configurar_banco_dados
from views.interface import ReservasFIAP

if __name__ == "__main__":
    # 1. Prepara o Banco de Dados
    configurar_banco_dados()
    
    # 2. Inicia o Front-end
    sistema_principal = ReservasFIAP()
    sistema_principal.mainloop()