import readNFA
import NFA2DFAVIVS
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

def recorrerEstados(arrTransiciones):
    arrTranOriginal = arrTransiciones
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

    for estado in arrParaNetworkX:
        #print("ESTADO:    ", estado)
        newState0 = []
        newState1 = []
        for x in arrTransiciones:
            if ((x.estado) == estado):
                if (x.lectura == '0'):
                    newState0.append(x.destino)
                    if (len(newState0) > 1):
                        arrParaNetworkX.append(newState0)
                if (x.lectura == '1'):
                    newState1.append(x.destino)
                    if (len(newState1) > 1):
                        arrParaNetworkX.append(newState1)


                #print(x.miTrans(), arrParaNetworkX)
    print(arrParaNetworkX)

    for n in arrTransiciones:
        print(n.miTrans())

    print("///////////////////////////////")
    for j in arrParaNetworkX:
        if (len(j)>1):
            for n in arrTransiciones:
                if (n.destino in j):
                    #print(n.miTrans())
                    n.destino = j
                if (n.estado in j):
                    #print(n.miTrans())
                    if (j[0] == n.estado):
                        pass
                    else:
                        n.estado = j
                    pass
    print(arrParaNetworkX)
    for n in arrTransiciones:
        print(n.miTrans())

def vivMain():
    data = NFA2DFAVIVS.readTXT('newNFA.txt')
    newStates = NFA2DFAVIVS.generateStates(data)
    newTranStates = NFA2DFAVIVS.newTansitionsStates(data)
    DFA = NFA2DFAVIVS.newTransition(newStates, newTranStates)



def miMain():
    print("NFA 2 DFA PYTHON SCRIPT")
    arrTransiciones = []
    txt = readNFA.readTXT("NFA.txt")
    for tr in txt:
        arrTransiciones.append(transicion(tr[0], tr[1], tr[2]))
    recorrerEstados(arrTransiciones)

if __name__ == '__main__':
    miMain()


