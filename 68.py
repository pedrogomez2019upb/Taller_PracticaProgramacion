#Construya un algoritmo que permita leer una cantidad variable de números indicando finalmente lo siguiente:
#• cuántos números fueron positivos
#• cuántos fueron negativos
#• cuantos fueron pares
#• cuantos fueron impares
#• cuántos fueron múltiplos de ocho
#Primero se recibe la cantidad de números a analizar
x=int(input("Bienvenido! Vamos a analizar los valores de una serie de números . Por favor ingresa el inicio del rango: "))
y=int(input("Ahora ingresa el final del rango: "))
#Ahora vamos a crear un for
for i in range (x,y):
    i=i+1
a=i>0
b=i<0
c=i%2 == 0
d=i%2 != 0
e=i%8 == 0
print(a,b,c,d,e)