# ############################################################
# Classe que implementa uma Pilha
# Utilizada para criar um deck de cartas (Agrupamento de Cartas Embaralhadas (ACE))
# e o morto (Agrupamento de Cartas Emparelhadas)
# ############################################################

import cCarta

# *******************************************************
# ***                                                 ***
# *******************************************************
class cMonte:

# *******************************************************
    def __init__(self, n):
        self.vPilha     = [0] * n 
        self.maxElem    = n 
        self.topo       = 0

# *******************************************************
    def __str__(self):
        outStr = ''
        
        if self.empty():
            outStr += "=====================\n"
            outStr += "|   PILHA   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            pilhaTemp = cMonte(self.topo)
            outStr += '[ '
            while(not self.empty()):
                i = self.pop()
                pilhaTemp.push(i)
                outStr += f'| {i.getDado()} | '
            while (not pilhaTemp.empty()):
                i = pilhaTemp.pop()
                self.push(i)
            outStr += ']'
        
        return outStr
            
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

# *******************************************************
    def empty(self):
        return self.topo == 0

# *******************************************************
    def full(self):
        return self.topo == self.maxElem

# *******************************************************
    def size(self):
        return self.topo

# *******************************************************
    def getTopo(self):
        return self.vPilha[self.topo-1]
    
# *******************************************************
    def getUltPar(self):
        topo = self.pop()
        par = f'[ {self.getTopo().getDado()} {topo.getDado()} ]'
        self.push(topo)
        return par

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    pilha = cMonte(10)
    
    i = 1
        
    while(not pilha.full()):
        carta = cCarta.cCarta(i, 'Espadas')
        pilha.push(carta)
        print(f'++ {carta.getDado()}')
        i += 1

    print(pilha.getTopo().getDado())
    print(pilha.getUltPar())
    print(pilha)
    
    while(not pilha.empty()):
        i = pilha.pop()
        print(f'-- {i.getDado()}')