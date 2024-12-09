from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/alejandrosierra/Documents/Py_alt/Dic.txt')
# print(carpeta.read_text())     sirve para ver el contenido

# print(carpeta.name)            sirve para ver el nombre del archivo

#print(carpeta.suffix)           sirve para ver la terminacion de documento

#print(carpeta.stem)             sirve para ver el nombre sin la terminacion

ruta_win = PureWindowsPath(carpeta)
print(ruta_win)

