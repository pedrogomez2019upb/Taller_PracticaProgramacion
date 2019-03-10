#Escribe un algoritmo que lea un número y si este es mayor o igual a 10 devuelva el triple de este de lo contrario la cuarta parte de este.
#Primero hay que recibir el valor
a=float(input("Bienvenido! Vamos a analizar un número. Por favor ingresa el número: "))
#Ponemos las condicionales necesarias
if a>= 10:
    y=a*3
    print("El valor de {} queda en {}. Muchas gracias por utilizar el programa.".format(a,y))
else:
    z=a/4
    print("El valor de {} queda en {} . Muchas gracias por utilzar el programa.".format(a,z))
#Desarrollado por Pedro Gómez / ID:000396221