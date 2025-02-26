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
#fazendo login (qualquer e-mail e senha funcionará)
pyautogui.click(x=596, y=377)
pyautogui.write("deborasantos@gmail.com")
pyautogui.press("enter")
pyautogui.click(x=546, y=470)
pyautogui.write("****")
pyautogui.press("enter")

#Aqui precisamos percorrer as linhas da tabela
#Para cada linha vamos cadastrar um produto
for linha in tabela.index:
    #Clica no primeiro campo
    pyautogui.click(x=470, y=254)
    #Pega o código da tabela e escreve no campo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    #passando para o próximo campo
    pyautogui.press("enter")
    #segue essa sequência para os demais campos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("enter")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("enter")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("enter")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("enter")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("enter")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("enter")
    #verifica se tem informação em "obs", caso contrário não preenche
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

  