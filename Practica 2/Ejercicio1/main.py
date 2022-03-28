# 1. Tomando el texto del README.md de numpy, imprima todas las líneas que contienen ‘http’ o
# ‘https’.

import requests
from bs4 import BeautifulSoup

# extraemos el html del archivo mediante requests
url = 'https://github.com/numpy/numpy/blob/main/README.md'
page = requests.get(url).text

# convertimos a texto plano mediante beatiful soup
soup = BeautifulSoup(page, features='lxml')
texto = soup.get_text()

lista_lineas = texto.split('\n')

for linea in lista_lineas:
    if 'http' in linea:
        print(linea)