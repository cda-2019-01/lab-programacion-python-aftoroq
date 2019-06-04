##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

# Carga de base de datos y ajuste de formato 

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n',',') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Creamos una variable auxiliar

resultado = set([row[0] for row in datos4])
resultado = list(resultado)
resultado.sort()

q02_aux = [row[0] for row in datos4]

q02 = [(w,q02_aux.count(w)) for w in resultado]

# Imprimimos resultado

for a,b in q02:
	print("{},{}".format(a,b))
