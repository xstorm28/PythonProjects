class Pajaro:
    alas = True

    def __init__(self,color, especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print('Pio, pio, mi color es {}'.format(self.color))
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()
    def pintar_negro(self):
        self.color = 'Negro'
        print(f'Ahora el pajaro es {self.color}')
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
    @staticmethod
    def mirar():
        print("El pajaro mira")
Pajaro.mirar()
Pajaro.poner_huevos(5)



#piolin = Pajaro('Amarillo', 'Canario')






