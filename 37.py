#Escribe un algoritmo que determine el valor de un pasaje en avión, conociendo la distancia a recorrer, el número de días de estancia, y sabiendo que, si la distancia a recorrer es superior a 1000 Km y el número de días de estancia es superior a 7, la línea aérea le hace un descuento del 15%. (el precio por km. es de $5.000 aunque el mínimo a cobrar siempre es $100.000)
#Primero hay que recibir los valores a analizar 
distancia=float(input("Bienvenido! Vamos a calcular el precio de tu pasaje. Por favor ingrese la distancia a recorrer en Km: "))
dias=float(input("Por favor ingrese el número de dias a viajar: "))
#Vamos a calcular el precio del viaje 
precio=5000*distancia
#Vamos a poner las condicionales necesarias para que pueda sacar el valor del viaje
if distancia>1000 and dias>7:
    #Se aplica el descuento y se imprime
    x=precio-(precio*0.15)
    print("Felicitaciones! Se te va a hacer un descuento del 15% haciendo que tu viaje de ${} cueste ahora ${}. Gracias por viajar con nosotros.".format(precio,x))
else:
    #Se imprime el valor normal del viaje
    print("El valor del viaje total es de: ${} . Gracias por viajar con nosotros.".format(precio))
#Desarrollado por Pedro Gómez / ID:000396221