import re

clave = input('Clave: ')

patron = r'\D{1}\w{7}'

checar = re.search(patron , clave)

print(checar)