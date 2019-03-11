#Determinar si una serie de tres números están aumentando
#Primero vamos a recibir los valroes a analizar
n1=float(input("Bienvenido! Vamos a analizar unos números. Por favor ingrese el primer valor: "))
n2=float(input("Por favor ingresa el segundo valor: "))
n3=float(input("Ingresa el tercer valor: "))
#Creamos unas condicionales if y then para determinar el valor
if n1<n2<n3:
    print("La serie de números ingresados van aumentando.")
else:
    if n1>n2>n3:
        print("La sere de números ingresado van disminuyendo.")
    else:
        print("No hay ningun cambio en la secuencia.")
#Desarrollado por Pedro Gómez / ID:000396221