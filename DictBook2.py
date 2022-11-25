#Ejercicio 2: Escribir un programa que clasifica cada mensaje de correo
#dependiendo del día de la semana en que se recibió. Para hacer esto
#busca las líneas que comienzan con “From”, después busca por la tercer
#palabra y mantén un contador para cada uno de los días de la semana.
#Al final del programa imprime los contenidos de tu diccionario (el orden
#no importa).
manejador=open('mbox.txt')
diccionario=dict()
for linea in manejador:
    linea=linea.split()
    if len(linea)<3 or linea[0]!='From':continue
    clave=linea[2]
    diccionario[clave]=diccionario.get(clave,0) +1
print(diccionario)
