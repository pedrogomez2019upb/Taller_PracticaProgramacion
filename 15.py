#Distancia recorrida por un objeto luego de un tiempo, aceleración y velocidad inicial
#Primero nos toca conseguir los valores necesarios para hacer el procedimiento matemático.
t=float(input("Hola! Vamos a sacar la distancia que recorre un objeto en una línea recta. Por favor ingresa el tiempo recorrido: "))
a=float(input("Ahora ingresa la aceleración: "))
vo=float(input("Ingresa por favor la velocidad inicial: "))
#Vamos a declarar una variable que haga el procedimiento matemático
d=(vo*t)+(0.5*a*(t*t))
#Finalmente imprimimos el valor de la distancia
print("La distancia recorrida fue de: {} . Gracias por utilizar el programa.".format(d))
#Desarrollado por Pedro Gómez / ID:000396221
