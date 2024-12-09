from random import *
intentos = 0
numero_correcto = randint(1,100)

nombre = input("Introduce tu nombre")
print(f"Bienvenido {nombre.lower()}, he pensado un numero del 1 al 100, podras adivinar en cual numero he pensado? \nTienes 8 intentos para poder adivinarlo \nBuena suerte!!")

while intentos < 8:
    elegir = int(input(f"Cual es el numero que he pensado?: "))
    intentos += 1
    if elegir not in range(1,101):
        print("Escoge un numero dentro del rango '(1,100)'")

    elif elegir == numero_correcto:
        print(f"Wow!!! \n felicidades{nombre} has adivinado el numero correcto, te ha costado {intentos} intentos")
        break

    elif elegir > numero_correcto:
        print("Mi numero es más bajo, sigue intentando")
    else:
        print("Mi numero es más grande, sigue intentando")
if elegir != numero_correcto:
    print(f"Lo siento, se han acabado los intentos, el numero en el que pense fue: {numero_correcto}")
