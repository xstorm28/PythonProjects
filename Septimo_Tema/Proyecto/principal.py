import numeros

def preguntar():
    print('BIENVENIDO A FARMACIAS L')
    while True:
        print('[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica')
        try:
            mi_rubro = input('Eliga su rubro:' ).upper()
            ['P', 'F', 'C'].index(mi_rubro)
        except ValueError:
            print("Elige una opcion valida")
        else:
            break
    numeros.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [Y]/[N]").upper()
            ['Y','N'].index(otro_turno)
        except ValueError:
            print("Elige una opcion valida [Y]/[N]")
        else:
            if otro_turno == 'N':
                print('Gracias por su visita a farmacias L')
                break
inicio()





