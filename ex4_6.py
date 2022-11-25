#Escriba un programa para solicitar al usuario las horas y la tarifa por hora
#utilizando la entrada para calcular el salario bruto. El pago debe ser la tarifa
#normal para las horas de hasta 40 horas y una vez y media para la tarifa por hora
#de todas las horas trabajadas por encima de las 40 horas. Ponga la lógica para
#hacer el cálculo de pago en una función llamada computepay () y use la función
#para hacer el cálculo. La función debería devolver un valor. Utilice 45 horas
#y una tarifa de 10,50 por hora para probar el programa (el pago debe ser 498,75).
#Debe usar input para leer una cadena y float () para convertir la cadena en
#un número. No se preocupe por los errores al verificar la entrada del usuario a
#menos que lo desee; puede asumir que el usuario escribe los números correctamente.
#No nombre su variable suma ni use la función sum ().

def computepay(h,r):
    if h>40:
        Nhextra=h-40
        PHext=r*1.5
        PagoExtra=PHext*Nhextra
        Totalpay=(40*r)+PagoExtra
    else:
        Totalpay=h*r
    return Totalpay

hrs = input("Enter Hours:")
fhrs= float(hrs)
rate = input("Enter Rate:")
frate= float(rate)
p = computepay(fhrs,frate)
print("Pay",p)
ZZZ= input("Waiting")
