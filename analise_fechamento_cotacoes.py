#PASSO A PASSO 

#1° Buscar no site yahoo finance as cotações das ações no período de 01/01/2020 a 31/12/2020 automaticamente;
#2º Criar análses: 
#    - cotação mínima;
#    - cotação máxima;
#    - média.
# 3º Enviar análises automaticamente por e-mail.

# Importando bibliotecas necessárias

import yfinance
import pyautogui
import time

# Buscando dados de uma ação;

ticker = input("Digite o código da ação: ")
dt_inicial = input("Digite a data inicial (aaaa-mm-dd): ")
dt_final = input("Digite a data final (aaaa-mm-dd): ")
dados = yfinance.Ticker(ticker)
tabela = dados.history(start = dt_inicial, end = dt_final)
print(tabela)

# Selecionando apenas a coluna de Fechamento (Close);

fechamento = tabela.Close
print(fechamento)
