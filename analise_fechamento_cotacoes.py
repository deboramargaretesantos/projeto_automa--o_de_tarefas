# Importando bibliotecas necessárias

import yfinance
import pyautogui
import pyperclip
import webbrowser
from time import sleep

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

# Gerando estatísticas

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
media = round(fechamento.mean(), 2)
print(maxima)
print(min)
print(media)

