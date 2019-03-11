#Escribe un algoritmo que dado un número n, imprima los números entre 1 y n siguiendo la siguiente secuencia:
#1 -2 3 -4 5 -6 ….
#Vamos a introducir el programa
n=int(input("Bienvenido! Vamos a imprimir una secuencia dada. Ingrese el número a analizar: "))
#Vamos a poner los valores necesarios en las condicionales.
for i in range(1,n+1):
	if i%2==0:
		i=i*-1
	print(i)
#Desarrollado por Pedro Gómez / ID:000396221

