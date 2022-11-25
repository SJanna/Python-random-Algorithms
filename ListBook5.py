#Ejercicio 5: Escribir un programa para leer a través de datos de una bandeja
#de entrada de correo y cuando encuentres una línea que comience
#con “From”, dividir la línea en palabras utilizando la función split.
#Estamos interesados en quién envió el mensaje, lo cual es la segunda
#palabra en las líneas que comienzan con From.
#Tendrás que analizar la línea From e imprimir la segunda palabra de
#cada línea From, después tendrás que contar el número de líneas From
#(no incluir From:) e imprimir el total al final. Este es un buen ejemplo
#de salida con algunas líneas de salida removidas:
try:
    manejador=open(input('Nombre del archivo:'))
except:
    print('Nombre del archivo no encontrado')
    exit()

contador=0
for linea in manejador:
    palabras=linea.split()
    if len(palabras)<2 or palabras[0]!='From':continue
    contador=contador+1
    print(palabras[1])
print('Hay',contador,'lineas en el archivo que inician con la palabra From')
