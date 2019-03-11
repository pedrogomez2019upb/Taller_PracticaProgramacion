#64. Escribe un algoritmo que lea n números y calcule su suma y su promedio
#Contador
i=0
y=0
#Mensaje de bienvenida
n=int(input("Bienvenido ! Vamos a calcular el promedio de n números . Por favor ingresa la cantidad de números a evaluar: "))
#Condicional for
for i in range (0,n):
    x=float(input("Ingresa el número \n: "))
    y=x+i
#imprimir
print("La suma es: {}".format(x))
