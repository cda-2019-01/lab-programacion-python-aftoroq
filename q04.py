##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

# Carga de base de datos y ajuste de formato 

datos=open('data.csv','r').readlines()
datos1 = [z.replace('\n',',') for z in datos]
datos2 = [z.replace(',',';') for z in datos1]
datos3 = [z.replace('\t',',') for z in datos2]
datos4 = [z.split(',') for z in datos3]

# Importamos libreria de datetime y time

import time, datetime

# Creamos funcion para extraer el mes

def MONTH(s): return datetime.datetime.strptime(s,'%Y-%m-%d').strftime('%m')

# Reemplazamos dato incoherente

for i,x in enumerate(datos4):
	for j,a in enumerate(x):
		if '02-29' in a:
			datos4[i][j]=a.replace('02-29','02-28')	

e = [MONTH(row[2]) for row in datos4]

f = sorted(set([MONTH(row[2]) for row in datos4]))

g =[(w,e.count(w)) for w in f]

for a,b in g:
	print ("{},{}".format(a,b))