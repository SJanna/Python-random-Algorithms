numeros= list()
print('Escriba "fin" para obtener el promedio')
while True:
    inp=input('Ingresa un número:')
    if inp=='fin':
        break
    inp=float(inp)
    numeros.append(inp)
    print(numeros)
print('Promedio:',sum(numeros)/len(numeros))
