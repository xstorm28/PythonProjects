import re
import time
import os
import datetime
from pathlib import Path
import math
inicio = time.time()
ruta = '/Users/alejandrosierra/Desktop/mi_gran_directorio'

mi_patron =r'N\D{3}-\d{5}'
hoy = datetime.date.today()
num_encontrados = []
arc_encontrados = []

def buscar_numero(archivo,patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron,archivo):
        return re.search(patron,archivo)
    else:
        return''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), mi_patron)
            if resultado != '':
                num_encontrados.append((resultado.group()))
                arc_encontrados.append(a.tittle())

def mostrar_todo():
    indice = 0
    print('=' * 50)
    print(f'Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\t NO.SERIE ')
    print('=======\t\t\t =========')
    for a in arc_encontrados:
        print(f'{a}\t{num_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'NUMEROS ENCONTRADOS: {len(num_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('=' * 50)

crear_listas()
mostrar_todo()









