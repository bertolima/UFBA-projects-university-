# ############################################################
# Classe nó de uma Fila Circular
# Utilizada para implementar o jogador que armazena o nome, sua mão e sua ordem no jogo
# ############################################################

import cMao
import cCarta
import random as rd
from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
class cJogador():
    
    def __init__(self, nome = 'Jogador'):
        self.__nome__ = nome
        self.__mao__ = cMao.cMao()
        self.__desc__ = None
        self.__status__ = None
        self.__prox__ = None
        
    def getMao(self):
        return self.__mao__
    
    def getDesc(self):
        return self.__desc__
    
    def getName(self):
        return self.__nome__
    
    def setStatus(self):
        if self.__mao__.isempty():
            self.__status__ = f'{self.__nome__} descartou todas cartas!'
        else:
            self.__status__ = f'{self.__nome__}: {self.__mao__}'
    
        return self.__status__
    
    def setMico(self):
        self.__status__ = f'{self.__nome__} perdeu! Ele está com o MICO!'
        
    def getStatus(self):
        return self.__status__
    
    def setProx(self, prox):
        if type(prox) == cJogador:
            self.__prox__ = prox
        else:
            self.__prox__ = None
            
    def getProx(self):
        return self.__prox__
    
    def descartarPares(self):
        self.__desc__ = self.__mao__.verificarPares()
        return True

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':
    Jogador1 = cJogador('Jogador 1')
    rd.seed(int(datetime.now().strftime('%H%M%S')))
    print(Jogador1.getMao())
    
    for i in range(10):
      carta = cCarta.cCarta(rd.randint(1,10), 'Ouros')
      Jogador1.getMao().setCarta(carta)
    
    print(f'{Jogador1.getName()}: {Jogador1.getMao()}')
    
    Jogador1.descartarPares()
    
    print(Jogador1.setStatus())
    print(f'Cartas Descartadas: {Jogador1.getDesc()}')
    
    