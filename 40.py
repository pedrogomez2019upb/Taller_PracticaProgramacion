#Usuario y contraseña
#Para este ejercicio vamos a utilizar como usuario "carlos" y contraseña "1234"
#Primero solicitamos las variables
user=input("Bienvenido al sistema! Ingresa tu usuario: ")
password=input("Ingresa tu contraseña: ")
#ponemos condicionales if y then para que compruebe las credenciales
name=("carlos")
codigo="1234"
if user==name and password==codigo:
    print("Estás logueado! Gracias por utilizar nuestro sistema.")
else:
    print("Lo siento! Algo ingresaste mal . Vuelve a intentarlo.")
#Desarrollado por Pedro Gómeze / ID:000396221