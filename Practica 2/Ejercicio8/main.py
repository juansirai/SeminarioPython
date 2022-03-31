# 7. Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
# misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
# inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
# es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.
# Tener en cuenta - Lo que no se puede repetir en la frase son sólo aquellos caracteres que sean
# letras. - No se distingue entre mayúsculas y minúsculas, es decir si en la frase o palabra tenemos
# la letra “T” y la letra “t” la misma NO será un Hererograma. - Para simplificar el ejercicio vamos
# a tomar como que las letras con tilde y sin tilde son distintas. Ya que Python las diferencia:
# >>> 'u'




def heterograma(evaluar):
    i = 0
    letras = []
    continua = True
    while continua and i<len(evaluar):
        if evaluar[i] in letras:
            continua = False
        else:
            letras.append(evaluar[i])
            i+=1
    return continua

jugar = 'y'
while jugar == 'y':
    evaluar = input('Ingrese una frase o palabra: ').replace(' ', '').lower()
    if heterograma(evaluar):
        print('Es un heterograma')
    else:
        print('No es un heterograma')
    jugar = input('Quiere intentar con otra? ').lower()