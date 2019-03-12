#"Escribe un algoritmo que convierta un número binario a octal"
#Primero recibimos el número binario
binario=input("Hola! Vamos a convertir de binario a octal. Por favor ingresa el número binario: ")
#Ahora creamos la formula para octal
temp=int(binario, 2)
#Convertimos el valor a octal
octal=oct(temp)
#Finalmente imprimimos el valor
print("El valor convertido a octal seria de: {} . Gracias por utilizar el programa.".format(octal))
#Desarrollado por Pedro Gómez / ID:000396221