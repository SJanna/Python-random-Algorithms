texto= open('romeo.txt')
d=dict()
for linea in texto:
    palabra = linea.split()
    rango=range(len(palabra))
    for i in rango:
        clave = palabra[i]
        d[clave]=d.get(clave,0)+1


lista=list(d.keys())
lista.sort()
for i in lista:
    print(i, d[i]) 
