##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##


# Carga de base de datos y ajuste de formato 

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n','') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Conteo de elementos de columna 4 y 5 por cada registro

datos5 = [(x[0],len(x[3].split(';')),len(x[4].split(';'))) for x in datos4]

# Imprimir en formato necesario

for a,b,c in datos5:
    print ("{},{},{}".format(a,b,c))