archivo = open('Prueba1.txt', 'r') # cambiar primero a w para modificarlo, luego a r para verlo
# archivo.write('Esto es nuevo):')     # despues aplico esto para modificar
print(archivo.read())



archivo.close()