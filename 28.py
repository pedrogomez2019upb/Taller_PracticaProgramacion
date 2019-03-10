#Algoritmo que revise si un número es positivo o negativo
#Primero recibimos el valor a analizar
a=float(input("Bienvenido! Vamos a ver si tu número es positivo o negativo. Por favor ingresa el número: "))
#Ponemos un if y then para saber cuando es cero
if a==0:
    print("El número es 0. Gracias por utilizar el programa.")
else:
    #Ahora ponemos las condicionales para saber si es positivo o no
    if a>0:
        print("El número es positivo. Gracias por utilizar el programa.")
    else:
        print("El número es negativo. Gracias por utilizar el programa.")
#Desarrollado por Pedro Gómez / ID:000396221