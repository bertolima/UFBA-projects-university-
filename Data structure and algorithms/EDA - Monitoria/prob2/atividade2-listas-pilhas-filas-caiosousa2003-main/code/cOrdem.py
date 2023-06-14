# ############################################################
# Classe que implementa uma Fila Circular
# Utilizada para implementar a ordem no jogo
# ############################################################

import cJogador
import random as rd
from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
class cOrdem():
    
    def __init__(self):
        self._inicio     = None
        self._fim        = None
        self._numElems   = 0

# *******************************************************
    def size(self):
        return self._numElems

# *******************************************************
    def enfileirar(self, n):

        novoNo = n

        if self.empty():
            self._inicio = novoNo
            self._fim    = novoNo
            novoNo.setProx(novoNo)
            self._numElems += 1
        else:
            novoNo.setProx(self._inicio)
            self._fim.setProx(novoNo)
            self._fim = novoNo
            self._numElems += 1

# *******************************************************
    def desenfileirar(self):

        if self.empty():
            return None

        noCor = self._inicio

        if noCor == self._fim:
            self._inicio = None
            self._fim = None
            self._numElems -= 1
        else:
            self._inicio = noCor.getProx()
            self._fim.setProx(self._inicio)
            self._numElems -= 1

        return noCor

# *******************************************************
    def empty(self):
        return self._inicio == None
    
# *******************************************************    
    def __str__(self):
        outStr = ''
        
        if self.empty():
            outStr += "=====================\n"
            outStr += "|   FILA   VAZIA    |\n"
            outStr += "=====================\n"
        else:
            filaTemp = cOrdem()
            outStr += '[ '
            while(not self.empty()):
                i = self.desenfileirar()
                filaTemp.enfileirar(i)
                outStr += f'| {i.getName()} | '
            while (not filaTemp.empty()):
                i = filaTemp.desenfileirar()
                self.enfileirar(i)
            outStr += ']'
        
        return outStr

# *******************************************************    
    def proxTurno(self):
        i = self.desenfileirar()
        self.enfileirar(i)
        return i

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    rd.seed(int(datetime.now().strftime('%H%M%S')))
    
    qntdd = 4

    fila = cOrdem()
    
    ordem = rd.sample(range(1,5), 4)
    for i in ordem:
        nome = f'Jogador {i}'
        JogadorX = cJogador.cJogador(nome)
        fila.enfileirar(JogadorX)
    
    print(fila.size())
    print(fila)
    jogador = fila.proxTurno()
    print(jogador.getName())
    print(fila)
        