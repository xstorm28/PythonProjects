class Animal:
    def __init__(self,edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print('Esre animal ha nacido')
class Pajaro(Animal):
    pass

piolin = Pajaro(2,'Amarillo')

piolin.nacer()
print(piolin.color)
