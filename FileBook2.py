#Ejercicio 2: Escribe un programa que solicite un nombre de archivo
#y después lea ese archivo buscando las líneas que tengan la siguiente
#forma: X-DSPAM-Confidence: 0.8475 (Usar el archivo mbox-short.txt )
#Debemos sacar el número de la linea de texto
while True:
    arch=input('Nombre del archivo:')
    if arch == 'fin':
        print('Programa finalizado')
        exit()
    try:
        archivo= open(arch)
        break
    except:
        print('El archivo *'+arch+'* no se ha encontrado')

for linea in archivo:
    if linea.startswith('X-DSPAM-Confidence:'):
        findline=linea.find(':') #Buscamos el :
        flinea=linea[findline+1:] #Se toma todo lo que hay después de :
        number=float(flinea) #Se pasa a float para quitar todos los espacios
        print(number)
