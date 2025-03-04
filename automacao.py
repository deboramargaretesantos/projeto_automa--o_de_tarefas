#Biblioteca pyautogui usada aqui com a finalidade de controlar o mouse e o teclado, realizar capturas de tela, clicar em campos, digitar textos, entre outros
import pyautogui
#Biblioteca pandas usada aqui Leitura e escrita de arquivos como CSV
import pandas as pd
#Pausa a execução de um programa por um tempo específico com
import time

#Importando base de dados
tabela = pd.read_csv("produtos2.csv")
print(tabela)

#Tempo de espera entre os comandos do Pyautogui.
pyautogui.PAUSE = 1.5

#Abre o sitema usando chrome, usando pyautogui
pyautogui.press("win")
pyautogui.write("chome")
pyautogui.press("enter")
link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write(link)
pyautogui.press("enter")
#Tempo de espera para abertura do sistema, antes que a próxima etapa comece.

#Faz o  login (qualquer e-mail e senha funcionará)252.95
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
    pyautogui.click(x=381, y=255)
    pyautogui.hotkey('ctrl', 'a')  # Seleciona todo o texto
    pyautogui.press('delete')  # Deleta o texto selecionado
    #Busca o código da tabela e escreve no campo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    #Passa para o próximo campo
    pyautogui.press("tab")
    #Segue essa sequência para os demais campos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    #Verifica se tem informação em "obs", caso contrário não preenche
    if not pd.notna(tabela.loc[linha, "obs"]):
       pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.click(x=605, y=222)
    pyautogui.press("enter")
    pyautogui.scroll(3000)


  