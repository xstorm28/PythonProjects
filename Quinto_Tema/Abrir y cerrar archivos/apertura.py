archivo = open('Prueba2.txt', 'w')

lista = ['Hola','Mundo','aqui','estoy']

for p in lista:
    archivo.writelines(p + '\n')


archivo.close()