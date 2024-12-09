class Vertebrado:
    vertebrado = True


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Ave(Vertebrado):
    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")


class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    tiene_pico = True

ornitorrinco = Ornitorrinco()
print(f"Ornitorrinco tiene pico: {ornitorrinco.tiene_pico}")
print(f"Ornitorrinco es vertebrado: {ornitorrinco.vertebrado}")
print(f"Ornitorrinco es venenoso: {ornitorrinco.venenoso}")

ornitorrinco.nadar()          # Nadando
ornitorrinco.caminar()        # Caminando
ornitorrinco.amamantar()      # Amamantando crías
ornitorrinco.poner_huevos()   # Poniendo huevos (de Ave)