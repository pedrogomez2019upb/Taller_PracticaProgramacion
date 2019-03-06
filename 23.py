#Segundos a formato hh:mm:ss
#Primero vamos a recibir los segundos a convertir
seg=int(input("Bienvenido! Vamos a convertir los segundos a formato HH:MM:SS . Por favor ingresa los segundos a analizar: "))
#Ahora vamos a plantear las ecuaciones para las respectivas conversiones
minutos = seg / 60
segundos_res=int(seg%60)
horas = int (minutos/60)
minutos_res=int(minutos%60)
#Finalmente imprimimos los valores conseguidos
print ("El formato de segundos a hh:mm:ss es {}:{}:{} .".format(horas,minutos_res,segundos_res))
#Desarrollado por Pedro Gómez / ID:000396221
