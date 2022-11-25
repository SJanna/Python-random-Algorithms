#Ejercicio 6: Reescribe el programa que pide al usuario una lista de
#números e imprime el máximo y el mínimo de los números al final cuando
#el usuario ingresa “hecho”. Escribe el programa para almacenar los
#números que el usuario ingrese en una lista, y utiliza las funciones max()
#y min() para calcular el máximo y el mínimo después de que el bucle
#termine.

manejador=open('try.txt','w')
lista=list()
while True:
    numero=input('Igrese un número:')
    if numero == 'fin':break
    manejador.write(numero)
    manejador.write(', ')
    numero=float(numero) #Opcional para este ejercicio
    lista.append(numero)
print('Máximo:',max(lista))
print('Máximo',min(lista))
