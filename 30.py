#Valor total de una venta
#Primero vamos a pedirle el valor de la compra neta
a=float(input("Bienvenido ! Vamos a aplicarle el IVA a tu compra. Por favor ingresa el valor total de la compra: "))
#Vamos a poner la condicional para que haga el descuento
if a > 150000:
    x=a*0.05
    y=a-x
    print("Felicitaciones! Tu venta es mayor de 150000 , por lo que se le aplicará un descuento del 5%")
    #Se le aplica el IVA
    b=y*0.19
    c=y+b
    #Se imprime el valor
    print("La venta con valor ${} te queda en ${} y con el iva final te queda en ${} . Gracias por utilizar el programa.".format(a,y,c))
else:
    #Se aplica el IVA normal al precio bruto
    q=a*0.19
    w=a+q
    #Se imprime el valor 
    print("El valor de la venta de ${} te queda en ${} con el IVA aplicado. Muchas gracias por utilizar el programa.".format(a,w))
#Desarrollado por Pedro Gómez / ID:000396221
