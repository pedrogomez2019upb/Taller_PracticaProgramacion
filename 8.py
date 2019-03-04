#Algoritmo que saque el promedio de 5 notas con el respectivo porcentaje : 15 ,20,15,30,20
#Lo primero que vamos a hacer es recibir las cinco notas a las cuales se les va a sacar el promedio.
n1=float(input("Bienvenido! Vamos a sacar el promedio de tus 5 notas. Por favor ingresa la primera nota: "))
n2=float(input("Ahora ingresa la segunda nota: "))
n3=float(input("Ingresa la tercera nota: "))
n4=float(input("Ingresa la cuarta nota: "))
n5=float(input("Ingresa la quinta nota: "))
#Se hacen diferentes variables que saquen el valor de la nota en su respectivo porcentaje
a=n1*0.15
b=n2*0.2
c=n3*0.15
d=n4*0.3
e=n5*0.2
#Finalmente se saca otra variable que haga las sumatoria de las 5 notas ya promediadas
nf=a+b+c+d+e
#Se imprime el resultado con un mensaje
print("El ponderado de tu materia es: {}. Gracias por utilizar el programa.".format(nf))
#Desarrollado por Pedro Gómez / ID:000396221
