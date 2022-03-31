
cadena = list(input("Ingresa la clave (debe tener menos de 10 caracteres y no "
               "contener los símbolos:@ y !):"))

continua = True
while continua:
    if len(cadena)>=10:
        print('Debe tener menos de diez caracteres')
        cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no "
                       "contener los símbolos:@ y !):").split()
    elif '@' in cadena or '!' in cadena:
        print('No debe contener @ ni !')
        cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no "
                       "contener los símbolos:@ y !):").split()
    else:
        print('Clave correcta')
        continua = False


