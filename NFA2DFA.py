import readNFA
class transicion:
    def __init__(self, lectura,estado, destino):
        self.estado = estado
        self.lectura = lectura
        self.destino = destino
    def miTrans(self):
        #print("TRANSICION", self.lectura, self.estado, self.destino)
        return (self.lectura, self.estado, self.destino)
    def miEstado(self):
        return self.estado

def recorrerEstados(estadoInicial, arrTransiciones):
    estadoActual = estadoInicial
    arrParaNetworkX = []
    for i in arrTransiciones:
        if (i.estado in arrParaNetworkX):
            pass
        else:
            arrParaNetworkX.append(i.estado)
        if (i.destino in arrParaNetworkX):
            pass
        else:
            arrParaNetworkX.append(i.destino)

    print(arrParaNetworkX)
    for estado in arrParaNetworkX:
        print(estado)
        for x in arrTransiciones:
            if ((x.estado) == estado):
                ceros = 0
                unos = 0
                print(ceros  , unos  )
                print(x.miTrans())

if __name__ == '__main__':
    print("NFA 2 DFA PYTHON SCRIPT")
    estadoActual= "p"
    estadoAceptacion = "s"
    arrTransiciones = []

    txt = readNFA.readTXT("NFA.txt")

    for tr in txt:
        arrTransiciones.append(transicion(tr[0], tr[1], tr[2]))

    recorrerEstados("p", arrTransiciones)