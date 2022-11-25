#Escriba un programa para solicitar al usuario las horas y la tarifa por
##hora utilizando la entrada para calcular el salario bruto. Pague la tarifa
#por hora por las horas hasta 40 y 1.5 veces la tarifa por hora por todas
#las horas trabajadas por encima de las 40 horas. Utilice 45 horas y una
#tarifa de 10,50 por hora para probar el programa (el pago debe ser 498,75).
#Debe usar input para leer una cadena y float () para convertir la cadena en
#un número. No se preocupe por los errores de verificación de la entrada del
#usuario, suponga que el usuario escribe los números correctamente.
hrs= input("Horas de trabajo: ")
h=float(hrs)
rte= input("Pago por hora: ")
r=float(rte)
if h>40:
    Nhextra=h-40
    PHext=r*1.5
    PagoExtra=PHext*Nhextra
    PagoTotal=(40*r)+PagoExtra
else:
    PagoTotal=h*r
print("El pago total es de:", PagoTotal)
zzz=input("Just waiting")
