#Escribe un algoritmo que, dados dos números, verifique si ambos están entre 0 y 5 o retorne false sino es cierto. Por ejemplo 1 y 2 ---> true ; 1 y 8 ---> false
#Primero hay que recibir los valores a analizar
a=int(input("Bienvenido! Por favor ingresa el primer número: "))
b=int(input("Por favor ingresa el segundo valor: "))
#Ponemos condicionales para analizar los valores
if (a<5 and a>0)and(b<5 and b>0):
    print("True")
else:
    print("False")
#Desarrollado por Pedro Gómez / ID:000396221