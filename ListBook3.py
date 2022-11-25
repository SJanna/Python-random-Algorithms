#Ejercicio 3: Reescribe el código guardián en el ejemplo de arriba sin las
#dos sentencias if. En vez de eso, utiliza una expresión lógica compuesta
#utilizando el operador lógico or con una sola sentencia if.

manejador = open('mbox-short.txt')
for linea in manejador:
    palabras=linea.split()
    if len(palabras)==0 or palabras[0] != ('From'):continue
    print(palabras[2])
