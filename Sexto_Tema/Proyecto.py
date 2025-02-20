class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance


    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} \n Balance de cuenta {self.numero_cuenta} : ${self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito realizado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")

def crear_cliente():
    nombre_cl = input("Ingrese su nombre:")
    apellido_cl = input("Ingrese su apellido")
    numero_cl = input("Ingrese su numero de cuenta:  ")
    cliente = Cliente(nombre_cl,apellido_cl,numero_cl)
    return cliente
def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != "S":
        print('Elige: Depositar (D) , Retirar (R), Salir (S)')
        opcion = input()
        if opcion == "d":
            monto_dep= int(input("Monto a depositar"))
            mi_cliente.depositar(monto_dep)
        elif opcion == "r":
            monto_ret = int(input("Monto a Retirar"))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    print("Gracias por operar en Banco Python")

inicio()









