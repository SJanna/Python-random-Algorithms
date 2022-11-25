num1 = 0b000
num2 = 0b001
lista =list()
n=input("Digitos: ")
n=int(n)
for value in range(10):
	num1 = num1 + num2
	Snum1= str(bin(num1))
	if len(Snum1)-2==n and '00' not in Snum1 and '00' not in Snum1:
		lista.append(bin(num1))
print (lista)
