class estado:
    def __init__(self, estado):
        self.estado = estado
        self.transiciones = []

    def agregarTransiciones(self, transAgregar):
        self.transiciones.append(transAgregar)

    def miEstado(self):
        print("ESTADO :")
        print(self.estado)
    def misTransiciones(self):
        print("TRANSICIONES DE " + self.estado)
        for i in self.transiciones:
            print(i.miTrans())

class transicion:
    def __init__(self, lectura, destino):
        self.lectura = lectura
        self.destino = destino
    def miTrans(self):
        print("TRANSICION")
        print(self.lectura)
        print(self.destino.estado)


def recorrer():



if __name__ == '__main__':
    print("NFA 2 DFA PYTHON SCRIPT")
    e1 = estado("e1")
    transi1 = transicion(0, e1)

    e1.agregarTransiciones(transi1)

    e1.misTransiciones()

    #e1.misTransiciones()
    e2 = estado("e2")
    e2.agregarTransiciones(transi1)

    e2.misTransiciones()

