#Algoritmo que lea un número y determine si es par o impar
#Primero nos toca recibir el valor 
a=int(input("Bienvenido! Vamos a revisar si el valor ingresado es par o impar. Por favor ingresa el número a evaluar: "))
#Ponemos una condicional if y then para revisar el valor
if a%2==0:
    print("El número {} es par. Gracias por utilizar el programa.".format(a))
else:
    print("El número {} es impar. Gracias por utilizar el programa.".format(a))
#Desarrollado por Pedro Gómez / ID:000396221