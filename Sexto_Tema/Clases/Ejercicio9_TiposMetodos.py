class Personaje:
    def __init__(self, cantidad_flechas):

        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print(f"Flecha lanzada. Flechas restantes: {self.cantidad_flechas}")
        else:
            print("No quedan flechas para lanzar.")



mi_personaje = Personaje(5)

mi_personaje.lanzar_flecha()  # Flecha lanzada. Flechas restantes: 4
mi_personaje.lanzar_flecha()  # Flecha lanzada. Flechas restantes: 3
mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()
mi_personaje.lanzar_flecha()