#Escriba un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación
#está fuera de rango, imprima un error. Si el puntaje está entre 0.0 y 1.0, imprima
#una calificación usando la siguiente tabla:
#Puntaje Calificación
#> = 0.9 A
#> = 0.8 B
#> = 0.7 C
#> = 0.6 D
#<0.6 F
#Si el usuario ingresa un valor fuera del rango, imprima un mensaje de error
#adecuado y salir. Para la prueba, ingrese una puntuación de 0.85.
Score=input("Score:")
try:
    Sc=float(Score)
    if(Sc<0.0):
        print("Invalid value");
        quit()
    elif(Sc>1.0):
        print("Invalid value");
        quit()
    elif(Sc>=0.9):
        print("A")
    elif(Sc>=0.8):
        print("B")
    elif(Sc>=0.7):
        print("C")
    elif(Sc>=0.6):
        print("D")
    elif(Sc<0.6):
        print("F")
except:
    print("Invalid value")
    quit()
zzz=input("Just Waiting")
