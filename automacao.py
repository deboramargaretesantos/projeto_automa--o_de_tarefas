#Biblioteca pyautogui usada aqui com a finalidade de controlar o mouse e o teclado, realizar capturas de tela, clicar em campos, digitar textos, entre outros
import pyautogui
#Biblioteca pandas usada aqui Leitura e escrita de arquivos como CSV
import pandas as pd
#Pausar a execução de um programa por um tempo específico com
import time

#Importando base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

#define o tempo de espera entre os comandos do pyautogui
pyautogui.PAUSE = 1.0

#Abrindo o sitema usando chrome, usando pyautogui
pyautogui.press("win")
pyautogui.write("chome")
pyautogui.press("enter")
link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write(link)
pyautogui.press("enter")

#tempo de espera para abertura do sistema
time.sleep(5)

