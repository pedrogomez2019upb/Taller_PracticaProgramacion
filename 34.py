#Leer tres valores y ver cual es el mayor de ellos
#Primero hay que leer los valores a analizar
n1=float(input("Bienvenido ! Vamos a analizar el mayor de tres números. Por favor ingresa el primer valor: "))
n2=float(input("Por favor ingresa el segundo valor: "))
n3=float(input("Ingresa el tercer valor: "))
#Vamos a poner tres condicionales if y then para los números 
if n1>n2>n3 or n1>n3>n2:
    print("El número {} es el mayor de todos. Gracias por utilizar el programa.".format(n1))
else:
    if n2>n1>n3 or n2>n3>n1:
        print("El número {} es el mayor de todos. Gracias por utilizar el programa.".format(n2))
    else:
        if n3>n1>n2 or n3>n2>n1:
            print("El número {} es el mayor de todos . Gracias por utilizar el programa.".format(n3))
#Desarrollado por Pedro Gómez / ID:000396221