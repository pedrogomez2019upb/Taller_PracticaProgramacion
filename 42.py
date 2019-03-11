#Contar cuantos dígitos tiene un número
#Primero nos toca crear un contador que empiece desde cero
contador=0
#Recibimos el valor a analizar
a=int(input("Bienvenido! Vamos a analizar los digitos de un número. Por favor ingresa el número a analizar: "))
#Creamos un if para que solo cuente los números menores a 100000
if a < 100000:
    print("El número total de digitos es: ",len(str(abs(a))))
else:
    print("Lo siento! Solo puedo analizar números menores a 100000.")
#Desarrollado por Pedro Gómez / ID:000396221