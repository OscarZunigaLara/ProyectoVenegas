# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:26:37 2020

@author: Vivian
"""

import readNFA

from itertools import combinations


def readTXT(nombreArchivo):
    data = []
    file = open(nombreArchivo, 'r')
    lines = file.readlines()
    for line in lines:
        # quitar { }
        x = line.strip('{}')
        # Separar por()
        y = x.split('(')
        z = ''.join(y)
        m = z.split(')')
        blanc = '|'.join(m)
        node = blanc.split('|')
        for i in node:
            j = i.split(',')
            element = '|'.join(j)
            space = element.strip('|')
            array = space.split('|')
            data.append(array)
    data.pop(-1)
    # for i in range(len(data)):
    #     print (data[i]),
    return data


# Regresa todas las combinaciones de estados posibles.
def generateStates(data):
    states = []
    newStates = []
    # añade los estados.
    for node in data:
        states.append(node[1])
    # elimina los repetidos
    uniqueStates = set(states)
    # Todas las combinaciones de estados.
    for i in range(1, len(uniqueStates) + 1):
        comb = combinations(uniqueStates, i)
        for i in list(comb):
            newStates.append(i)
    # for i in range(len(newStates)):
    #     print (newStates[i])
    return newStates


def newTansitionsStates(data):
    inp, state = '', ''
    newState = []
    for node in data:
        inp, state = node[0], node[1]
        # print(inp,state)
        for i in data:
            if str(i[0]) == inp and str(i[1]) == state:  # Si la entrada es la misma y el estado es el mismo
                estado1 = i[2]
                estado2 = node[2]
                if i[2] != node[2]:
                    transtate = [estado1, estado2]
                    newNode = [inp, state, transtate]
                    newState.append(newNode)
                    data.remove(i)
    # elimina estados repetidos
    for j in range(len(newState)):
        for node in newState:
            inp, state = node[0], node[1]
            for i in data:
                if str(i[0]) == inp and str(i[1]) == state:
                    data.remove(i)

    # juntar todo. Ay prof si ve esto perdoon. No es mucho pero es trabajo honesto
    for i in data:
        newState.append(i)
    # for i in range(len(newState)):
    #     print (newState[i])
    return newState


def newTransition(states, transitionStates):
    return 0


def main():
    data = readTXT('NFA.txt')
    newStates = generateStates(data)
    newTranStates = newTansitionsStates(data)
    DFA = newTransition(newStates, newTranStates)


main()
