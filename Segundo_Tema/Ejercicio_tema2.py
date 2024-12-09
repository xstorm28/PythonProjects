
nombre = input("Introduce tu nombre")
ventas = input("Introduce el total de ventas que has generado")

ventas = int(ventas)

comision = round (ventas * 13/100)

print (f"Felicidades {nombre}, haz alcanzado la cantidad de ${comision} esto gracias a una comision del 13% sobre tus ventas!!")