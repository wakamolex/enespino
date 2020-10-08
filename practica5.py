radio = float(input('Ingrese el radio:'))
volumen = (4/3)*(3.14*(radio**3))
print("El volumen de la esfera es: "+ str(round(volumen,1)) + " m^3")



while  True:
	try:
		dividendo = int(input('Ingrese un dividendo:'))
		divisor = int(input('Ingrese un divisor:'))
		resultado = dividendo/divisor
		break
	except ZeroDivisionError:
		print("Divisor no puede ser 0")

print("El resultado es " + str(resultado))

import os

n = 8
path = os.path.join('files', 'bookstore.txt')
with open(path, 'r') as f:
	for i, line in enumerate(f):
		if i == n - 1:
			print(line)


with open(path, 'r') as f:
	for i in f:
		print(i)


div = []
fechas = []
filt = []
path = os.path.join('files', 'dates.txt')
archivo = open(path, 'r')
with open(path, 'r') as f:
	for i in f:
		div.append(i.split("\t"))

for i in div[3:8]:
	filt.append(i[2])
	print(i[2])

path = os.path.join('files', 'filter.txt')
with open(path, 'w') as f:
	for j in filt:
		f.write(j + "\n")
