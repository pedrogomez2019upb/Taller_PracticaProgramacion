#Escribe un algoritmo que convierta un número binario a hexadecimal
#Primero recibimos el valor a analizar a hexadecimal
binario = input("Hola! Vamos a convertir el número a hexadecimal. Por favor ingresa el número: ")
#Creamos la formula para hexadecimal
temp=int(binario, 2)
#Creamos otra variable para convetirla a hexadecimal
hexadecimal=hex(temp)
#Finalmente imprimimos el valor obtenido
print("El valor convertido a hexadecimal seria de : {} . Gracias por utilizar el programa.".format(hexadecimal))
#Desarrollado por Pedro Gómez / ID:000396221