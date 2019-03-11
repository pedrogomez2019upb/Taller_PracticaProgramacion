#Lea tres números y determine cual es el menor de ellos y el mayor
#Primero hacemos que reciba los valores a analizar
n1=float(input("Bienvenido! Vamos a analizar tres números. Por favor ingresa el primer valor: "))
n2=float(input("Por favor ingresa el segundo valor: "))
n3=float(input("Por favor ingresa el tercer valor: "))
#Vamos a poner más if y then que el ejercicio anterior
if n1>n2>n3:
    print("El número mayor es {} y el menor es {} . Gracias por utilizar el programa.".format(n1,n3))
else:
    if n1>n3>n2:
        print("El número mayor es {} y el menor es {} . Gracias por utilizar el programa.".format(n1,n2))
    else:
        if n2>n1>n3:
            print("El número mayor es {} y el menor es {}. Gracias por utilizar el programa.".format(n1,n3))
        else:
            if n2>n3>n1:
                print("El número mayor es {} y el menor es {}. Gracias por utilizar el programa.".format (n2,n1))
            else:
                if n3>n1>n2:
                    print("El número mayor es {} y el menor es {} . Gracias por utilizar el programa.".format(n3,n2))
                else:
                    if n3>n2>n1:
                        print("El número mayor es {} y el menor es {} . Gracias por utilizar el programa.".format(n3,n1))
#Desarrollado por Pedro Gómez / ID:000396221