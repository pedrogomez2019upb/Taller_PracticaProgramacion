#Calcular el promedio 
# -*- coding: utf-8 -*-
#Hay que recibir las notas para empezar a sacar los promedios
n1=float(input("Bienvenido ! Vamos a sacar el promedio. Por favor ingresa el primer valor : "))
n2=float(input("Ingresa el segundo valor: "))
n3=float(input("Ingresa el tercer valor: "))
n4=float(input("Ingresa el cuarto valor: "))
n5=float(input("Ingresa el quinto valor: "))
#Aplicamos el porcentaje a cada nota
a=n1*0.15
b=n2*0.2
c=n3*0.15
d=n4*0.3
e=n5*0.2
#Se suma el promedio y se imprime
prom=a+b+c+d+e
print("El promedio del estudiante quedó en: {} . ".format(prom))
#Se pone las condicionales para saber si va perdiendo o va ganando
if prom < 3:
    print("Lo siento , perdiste la materia. Gracias por utilizar el programa")
else:
    if prom >= 3 and prom < 4.5:
        print("Estás pasando la materia.")
    else:
        if prom > 4.5:
            print("Felicitaciones! Eres excelencia académica.")
#Desarrollado por Pedro Felipe Gómez / ID:000396221