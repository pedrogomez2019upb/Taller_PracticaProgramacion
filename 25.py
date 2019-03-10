#Intercalar un número de 4 digitos
#Primero debemos recibir el valor a evaluar
a=int(input("Bienvenido! Vamos a intercalar un número de 4 digitos. Por favor digita el número. "))
#Ahora vamos a hacer los respectivos procedimientos matemáticos
#1.Sacamos el primer valor
b=int(a/1000)
#2.Sacamos el residuo a otro valor
c=a-(b*1000)
#Así sucesivamente para poder sacar los valores indivisualmente
d=int(c/100)
e=c-(d*100)
f=int(e/10)
g=e-(f*10)
#Finalmente imprimimos el valor
print("El valor intercalado de {} es: {}{}{}{} . Gracias por utilizar el programa.".format(a,g,f,d,b))
#Desarrollado por Pedro Gómez / ID:000396221