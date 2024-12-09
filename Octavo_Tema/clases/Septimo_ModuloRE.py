import re

texto = 'No atendemos los lunes por la tarde'

buscar = re.search(r'lunes|martes', texto)

print(buscar)