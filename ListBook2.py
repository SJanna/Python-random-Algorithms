#Ejercicio 2: Encontrar que línea del programa de arriba no está protegida
#(método guardián) propiamente. Trata de construir un archivo de
#texto que cause que el programa falle y después modifica el programa de
#modo que la línea es propiamente protegida y pruébalo para asegurarte
#que el programa es capaz de manejar tu nuevo archivo de texto.

#Si una linea comienza con From, pero el resto de la linea está vacia entonces dará error, así lo corregí:
manejador = open('try.txt')
for linea in manejador:
    palabras=linea.split()
    if len(palabras)<3 or palabras[0] != ('From'): continue #Con len(palabras)<3 obligo a que si se encuentra un From siempre haya algo en la pocisión [2]
    print(palabras[2])
