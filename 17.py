#Determinar la energía (Jules) con masa mk y velocidad de la luz en m/S
#Primero se recibe la masa del objeto en kg
m=float(input("Hola! Vamos a calcular la energia que tu objeto tiene. Por favor ingresa la masa en kg: "))
#Se plantea la formula para sacar la energía
v_luz=299792458
e=(m*(v_luz*v_luz)/2)
#Finalmente se imprime el resultado
print("El resultado con la velocidad de la luz es de: {} . Gracias por utilizar el programa.".format(e))
#Desarrollado por Pedro Gómez / ID:000396221