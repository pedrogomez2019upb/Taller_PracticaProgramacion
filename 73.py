#Escribe un algoritmo que convierta un número binario a decimal
#Contador para decimal
decimal=0
#Primero vamos a recibir el número binario
binario=input("Hola! Vamos a convertir un binario a decimal: Por favor ingresa el binario: ")
#Utilizamos un for para hacer el proceso
for digito in binario:
    #Creamos la formula de decimal
    decimal=decimal*2 + int(digito) #Convertimos el digito a integro
#Finalmente imprimimos el resultado
print("La conversión da: {} . Gracias por utilizar el programa.".format(decimal))
#Desarrollado por Pedro Gómez / ID:000396221
