#Dada una cantidad de dinero , determinar cual es la menor cantidad de billetes que puede sacar
#Primero vamos a solicitar la cantidad de dinero a evaluar.
moneyhoney=int(input("Bienvenido! Vamos a calcular la menor cantidad de billetes que un cajero puede retirar. Por favor ingresa la cantidad de dinero a retirar: "))
#Vamos a declarar unas variables para que retiren el dinero en la misma cantidad de biletes de tal denominacion
m50=moneyhoney/50000
m20=moneyhoney/20000
m10=moneyhoney/10000
m5=moneyhoney/5000
m2=moneyhoney/2000
m1=moneyhoney
#Finalmente se imprime el valor de los billetes a sacar en tal denominación de billetes
print("El valor de {} se puede sacar en {} billetes de 50 , {} billetes de 20 , {} billetes de 10 , {} billetes de 5, {} billetes de 2 . Gracias por utilizar el programa.".format(moneyhoney,m50,m20,m10,m5,m2))
#Desarrollado por Pedro Gómez / ID:000396221
