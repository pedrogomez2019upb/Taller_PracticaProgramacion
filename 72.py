#Escribe un algoritmo que convierta un número decimal a binario
#Primero recibimos el valor del decimal
dec=int(input("Bienvenido! Vamos a convertir el número a decimal. Por favor ingresa el número a convertir: "))
#Utlizamos la propiedad bin,oct y hex para convertirlo de una vez
print("El valor decimal de {} es: ".format(dec))
print(bin(dec),"en binario.")
print(oct(dec),"en octal.")
print(hex(dec),"en hexadecimal.")
#Desarrollado por Pedro Gómez / ID:000396221