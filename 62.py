#Escribe un algoritmo que determine la suma de los números naturales contenidos entre dos números n y m (verificar que m>n)
#Contador para suma
suma=0
#Primero recibios los valores n y m
n=int(input("Hola ! Vamos a imprimir los números contenidos entre dos números n y m . Por favor ingresa el primer valor: "))
m=int(input("Ingresa el segundo valor: "))
#Condicional if then
if m<n:
    print("No se puede desarrollar. Gracias por utilizar el programa")
else:
    for i in range(n,m+1):
        suma = i+i
        #Se imprime el resultado fuera del for
print(suma)
#Desarrollado por Pedro Gómez / ID:000396221