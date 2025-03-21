Este projeto consiste em um script Python para automatizar o cadastro de produto em um sistema web, utilizando as bibliotecas pyautogui, pandas e time. 
O script lê os dados de um arquivo CSV (produtos2.csv) e utiliza pyautogui para interagir com a interface gráfica do sistema web, simulando cliques e digitação de dados.

Arquivos do Projeto:

* automacao.py: Script principal que automatiza o cadastro de produtos.
* auxiliar.py: Script auxiliar para obter as coordenadas do mouse.
* produtos2.csv: Arquivo CSV contendo os dados dos produtos a serem cadastrados (base de dados reduzida, utilizada durante testes).

Dependências:

* Python 3.x
* Bibliotecas Python:
  pyautogui
  pandas
  time
  
Instalação das Dependências:

*Para instalar as dependências, execute o seguinte comando no terminal:

Bash

pip install pyautogui pandas

Uso

1. Preparação do ambiente:

  Certifique-se de que o arquivo produtos2.csv esteja presente na mesma pasta que os scripts Python.
  Abra o navegador Chrome e faça login no sistema web no endereço https://dlp.hashtagtreinamentos.com/python/intensivao/login.
  Posicione a janela do navegador de forma que os campos do formulário de cadastro de produtos sejam visíveis.

2. Execução do script auxiliar (auxiliar.py):

  Execute o script auxiliar.py para obter as coordenadas do mouse dos campos do formulário de cadastro de produtos.
  Anote as coordenadas obtidas para usar no script principal.

3.  Execução do script principal (automacao.py):

  Execute o script automacao.py.
  O script abrirá o navegador Chrome, fará login no sistema web e começará a cadastrar os produtos do arquivo produtos2.csv.
  O script simulará cliques e digitação de dados nos campos do formulário de cadastro de produtos.
  
Estrutura do Arquivo produtos2.csv

* O arquivo produtos2.csv deve conter as seguintes colunas:

  codigo
  marca
  tipo
  categoria
  preco_unitario
  custo
  obs

Explicação dos Scripts

* automacao.py
  
  Importa as bibliotecas pyautogui, pandas e time.
  Lê os dados do arquivo produtos2.csv usando pandas.
  Configura o tempo de espera entre os comandos do pyautogui.
  Abre o navegador Chrome e acessa o sistema web.
  Faz login no sistema web.
  Percorre as linhas do arquivo produtos2.csv e cadastra os produtos no sistema web.
  Utiliza pyautogui.click() para simular cliques nos campos do formulário.
  Utiliza pyautogui.write() para digitar os dados dos produtos.
  Utiliza pyautogui.press() para simular a pressão das teclas "Tab" e "Enter".
  Utiliza pyautogui.hotkey('ctrl', 'a') e pyautogui.press('delete') para limpar o campo de código antes de digitar um novo código.
  Utiliza pyautogui.scroll() para rolar a página para baixo.

* auxiliar.py

  Importa as bibliotecas pyautogui e time.
  Pausa a execução do script por 5 segundos para dar tempo ao usuário de posicionar o mouse.
  Imprime as coordenadas do mouse no console.
  Simula a rolagem da tela para cima.
