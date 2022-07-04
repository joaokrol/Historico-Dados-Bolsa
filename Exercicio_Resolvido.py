from time import sleep
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

def url(nome, numero):
    return f'https://www.ibovx.com.br/historico-papeis-bovespa.aspx?papel={nome}&qtdpregoes={numero}'

acoes = ['PETR3','ABEV3','VALE3']

dados = []
numero = 1000

for i in acoes:
    navegador.get(url(i, numero))
    sleep(2)
    dados.append(navegador.find_element(By.XPATH, '//*[@id="idConteudo"]/div/div[8]/table/tbody').get_attribute('innerText').split('\n'))

header = []
for i in range(len(dados)):
    header = dados[i].pop(0).split('\t')
header.insert(0,'Nome')

valores = []

for e,i in enumerate(dados):
    for j in i:
        aux = j.split('\t')[:]
        if(aux[0] != ''):
            aux.insert(0,acoes[e])
            valores.append(aux)
valores

df = pd.DataFrame(valores,columns=header)
df.to_csv("todos_valores.csv",index_label='Indice')