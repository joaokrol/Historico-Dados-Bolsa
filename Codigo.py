from time import sleep
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

navegador.get('https://www.ibovx.com.br/historico-papeis-bovespa.aspx?papel=abev3&qtdpregoes=100')

dados = navegador.find_element(By.XPATH, '//*[@id="idConteudo"]/div/div[6]/table/tbody').get_attribute('innerText')

dados_split = dados.split('\n')

valores = []
header = []

for i in dados_split:
    if(i != ''):
        valores.append(i.split('\t'))

header = valores.pop(0)
valores

df = pd.DataFrame(valores, columns=header)
df.to_csv('dados.csv')