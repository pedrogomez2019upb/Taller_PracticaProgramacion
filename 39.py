#Programa que pueda resolver funciones cuadráticas
#Primero nos toca importar la libreria cmath la cual es
#para procedimientos matemáticos complejos
import cmath
#Ya hecho esto , vamos a solicitar los valores a evaluar.
a=float(input("Bienvenido! Vamos a resolver una función cuadrática. Por favor ingresa el valor de a: "))
b=float(input("Por favor ingresa el valor b: "))
c=float(input("Por favor ingresa el valor c: "))
#Ahora calculamos la discriminante
d = (b**2)-(4*a*c)
#Buscamos las dos soluciones
solucion1=(-b-cmath.sqrt(d))/(2*a)
solucion2=(-b+cmath.sqrt(d))/(2*a)
#Finalmente imprimimos los resultados
print("La solución para esta funcion es {} y {} . Gracias por utilizar el programa.".format(solucion1,solucion2))
#Desarrollado por Pedro Gómez / ID:000396221