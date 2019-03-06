#Algoritmo que determine el tiempo de caída de un objeto que se suelta desde una velocidad inicial y final
#Primero damos un mensaje de bienvenida para recibir la altura h
h=float(input("Bienvenido! Vamos a calcular el tiempo de caida en un objeto con altura h. Por favor ingresa la altura: "))
#Planteamos la formula para calcular el tiempo con la altura
t=(2*h)/9.81
#Finalmente imprimimos el valor de t con el valor de h anteriormente utilizado
print("El tiempo de caida de una altura de {} es de: {} . Gracias por utilizar el programa.".format(h,t))
#Desarrollado por Pedro Gómez / ID:000396221