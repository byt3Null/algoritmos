# Facultad de Ingenieria Universidad de Buenos Aires

# Script Name		: burbujeo.py
# Author				: Rolon Leonel
# Created				: 20th Dic 2016
# Last Modified		:
# Version				: python 2.7


# Description			: El burbujeo es un algoritmo de ordenamiento de datos, que ordena los datos de menor a mayor en una lista. 

# Example
# [4,3,1,2] ---> [1,2,3,4]

#definimos una funcion llamada burbujeo que va tomar como parametro una tupla

def burbujeo(*v): #*v es una tupla, las tuplas son conjuntos inmutables

	datos = list(v) #tupla->lista   las lista son conjuntos mutables
	lista = datos[:] #desligo el vinculo con la sublista 
	
	#algoritmo
	for i in range(len(datos)):
		for j in range(len(datos)-1-i):
			if datos[j] >= datos[j+1]:       
				aux = datos[j+1]
				datos[j+1] = datos[j]
				datos[j] = aux
	
	#muestra datos
	for i in lista:
		print i, ;
	
	print "-->", ;
	
	for i in datos:
		print i, ;
	
