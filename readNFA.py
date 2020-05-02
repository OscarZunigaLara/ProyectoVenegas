from itertools import combinations

def readTXT(nombreArchivo):
    data = []
    file = open(nombreArchivo, 'r')
    lines = file.readlines()
    for line in lines:
        #quitar { }
        x=line.strip('{}')
        #Separar por()
        y = x.split('(')
        z= ''.join(y)
        m = z.split(')')
        blanc = '|'.join(m)
        node = blanc.split('|')
        for i in node:
            j = i.split(',')
            element = '|'.join(j)
            space=element.strip('|')
            array = space.split('|')
            data.append(array)
    data.pop(-1)
    # for i in range(len(data)):
    #     print (data[i]),
    return data

#Regresa todas las combinaciones de estados posibles.
def generateStates(data):
    states=[]
    newStates = []
    #añade los estados.
    for node in data:
        states.append(node[1])
    #elimina los repetidos
    uniqueStates = set(states)
    #Todas las combinaciones de estados.
    for i in range(1,len(uniqueStates)+1):
        comb = combinations(uniqueStates,i)
        for i in list(comb):
            newStates.append(i)
    return newStates