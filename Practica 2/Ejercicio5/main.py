# 5. Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de
# veces que se encuentra el string en la frase. No distingir entre mayúsculas y minúsculas.

jugar = 'y'

while jugar == 'y':
    frase = input("Ingrese una frase: ").lower()
    palabra = input("Ingrese una palabra a buscar: ").lower()
    frase_lista = frase.split()
    print(f"En la frase dada, la palabra {palabra} se encuentra {frase.count(palabra)} veces")
    jugar = input('Desea seguir jugando? (y/n)').lower()