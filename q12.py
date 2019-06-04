##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##

# Carga de base de datos y ajuste de formato 

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n','') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Creamos listas vacias para almacenar llaves y claves

llave = []
claves = []

# Agregamos datos a las listas vacias

for fila in datos4:  
    llave += [(int(fila[1]), valor) for valor in fila[3].split(';')]
    claves += [valor for valor in fila[3].split(';')]

# Creamos lista con valores unicos

valores_unicos = set(claves)
valores_unicos = list(valores_unicos)
valores_unicos.sort()

# Imprimimos en formato necesario

for valor in valores_unicos:
    x=0
    for i,j in llave:
        if valor == j:
            x += i
    print ("{},{}".format(valor,x))