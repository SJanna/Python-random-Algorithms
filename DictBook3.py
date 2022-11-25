#Ejercicio 3: Escribe un programa para leer a través de un historial de
#correos, construye un histograma utilizando un diccionario para contar
#cuántos mensajes han llegado de cada dirección de correo electrónico, e
#imprime el diccionario.
manejador=open('mbox-short.txt')
diccionario=dict()
for linea in manejador:
    linea=linea.split()
    if len(linea)<2 or linea[0]!='From':continue
    clave=linea[1]
    diccionario[clave]=diccionario.get(clave,0) +1
print(diccionario)
