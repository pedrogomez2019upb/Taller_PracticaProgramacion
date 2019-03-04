#Algoritmo que calcule el área de un hexágono
#Primero vamos a pedir el perímetro y el apotema para poder hacer el procedimiento matemático
p=float(input("Bienvenido! Vamos a calcular el área de un hexagono. Por favor ingresa el perímetro: "))
ap=float(input("Ahora por favor ingresa el valor del apotema: "))
#A continuación vamos a declarar una variable "x" que establesca el procedimiento matemático para sacar el área de un hexagono
x = 0.5 * p * ap
#Finalmente imprimimos el resultado con un mensaje y con las variables anteriormente establecidas.
print("El área de un hexágono con perímetro de {} y apotema de {} es de: {} . Muchas gracias por utilizar el programa.".format(p,ap,x))
#Desarrollado por Pedro Gómez / ID:000396221
