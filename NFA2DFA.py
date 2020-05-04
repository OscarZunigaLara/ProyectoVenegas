import readNFA
import NFA2DFAVIVS
import copy

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




def arrNetwork(arrTransiciones):
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
    return  arrParaNetworkX

def dfaGen(arrTransiciones):
    copyTrans = []
    for n in arrTransiciones:
        copyTrans.append(transicion(n.lectura, n.estado,n.destino))

    arrNetwork1 = arrNetwork(arrTransiciones)

    for n in arrTransiciones:
        print(n.miTrans())
    print("//////////////////////")
    indeter = []

    for n in arrNetwork1:
        print(n)
        sum = 0
        for h in arrTransiciones:
            if h.estado == n:
                sum = sum+1
        if (sum > 2):
            indeter.append(n)

    print("indeter: ",indeter)
    arrNet2 = []
    for n in indeter:
        for h in arrNetwork1:
            if n == h:
                pass
            else:
                arrNet2.append([n,h])

    for n in arrNet2:
        arrNetwork1.append(n)

    newARRTRA= []


    for x in arrNetwork1:
        sumCERO= 0
        sumUNO = 1
        for y in arrTransiciones:
            if(y.estado == x):
                print(x, "   ", y.miTrans(), sumCERO, sumUNO)
                newTrans = transicion(y.lectura, y.estado, y.destino)
                if (y.lectura == '0'):
                    sumCERO +=1
                if y.lectura == '1':
                    sumUNO +=1

    for x in arrNetwork1:
        sumCERO= 0
        sumUNO = 1
        for y in arrTransiciones:
            if(y.destino == x):
                print(x, "   ", y.miTrans(), sumCERO, sumUNO)
                newTrans = transicion(y.lectura, y.estado, y.destino)

                if (y.lectura == '0'):
                    sumCERO +=1
                if y.lectura == '1':
                    sumUNO +=1

    print(arrNetwork1)
    print("//////////////////////")
    for n in arrTransiciones:
        print(n.miTrans())
    print("//////////////////////")

    for n in newARRTRA:
        print(n.miTrans())
'''

        for n in copyTrans:
        for h in copyTrans:
            if (h.lectura == '0'):
                arrTransiciones.append(transicion('0', h.destino, h.estado))
        for h in copyTrans:
            if (h.lectura == '1'):
                arrTransiciones.append(transicion('1', h.destino, h.estado))

    

    ("//////////////////////")

   


    newaa = []
    for x in arrParaNetworkX:
        if (len(x)> 1):
            for y in arrParaNetworkX:
                if y in x:
                    pass
                elif y == x:
                    pass
                else:
                    newEs = x.copy()
                    newEs.append(y)
                    newaa.append(newEs)
    for x in newaa:
        arrParaNetworkX.append(x)
    for j in arrParaNetworkX:
        if (len(j) > 1):
            for n in arrTransiciones:
                if (n.destino in j):
                    # print(n.miTrans())
                    n.destino = j
                if (n.estado in j):
                    # print(n.miTrans())
                    if (j[0] == n.estado):
                        pass
                    else:
                        n.estado = j
                    pass
    
'''

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
    data = NFA2DFAVIVS.readTXT('NFA.txt')
    newStates = NFA2DFAVIVS.generateStates(data)
    newTranStates = NFA2DFAVIVS.newTansitionsStates(data)
    DFA = NFA2DFAVIVS.newTransition(newStates, newTranStates)



def miMain():
    print("NFA 2 DFA PYTHON SCRIPT")
    arrTransiciones = []
    txt = readNFA.readTXT("newNFA.txt")
    for tr in txt:
        arrTransiciones.append(transicion(tr[0], tr[1], tr[2]))
    dfaGen(arrTransiciones)

if __name__ == '__main__':
    miMain()


