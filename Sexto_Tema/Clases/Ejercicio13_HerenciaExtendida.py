class Padre:
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre:
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    pass

hija = Hija()
hija.reir()       # Utiliza el método reir de Padre
hija.trabajar()   # Utiliza el método trabajar de Madre