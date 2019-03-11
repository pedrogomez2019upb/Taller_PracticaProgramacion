#Determinar si un año es o no es biciesto
#Primero hay que recibir el año a analizar
a=int(input("Bienvenido! Vamos a analizar si el año ingresado es biciesto o no. Por favor ingresa el año a revisar: "))
#Vamos a poner las condicionales necesarias partiendo de lo general a lo particular
#donde en este caso debe ser divisible por 4
if a%4==0:
    #Ya sabiendo que es divisible por 4, vamos a aplicarle las otras condicionales
    if a%100 != 0 or a%400==0:
        print("El año {} es biciesto. Gracias por utilizar el programa.".format(a))
    else:
        print("El año {} no es biciesto. Gracias por utilizar el programa.".format(a))
#Desarrollado por Pedro Gómez / ID:000396221