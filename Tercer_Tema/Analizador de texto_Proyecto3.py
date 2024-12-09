texto = input("Por favor, introduce el texto que deseas analizar")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())

letras.append(input("Ingresa la segunda letra: ").lower())

letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS EN EL TEXTO")
can_letras1 = texto.count(letras[0])
can_letras2 = texto.count(letras[1])
can_letras3 = texto.count(letras[2])

print(f"se ha encntrado la letra '{letras[0]}' en {can_letras1} ocasiones ")
print(f"se ha encntrado la letra '{letras[1]}' en {can_letras2} ocasiones ")
print(f"se ha encntrado la letra '{letras[2]}' en {can_letras3} ocasiones ")

print("\n")
print("CANTIDAD DE PALABRAS EN EL TEXTO")

palabras = texto.split()
print(f"Hemos encontrado la cantidad de '{len(palabras)}' palabras")


print("\n")
print("LETRAS DE INICIO Y DE FIN ")
letra_i = texto[0]
letra_f = texto[-1]

print(f"La letra inicial es ´{letra_i}´ y la letra final es '{letra_f}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
invertido = ' '.join(palabras)
print(f"El texto invertido es: {invertido}")

print("\n")
print("BUSCAR PALABRA PYTHON")
buscar = 'python' in texto
dic = {True:'si', False:'no'}

print(f"La palabra 'Python' {dic[buscar]} se encuentra en el texto")








