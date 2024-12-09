class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

lego = Arquero()
mercurio = Mago()
batman = Samurai()

personajes = [lego,mercurio,batman]

for personaje in personajes:
    personaje.atacar()
