#Construya un algoritmo que le solicite al usuario un número entero positivo, si el usuario digita un valor no permito, le debe volver a pedir el número. Una vez ingrese un valor válido deberá imprimir dicho valor.
num=int(input("Bievenido! Vamos a analizar el número . Por favor digita un numero entero positivo: "))
#Se crea una condicional while
while num<0:
	num=int(input("Incorrecto! Ingresa un número entero: "))
	if num>0:
        #Ahora imprimimos el valor
		print(num)
		print("Gracias por utilizar el programa.")
#Desarrollado por Pedro Gómez / ID:000396221