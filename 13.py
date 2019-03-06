#Escribe un algoritmo que intercale dos variables 
#Primero vamos a recibir las dos variables que vamos a intercalar como enteros.
a=int(input("Bienvenido! Vamos a intercalar dos números enteros que tu ingreses. Por favor ingresa el primer número: "))
b=int(input("Ahora ingresa el segundo valor: "))
#Imprimimos los dos valores principales
print("Los números originales son: {} y {} .".format(a,b))
#Ahora vamos a hacer el intercambio mediante tres procedimientos matemáticos y cambio de variable
a += b
b = a -b
a -= b
#Finalmente imprimimos el resultados con un mensaje de los intercalados
print("El número A ahora es : {} y El número B ahora es: {}. Muchas gracias por utilizar el programa.".format(a,b))
#Desarrollado por Pedro Gómez / ID:000396221

 