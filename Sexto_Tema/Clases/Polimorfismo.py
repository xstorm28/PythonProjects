class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre


    def hablar(self):
        print(self.nombre + " dice muuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice beee")

vaca1 = Vaca('Lola')
oveja1 = Oveja('Salsa')

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)



