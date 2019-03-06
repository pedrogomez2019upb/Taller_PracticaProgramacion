#Algoritmo que determine la velocidad final de un objeto con tiempo y aceleración
#Importamos math para la raíz cuadrada
import math
#Primero vamos a obtener los datos de tiempo , aceleración y distancia
vo=float(input("Hola! Vamos a sacar la velocidad final de un movimiento. Por favor ingresa la velocidad inicial: "))
a=float(input("Ingresa la aceleración aplicada: "))
d=float(input("Ingresa la distancia recorrida: "))
#Sacamos la velocidad final
vf=math.sqrt((vo*vo)+(2*a*d))
#Finalmente imprimimos el resultado
print("La velocidad final es de: {} ".format(vf))
#Desarrollado por Pedro Gómez / ID:000396221
