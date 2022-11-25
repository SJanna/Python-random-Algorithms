#Ejercicio 5: Este programa almacena el nombre del dominio (en vez de
#la dirección) desde donde fue enviado el mensaje en vez de quién envió
#el mensaje (es decir, la dirección de correo electrónica completa). Al
#final del programa, imprime el contenido de tu diccionario.
manejador=open('mbox-short.txt')
diccionario=dict()
for linea in manejador:
    linea=linea.split()
    if len(linea)<2 or linea[0]!='From':continue
    correo=linea[1]
    correo=correo.split('@')
    clave=correo[1]
    diccionario[clave]=diccionario.get(clave,0) +1
print(diccionario)
