#6.5 Escriba el código usando find () y string slicing (consulte la sección 6.10)
#para extraer el número al final de la línea a continuación. Convierta el valor
#extraído en un número de punto flotante e imprímalo.

text = "X-DSPAM-Confidence:    0.8475";
inicio=text.find(':')
presplit=text[inicio+1:]
number=float(presplit) #float() elimina los espacios que quedaron en presplit
print(number)
ZzZ=input("Waiting")
