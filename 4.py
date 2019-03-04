#Algoritmo que imprima la suma de dos números
#Primero vamos a pedirle al cliente que nos de los dos números.
#Para ello vamos a solicitar dos variables float con mensaje.
x=float(input("Bienvenido! Vamos a sumar dos números, para ello necesito que por favor me des el primer valor: "))
y=float(input("Ahora ingresa el segundo valor: "))
#Sacamos una tercera variable que tenga el procedimiento matemático a imprimir
z=x+y
#Finalmente imprimimos el valor z con los números x y y.
print("La suma de los números {} y {} es de : {}. Gracias por utilizar el programa".format(x,y,z))
#Desarrollado por Pedro Gómez / ID:000396221
