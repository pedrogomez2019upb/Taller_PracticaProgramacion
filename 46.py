#Escribe un algoritmo que lea 3 números e indique si al menos 2 de ellos son iguales
#Primero vamos a recibir los valores a analizar
n1=float(input("Bienvenido! Vamos a analizar si al menos dos valores son iguales. Por favor ingresa el primer valor: "))
n2=float(input("Ingresa el segundo valor: "))
n3=float(input("Ingresa el tercer valor: "))
#Vamos a poner condicionales if y else para evaluar si almenos dos de ellos son iguales
if n1==n2 or n1==n3:
    print("Hay al menos dos números iguales.")
else:
    if n2==n3:
        print("Hay al menos dos números iguales.")
    else:
        print("Todos los números son diferentes.")
#Desarrollado por Pedro Gómez / ID:000396221