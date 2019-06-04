##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##

# Carga de base de datos y ajuste de formato 

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n','') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Creamos archivo con columnas de interes

datos5 = [(x[1], x[0]) for x in datos4]

# Creamos variable auxiliar con los valores unicos de la columna con numeros

aux = set(data[0] for data in datos5)
aux = list(aux)
aux.sort()

# Creamos resultado final agregando para cada numero el total de letras correspondientes

q08 = [(a,[b for c,b in datos5 if a==c]) for a in aux]

# Ajustamos el orden de las letras en  la segunda columna

q08 = [(a,sorted(b)) for a,b in q08]

# Imprimimos resultado final sin estar incluido en una lista 

for dato in q08:
    print (dato)