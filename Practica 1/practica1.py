import random

numero_aleatorio = random.randrange(100)
gane = False
print("Tenés 5 intentos para adivinar un entre 0 y 100")
intento = 1
while (intento < 6) and (not gane):
    numero_ingresado = int(input(f'Itento {intento}: Ingresa tu número: '))
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        if(numero_ingresado > numero_aleatorio):
            print('Ayy, te pasaste! Intenta con un número mas pequeño 😉')
        else:
            print('No tengas miedo, arriesga con un número mas alto! ')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
