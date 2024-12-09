capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinar = list(zip(capitales,paises))
for capitales, paises in combinar:
    print(f'La capital de {paises} es {capitales}')
