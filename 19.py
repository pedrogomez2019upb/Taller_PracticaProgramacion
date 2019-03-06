#Distancia entre dos coordenadas
#Primero vamos a importar la libreria math
import math
#Después vamos a solicitar las coordenadas
x1=float(input("Bienvenido! Vamos a ver la distancia entre dos coordenadas. Por favor ingresa el valor de X1: "))
y1=float(input("Por favor ingresa el valor de Y1: "))
x2=float(input("Por favor ingresa el valor de X2: "))
y2=float(input("Por favor ingresa el valor de Y2: "))
#Planteamos la ecuancion de distancia
d= math.sqrt( ((x2-x1)**2)+((y2-y1)**2) )
#Finalmente imprimimos el resultado
print("La distancia entre las coordenadas {},{} y {},{} es : {}. Gracias por utilizar el programa.".format(x1,y1,x2,y2,d))
#Desarrollado por Pedro Gómez / ID:000396221