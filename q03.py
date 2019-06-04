##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##

# Carga de base de datos y ajuste de formato

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n',',') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Importar librerias

from itertools import groupby

# Crear lista auxiliar 

list_aux = [[row[0], int(row[1])] for row in datos4]

# Crear archivo final

q03 = []

for valor1, valor2 in groupby(sorted(list_aux), key=lambda x: x[0]):
    q03.append([valor1, sum(valor3[1] for valor3 in valor2)])

# Imprimir en formato necesario

for a,b in q03:
	print("{},{}".format(a,b))
