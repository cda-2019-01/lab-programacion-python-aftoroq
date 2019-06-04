##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##

# Carga de base de datos y ajuste de formato 

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n','') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Seleccionamos los datos necesarios

datos5 = [(dato[0],dato[4].split(';')) for dato in datos4]

# Imprimimos en formato necesario

for valor in range(len(datos5)):
    x=0
    for valor2 in range(len(datos5[valor][1])):
        x += int(datos5[valor][1][valor2][-1])
    print ("{},{}".format(datos5[valor][0],x))