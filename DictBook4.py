#Ejercicio 4: Agrega código al programa anterior para determinar quién
#tiene la mayoría de mensajes en el archivo. Después de que todos los
#datos hayan sido leídos y el diccionario haya sido creado, mira a través
#del diccionario utilizando un bucle máximo (ve Capítulo 5: Bucles máximos
#y mínimos) para encontrar quién tiene la mayoría de mensajes e
#imprimir cuántos mensajes tiene esa persona.

manejador=open('mbox-short.txt')
diccionario=dict()
maximo=None
minimo=None
minclave=None
maxclave=None
minlist=list()
maxlist=list()
for linea in manejador:
    linea=linea.split()
    if len(linea)<2 or linea[0]!='From':continue
    clave=linea[1]
    diccionario[clave]=diccionario.get(clave,0) +1
for i in diccionario:
    if maximo is None or diccionario[i]>maximo:
        maximo=diccionario[i]
        maxclave=i
    if minimo is None or diccionario[i]<minimo:
        minimo=diccionario[i]
        minclave=i

#Este ciclo lo uso para crear una lista con todos los correos que hayan enviando la misma cantidad (menor o mayor) de correos
for clave in diccionario:
    if diccionario[clave]==minimo:
        minlist.append(clave)
    if diccionario[clave]==maximo:
        maxlist.append(clave)
#------------
print('\nSolo uno')
print('El máximo es',maxclave,'con',maximo,'correos' )
print('El mínimo es',minclave,'con',minimo,'correos' )
print('\nTodos')
print('El máximo es',maxlist,'con',maximo,'correos' )
print('El mínimo es',minlist,'con',minimo,'correos' )
