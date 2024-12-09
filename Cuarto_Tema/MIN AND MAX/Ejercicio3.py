diccionario_edades = {
    "Carlos": 55, "María": 42, "Mabel": 78, "José": 44, "Lucas": 24,
    "Rocío": 35, "Sebastián": 19, "Catalina": 2, "Darío": 49
}

edad_minima = min(diccionario_edades.values())

ultimo_nombre = max(diccionario_edades.keys())

print(f"La edad mínima es: {edad_minima}")
print(f"El último nombre en orden alfabético es: {ultimo_nombre}")