#Ejercicio 3: Algunas veces cuando los programadores se aburren o
#quieren divertirse un poco, agregan un inofensivo Huevo de Pascua
#a su programa. Modifica el programa que pregunta al usuario por el
#nombre de archivo para que imprima un mensaje divertido cuando el
#usuario escriba “na na boo boo” como nombre de archivo. El programa
#debería funcionar normalmente para cualquier archivo que exista o no
#exista. Aquí está un ejemplo de la ejecución del programa:
while True:
    arch=input('Nombre del archivo:')
    if arch == 'na na boo boo':
        print("Duuba doo, ¿Cómo lo sabias?")
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
