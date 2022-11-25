#Ejercicio 4: Descargar una copia de un archivo www.py4e.com/code3/romeo.txt.
#Escribir un programa para abrir el archivo romeo.txt y leerlo línea
#por línea. Para cada línea, dividir la línea en una lista de palabras
#utilizando la función split. Para cada palabra, revisar si la palabra ya
#se encuentra previamente en la lista. Si la palabra no está en la lista,
#agregarla a la lista. Cuando el programa termine, ordenar e imprimir
#las palabras resultantes en orden alfabético.
manejador = open('romeo.txt')
listap= list()
for linea in manejador:
    lpalabras=linea.split()
    for i in lpalabras:
        TorF= i in listap
        if TorF is True:
            continue
        listap.append(i)
listap.sort()
print(listap)
