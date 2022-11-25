#Ejercicio 1: Descargar una copia del archivo www.py4e.com/code3/words.txt
#Escribe un programa que lee las palabras en words.txt y las almacena
#como claves en un diccionario. No importa qué valores tenga. Luego
#puedes utilizar el operador in como una forma rápida de revisar si una
#cadena está en el diccionario.
manejador = open('words.txt')
diccionariop= dict()
clave=0
for linea in manejador:
    lpalabras=linea.split()
    for i in lpalabras:
        TorF= i in diccionariop
        if TorF is True:
            continue
        diccionariop[i]=clave
        clave=clave+1
buscar=input('Buscar llave:')
print(buscar in diccionariop)
