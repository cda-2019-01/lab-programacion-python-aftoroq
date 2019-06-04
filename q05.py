##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##

# Carga de base de datos y ajuste de formato 

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n',',') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Importamos librerias

import itertools
from itertools import groupby
from operator import itemgetter

# Creamos base de datos con las variables de interes

g=[[row[0],int(row[1])] for row in datos4]

# Creamos una lista con los maximos

maxg=[max(list(group)) for key,group in itertools.groupby(sorted(g,key=itemgetter(0)),itemgetter(0))]

# Creamos lista con minimos

ming=[min(list(group)) for key,group in itertools.groupby(sorted(g,key=itemgetter(0)),itemgetter(0))]

# Traer los maximos y manimos en donde la letra coincida entre ambas listas (maximo y minimo)

h=[[row_min[0], row_max[1], row_min[1]] for row_max in maxg for row_min in ming if row_min[0] == row_max[0]]

# Imprimir en formato necesario

for valor1,valor2,valor3 in h:
		print('{},{},{}'.format(valor1,valor2,valor3))