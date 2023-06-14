# Pilhas e Filas
# Criando uma Classe Pilha

import random
import array

MAX_PILHA = 52

# *******************************************************
# ***                                                 ***
# *******************************************************
class cPilha:

# *******************************************************
    def __init__(self, n):
        self.vPilha = [0] * n
        self.maxElem = n
        self.topo = 0

# *******************************************************
#     def __str__(self):                                  # Apenas para visualização
#         return f'{self.vPilha}'

# *******************************************************
    def push(self, obj):
        if self.full():
            return False
        self.vPilha[self.topo] = obj
        self.topo += 1
        return True

# *******************************************************
    def pop(self):
        if self.empty():
            return False
        self.topo -= 1
        obj = self.vPilha[self.topo]
        # self.vPilha[self.topo] = 0                       # Apenas para visualização
        return obj

# *******************************************************
    def empty(self):
        return self.topo == 0

# *******************************************************
    def full(self):
        return self.topo == self.maxElem

# *******************************************************
    def size(self):
        return self.topo

    def mostrarTopo(self):
        return self.vPilha[self.topo - 1]

# *******************************************************
    def __str__(self):
        valores = ""
        for i in range(self.topo):                             # Apenas para visualizar
            valores += f'{self.vPilha[i]}\n'
        if valores == "":
            return "Pilha vazia"
        return valores


# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    numElementos = 20

    pilha = cPilha(numElementos)

    print(pilha.size())

    i=100
    while not pilha.full():
        pilha.push(i)
        print(f'++ {i}')
        i += 3

    print(pilha.size())

    print(pilha.mostrarTopo())

    # while not pilha.empty():
    #     i = pilha.pop()
    #     print(f'-- {i}')
    #
    # print(pilha.size())
