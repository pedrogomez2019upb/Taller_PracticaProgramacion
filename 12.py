#Algoritmo que calcule el promedio de tres números
#Primero vamos a dar un mensaje de bienvenida y recibir los valores necesarios para hacer el siguiente promedio
a1=float(input("Bienvenido! Vamos a sacar el promedio de tres notas. Por favor ingresa la primera: "))
a2=float(input("Ahora ingresa la segunda nota: "))
a3=float(input("Ingerse la tercera nota: "))
#Ahora hacemos una variable x que saque el promedio de las tres notas
x=(a1+a2+a3)/3
#Finalmente imprimimos el resultado del promedio
print("Las notas {} {} {} tienen como promedio: {}. Gracias por utilizar el programa.".format(a1,a2,a3,x))
#Desarrollado por Pedro Gómez / ID:000396221