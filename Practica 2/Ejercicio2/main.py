# Indique la palabra que aparece mayor cantidad de veces en el texto del README.md de numpy.

import requests
from bs4 import BeautifulSoup
from collections import Counter

# extraemos el html del archivo mediante requests
url = 'https://github.com/numpy/numpy/blob/main/README.md'
page = requests.get(url).text

# convertimos a texto plano mediante beatiful soup
soup = BeautifulSoup(page, features='lxml')
texto = soup.get_text()

# generamos una lista con todas las palabras
lista = texto.lower().split()

# instanciamos la clase counter y utilizamos el metodo most_common

print(f'La palabra que aparece mas veces es "{Counter(lista).most_common(1)[0][0]}" con '
      f'{Counter(lista).most_common(1)[0][1]} repeticiones')