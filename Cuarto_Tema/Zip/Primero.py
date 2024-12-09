nombres = ["juan", "Roberto", "Ana", "Sofia"]
edad = [12,37,25,12]

combinar = list(zip(nombres,edad))
for nombres, edad in combinar:
    print(f'{nombres} tiene {edad} años')
