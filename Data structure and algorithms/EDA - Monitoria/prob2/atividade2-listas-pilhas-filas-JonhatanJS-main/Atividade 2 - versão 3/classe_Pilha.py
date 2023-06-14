# Pilhas e Filas
# Criando uma Classe Pilha

import random
import array

MAX_PILHA = 20

# *******************************************************
# ***                                                 ***
# *******************************************************
class cPilha:

# *******************************************************
    def __init__(self, n=52):
        self.vPilha     = [0] * n 
        self.maxElem    = n 
        self.topo       = 0
        return


# *******************************************************
    def push(self, k): # Empilha

        if self.full():
            return

        self.vPilha[self.topo] = k
        self.topo += 1

        return

# *******************************************************
    def pop(self):

        if self.empty():
            return

        self.topo -= 1
        return self.vPilha[self.topo]
    def getTopo(self):
        return self.vPilha[self.topo]
# *******************************************************
    def empty(self):
        return self.topo == 0

# *******************************************************
    def full(self):
        return self.topo == self.maxElem

# *******************************************************
    def size(self):
        return self.topo

    def __str__(self):
        outStr = ""
        if self.empty():
            outStr += "Pilha Vazia"
        else:
            for i in range(self.topo-1, -1, -1):
                if i == self.topo - 1:
                    outStr += f"({str(self.vPilha[i])}) "  # Adiciona parênteses ao redor do item do topo
                else:
                    outStr += f"{str(self.vPilha[i])}, "  # Separador por vírgula entre os itens
        return outStr[:-2]

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    numElementos = 10

    pilha = cPilha(numElementos)

    i=100
    while(not pilha.full()):
        pilha.push(i)
        print(f'++ {i}')
        i += 3

    while(not pilha.empty()):
        i = pilha.pop()
        print(f'-- {i}')
