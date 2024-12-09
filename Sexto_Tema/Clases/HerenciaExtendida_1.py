class Animal:
    def __init__(self,edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print('Esre animal ha nacido')
    def hablar(self):
        print('Este animal ha nacido ')
class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

        
    def hablar(self):
        print('Pio')
    def volar(self,metros):
        print(f'El pajaro vuela {metros} metros')



piolin = Pajaro(2,'Amarillo')
piolin.volar(100)


