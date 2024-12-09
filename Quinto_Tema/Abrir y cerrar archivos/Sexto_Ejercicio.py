registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open('Prueba2.txt','a')
linea_con_tabuladores = "\t".join(registro_ultima_sesion) + "\n"
archivo.writelines(linea_con_tabuladores)
archivo = open('Prueba2.txt','r')
print(archivo.read())

