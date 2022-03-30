# Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
# letra. En caso que no se haya ingresado una letra, indique el error. Ver: módulo string

import string

texto = """The constants defined in this module are:The constants defined in this module are:
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants described below. 
This value is not locale-dependent.
string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent 
and will not change.
string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent 
and will not change.
"""

palabras = texto.split(" ")

play = 'Y'

while play == 'Y':
    letra = input("Ingrese una letra: ")
    if letra in string.ascii_letters:
        print(f'Palabras que empiezan con {letra}')
        for p in palabras:
            if p.lower().startswith(letra):
                print(p)
        play = (input("Quiere continuar? (Y/N) ")).upper()
    else:
        print('El caracter ingresado no es una letra, intente nuevamente')
