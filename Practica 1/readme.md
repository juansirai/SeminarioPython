<h1>Seminario de Lenguaje: Python</h1>

<h2>Trabajo Práctico 1</h2>
<h4>Alumno: Sirai Juan <br>
Legajo: 20196/3</h4>
-----------------------------------------------------
<h3>Enunciado: </h3>
- Escriba en un archivo llamado adivino.py el siguiente programa en Python (similar al que
vieron en la teoría Clase 1 de la teoría).

```py
## Adivina adivinador....
import random
numero_aleatorio = random.randrange(5)
gane = False
print("Tenés 3 intentos para adivinar un entre 0 y 99")
intento = 1
while intento < 4 and not gane:
    numeroIngresado = int(input('Ingresa tu número: '))
    if numeroIngresado == numero_aleatorio:
       print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
       gane = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
```

Luego, modifíquelo para que:
* Genere un número aleatorio entre 0 y 100.
* Los nombres de las variables respeten la guía de estilo del lenguaje.
* Se de 5 posibilidades para adivinar el número.