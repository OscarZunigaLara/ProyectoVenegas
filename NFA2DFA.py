

class transicion:
    def __init__(self, lectura,estado, destino):
        self.estado = estado
        self.lectura = lectura
        self.destino = destino
    def miTrans(self):
        print("TRANSICION", self)
        print(self.lectura, self.estado, self.destino)
    def miEstado(self):
        return self.estado


def recorrerEstados(estadoInicial, arrTransiciones, aceptacion):
    estadoActual = estadoInicial
    for tra in arrTransiciones:
        #print(tra.miTrans())
        if(estadoActual == tra.estado):
            print(tra.miTrans())
            estadoActual = tra.destino

if __name__ == '__main__':
    print("NFA 2 DFA PYTHON SCRIPT")
    estadoActual= "p"
    estadoAceptacion = "s"
    arrTransiciones = []
    arrTransiciones.append(transicion(0, "p", "p" ))
    arrTransiciones.append(transicion(0, "p", "q" ))
    arrTransiciones.append(transicion(1, "p", "p" ))
    arrTransiciones.append(transicion(0, "q", "r" ))
    arrTransiciones.append(transicion(1, "q", "r"))
    arrTransiciones.append(transicion(0, "r", "s"))
    arrTransiciones.append(transicion(0, "s", "s"))
    arrTransiciones.append(transicion(1, "s", "s"))

    recorrerEstados("p", arrTransiciones, estadoAceptacion)