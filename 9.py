#Algoritmo que muestre el valor bruto y el iva aplicado.
#Primero que vamos a hacer es recibir el valor del producto.
x=float(input("Bienvenido! Vamos a sacarle el valor final de un producto. Por favor ingresa el valor: "))
#Se hace una variable que le aplique el iva al producto
iva=x*0.19
#Se hace otra variable que le sume el iva del producto al valor final
iva_aplicado= x + iva
#Finalmente se imprime el resultado.
print("El valor final de {} con el IVA del 19% es de: {} . Gracias por utilizar el programa.".format(x,iva_aplicado))
#Desarrollado por Pedro Gómez / ID:000396221
