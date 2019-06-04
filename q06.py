##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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

# Creamos lista auxiliar con valores unicos

valores_unicos = set(x[0] for x in datos7)
valores_unicos = list(valores_unicos)
valores_unicos.sort()

# Hallamos valores finales

for x in valores_unicos:
    q06 = (x,min([item[1] for item in datos7 if item[0]==x]),max([item[1] for item in datos7 if item[0]==x]))
    print ('{},{},{}'.format(q06[0],q06[1],q06[2]))