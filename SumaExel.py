
def sumalinea(Listaa):
    totalline=0
    for i in Listaa:
        try:
            i=int(i)
        except:
            i=0
        totalline=totalline+i
    return totalline
total=0
def sumatotal(totallinea, total):
    total=total+totallinea
    return total

tot=0
cont=0
manejador=open('Libro1.csv')
for linea in manejador:
    totalline=0
    Lista= linea.split(';')
    print('Suma linea',cont,':',sumatotal(sumalinea(Lista), total)) #Suma por linea
    x=(sumatotal(sumalinea(Lista), total))
    tot=x+tot
    cont=cont+1
print('Total general:',tot) #Suma de totas la lineas
print("FINALIZADO")
