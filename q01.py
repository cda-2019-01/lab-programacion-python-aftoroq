##
## Imprima la suma de la segunda columna.
##

# Carga de base de datos y ajuste de formato 

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n',',') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Hacemos el calculo de la suma

q01 = sum([int(row[1]) for row in datos4])

# Imprimimos

print(q01)