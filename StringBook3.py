#El siguiente programa cuenta el número de veces que la letra “a” aparece en una
#cadena.Ejercicio 3: Encapsula este código en una función llamada cuenta, y
#hazla genérica de tal modo que pueda aceptar una cadena y una letra
#como argumentos.
Finalizador=None
while Finalizador != 'done':
    def Nletras(fpalabra, fletra):
        count=0
        for i in fpalabra:
            if i == fletra:
                count=count+1
        return count
    palabra=input('Palabra:')
    letra=input('letra:')
    print(Nletras(palabra,letra))
    Finalizador=input('Escriba "done" si desea finalizar: ')
ZzZ=input('Waiting')
