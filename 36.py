#Escribe un algoritmo que lea tres números y determine si la suma del primero y el segundo es mayor o menor que el tercero
#Primero hay que recibir los números a analizar
n1=float(input("Bienvenido! Vamos a analizar unos números. Por favor ingresa el primer número: "))
n2=float(input("Por favor ingresa el segundo número: "))
n3=float(input("Ingresa el tercer valor: "))
#Se realiza la suma
x=n1+n2
#Se crea la condicional if y then
if x==n3:
    print("La suma da igual al tercer número. Gracias por utilizar el programa.")
else:
    if x>n3:
        print("La suma es mayor al tercer número. Gracias por utilizar el programa.")
    else:
        print("La suma es menor al tercer número. Gracias por utilizar el programa.")
#Desarrollado por Pedro Gómez / ID:000396221
