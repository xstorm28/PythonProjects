class Padre:
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

# Crear una instancia de Hijo
hijo = Hijo()

# Verificar que los atributos heredados y el método sobrescrito funcionan correctamente
print(hijo.color_ojos)           # marrón
print(hijo.tipo_pelo)            # rulos
print(hijo.altura)               # media
print(hijo.voz)                  # grave
print(hijo.deporte_preferido)    # tenis

print(hijo.reir())               # Jajaja
print(hijo.caminar())            # Caminando con pasos largos y rápidos
print(hijo.hobby())              # Juego videojuegos en mi tiempo libre