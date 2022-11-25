#Escriba un programa que solicite repetidamente al usuario números enteros hasta
#que el usuario ingrese 'done'. Una vez que ingrese "done", imprima el número
#más grande y el más pequeño. Si el usuario ingresa algo que no sea un número
#válido, descárguelo con un try / except y envíe un mensaje apropiado e ignore
#el número. Ingrese 7, 2, bob, 10 y 4 y haga coincidir la salida a continuación.
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done" :
            break
        inum=int(num)
    except:
        print("Invalid input")
        inum= None
    if inum is not None:
        #Thelargest
        if largest is None:
            largest=inum
        elif inum > largest:
            largest=inum
        #Thesmallest
        if smallest is None:
            smallest=inum
        elif inum < smallest:
            smallest=inum
print("Maximum", largest)
print("Minimun", smallest)
ZZZ=input("Waiting")
