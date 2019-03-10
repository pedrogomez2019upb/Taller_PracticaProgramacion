#Algoritmo que vea si es par positivo , par negativo , impar postivio o impar negativo
#Primeo hay que recibir el valor a analizar
a=float(input("Bienvenido! Vamos a ver si es par o impar . Por favor ingresa el valor a analizar: "))
#Ponemos primero para ver si es 0
if a==0:
    print("El número es 0. Gracias por utilizar el programa")
else:
    #Primero vemos si es positivo o negativo
    if a>0:
        #Vemos si es par o impar
        if a%2==0:
            print("El número es par positivo. Gracias por utilizar el programa.")
        else:
            print("El número es impar positivo. Gracias por utilizar el programa.")
    else:
        if a%2==0:
            print("El número es par negativo. Gracias por utilizar el programa.")
        else:
            print("El número es impar negativo. Gracias por utilizar el programa.")
#Desarrollado por Pedro Gómez / ID:000396221