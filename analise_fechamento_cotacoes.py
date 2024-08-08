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

# Definido tempo para abrir a caixa de e-mail;

time.sleep(5)
print(pyautogui.position)

# Criando variáveis para destinatário e assunto;

destinatário = "deboramargaretedossantos@gmail.com"
assunto = "Análises Cotação Ação"

# Criando mensagem padrão para corpo do e-mail;

mensagem = f"""

Bom dia!

    Seguem análises da ação {ticker} do período de {dt_inicial} a {dt_final}:

    Cotação máxima: R$ {maxima};
    Cotação mínima: R$ {minima};
    Valor médio: R$ {media}.

    Atenciosamente, 

    Maria Salgado
    Analista
"""
# Configurar uma pausa entre as ações do pyautogui;

pyautogui.PAUSE = 3

# Abrir o navegador no gmail

webbrowser.open("deboramargaretedossantos@gmail.com")
sleep(3)

# Clicar no botão "Escrever"

pyautogui.click(x=2503, y=314)

# Preencher Para

pyperclip.copy(destinatário)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Preencher Assunto

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl" , "v")
pyautogui.hotkey("tab")

# Preencher corpo do e-mail

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl" , "v")

# Clicar no botão enviar

pyautogui.click(x=4056, y=1360)

# fechar a aba

pyautogui.hotkey("ctrl" , "f4")
print("E-mail enviado com sucesso!")

