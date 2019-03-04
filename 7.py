#Responder con la parte entera y decimal de un número.
#Primero debemos recibir el valor como una entrada float.
a=float(input("Bienvenido! Vamos a sacarle la parte entera y decimal de un número. Por favor ingresa el número: "))
#Vamos a crear dos variables que definan "a" como parte entera y decimal
x= int(a)
#Despuúes se hace un procedimiento matemático para que solo me tire el residuo.
y=a-x
#Finalmente vamos a imprimir los resultados hechos previamente.
print("La parte entera de {} es {} , y su parte decimal es {} . Gracias por utilizar el prorama.".format(a,x,y))
#Desarrollado por Pedro Gómez / ID:00396221