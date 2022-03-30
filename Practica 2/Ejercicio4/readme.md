4. Para la aceptación de un artículo en un congreso se definen las siguientes especificaciones que
deben cumplir y recomendaciones de escritura:

• título: 10 palabras como máximo

• cada oración del resumen:
 * hasta 12 palabras: fácil de leer
 * entre 13-17 palabras: aceptable para leer
 * entre 18-25 palabras: difícil de leer
 * mas de 25 palabras: muy difícil
 
Dado un artículo en formato string, defina si cumple las especificaciones del título y cuántas oraciones tiene de cada categoría. El formato estándar en que recibe el string tiene la siguiente forma:


evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit withresumen: Distributed agent-based modeling (ABM) on high-performance computing resources provide"""

<br>
En este ejemplo debería informar:
* titulo está ok
* Cantidad de oraciones fáciles de leer: 1, aceptables para leer: 2, dificil de leer: 1, muy dificil
de leer: 2

*investigue Pattern Matching para una solución simplificada.* 
¿cuántas variables utilizó para guardar la cantidad de cada categoría, se podría usar alguna estructura?