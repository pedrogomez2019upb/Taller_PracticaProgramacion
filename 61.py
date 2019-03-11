#Escribe un algoritmo que imprima los números naturales contenidos entre dos números n y m (verificar que m>n)
#Primero recibios los valores n y m
n=int(input("Hola ! Vamos a imprimir los números contenidos entre dos números n y m . Por favor ingresa el primer valor: "))
m=int(input("Ingresa el segundo valor: "))
#Condicional if then
if m<n:
    print("No se puede desarrollar. Gracias por utilizar el programa")
else:
    for i in range(n,m):
        i=i+1
        print("Los números entre {} y {} es : {}. Gracias por utilizar el programa.".format(n,m,i))
#Desarrollado por Pedro Gómez / ID:000396221
