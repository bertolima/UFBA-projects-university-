import random
import array


class Pilha:


    def __init__(self, n):
        self.__vPilha     = [0] * n 
        self.__maxElem    = n 
        self.__topo       = 0
    
    @property
    def maxElem(self):
        return self.__maxElem
    @maxElem.setter
    def maxElem(self, value):
        self.__maxElem = value
    
    @property
    def topo(self):
        return self.__topo
    @topo.setter
    def topo(self, value):
        self.__topo = value
        
    def getElemTopo(self):
        return self.__vPilha[self.__topo - 1]
    def push(self, k): # Empilha

        if self.full():
            return
        self.__vPilha[self.topo] = k
        self.__topo += 1

        return

    def pop(self):

        if self.empty():
            return

        self.__topo -= 1
        return self.__vPilha[self.topo]


    def empty(self):
        return self.__topo == 0


    def full(self):
        return self.__topo == self.__maxElem


    def size(self):
        return self.__topo
    