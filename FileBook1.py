#Ejercio 1: Escribe un programa que lea un archivo e imprima su contenido (línea
#por línea), todo en mayúsculas.
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
    linea=linea.rstrip().upper()
    print(linea)
