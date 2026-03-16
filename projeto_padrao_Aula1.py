# Bibliotecas utilizadas
import pyautogui as py
import pandas as pd
import time

# Variáveis utilizadas
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'batatinha123@gmail.com'
senha = 'senhabraba123'

# Pausa entre comandos para não quebrar o código
py.PAUSE = 0.3

# Passo a passo do programa:
# Passo 1: Entrar no sistema da empresa
# 1.1 - Abrindo navegador
py.press('win')
py.write('brave')
py.press('enter')
# 1.2 - Entrando no site
py.write(link)
py.press('enter')
time.sleep(3) # Tempo para o site carregar

# Passo 2: Logar no sistema
py.click(x=768, y=368) # Clicando no campo de email
py.write(email)
py.press('tab')
py.write(senha)
py.press('tab')
py.press('enter')
time.sleep(3) # Tempo para o site carregar

# Passo 3: Abrir a base de dados
tabela = pd.read_csv('produtos.csv') # Carrega os dados da tabela para uma variável

# Passo 4: Cadastrar 1 produto e Passo 5: Repetir o passo 4 até acabar a lista
for linha in tabela.index: # Repete o cadastro para cada item/linha da tabela
    py.click(x=719, y=252)
    codigo = str(tabela.loc[linha, 'codigo'])
    py.write(codigo)
    py.press('tab')

    marca = str(tabela.loc[linha, 'marca'])
    py.write(marca)
    py.press('tab')

    tipo = str(tabela.loc[linha, 'tipo'])
    py.write(tipo)
    py.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    py.write(categoria)
    py.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    py.write(preco_unitario)
    py.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    py.write(custo)
    py.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan': # Verificando se o valor é nulo
        py.write(obs)
    py.press('tab')
    py.press('enter')

    py.scroll(5000) # Retorna ao inicio da página(poderia usar home)


    

