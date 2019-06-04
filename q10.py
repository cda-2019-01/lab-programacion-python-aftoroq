##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##

# Carga de base de datos y ajuste de formato 

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n','') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Seleccionamos la columna de interes, y dividimos por ;

datos5 = [str(row[4]).split(';') for row in datos4]

# Creamos una lista unica que contenga todos los valores

datos6 = [data for sublist in datos5 for data in sublist]

# Dividimos cada llave

datos7 = [(dato.split(':')) for dato in datos6]

# Creamos una lista auxiliar con con la columna que contiene las letras

lista_aux = [x[0] for x in datos7]

# Creamos lista auxiliar con valores unicos

valores_unicos = set(x[0] for x in datos7)
valores_unicos = list(valores_unicos)
valores_unicos.sort()

# Creamos conteo del archivo

q10 = [(fila,lista_aux.count(fila)) for fila in valores_unicos]

# Imprimir en formato necesario

for fila in q10:
    print ("{},{}".format(fila[0],fila[1]))

