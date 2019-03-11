#Construya un algoritmo que permita leer una cantidad variable de números y nos indique cuantos fueron mayores a 100 y cuántos menores a 100.
#Creamos los contadores necesarios
mayor=0
menor=0
igual=0
#Se solicitan los valores necesarios
n=int(input("Bienvenido ! Vamos a leer una cantidad de numeros. Ingresa el primer valor: "))
m=int(input("Ingresa el segundo valor: "))
#Se crea una funcion for para el número
for num in range(n,m+1):
	if num>100:
		mayor+=1
	elif num==100:
		igual+=1
	else:
		menor+=1
#Finalmente se imprime los valores
print("Hay {} numeros mayores a 100. Gracias por utilizar el programa".format(mayor))	
print("Hay {} números menores a 100. Gracias por utilizar el programa".format(menor))			
print("Hay {} números iguales a 100. Gracias por utilizar el programa".format(igual)) 
#Desarrollado por Pedro Gómez / ID:000396221