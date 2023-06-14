# ############################################################
# Classe que implementa uma Lista Duplamente Encadeada - LDE
# Utilizada para criar uma mão de cartas
# ############################################################

import cCarta
import cMonte
import random as rd
from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
class cMao:

# *******************************************************
# ***                                                 ***
# *******************************************************
    def __init__(self):
        self.__inicio__     = None
        self.__fim__ = None
        self.__numElems__   = 0

# *******************************************************
# ***                                                 ***
# *******************************************************
    def getTamanho(self):
        return self.__numElems__

# *******************************************************
# ***                                                 ***
# *******************************************************
    def isempty(self):
        return self.__inicio__ == None
      
# *******************************************************
# ***                                                 ***
# *******************************************************
    def __str__(self):

        outStr = ""

        if self.__inicio__ == None:        
          outStr += "|    MÃO   VAZIA    |\n"
        elif self.__inicio__ == self.__fim__:
          outStr += f'[{self.__inicio__.getDado()}]'
        else:
          noCor = self.__inicio__
          outStr += f'[{noCor.getDado()}'
          while noCor != self.__fim__:
            outStr += f', {noCor.getProx().getDado()}'
            noCor = noCor.getProx()
          outStr += "]"

        return outStr

# *******************************************************
# ***                                                 ***
# *******************************************************
    def setCarta(self, no):
      novoNo = no
      if self.isempty():
        self.__inicio__ = novoNo
        self.__fim__ = novoNo
        self.__numElems__ += 1        
        return True
        
      elif novoNo.getValor() <= self.__inicio__.getValor():
        self.__inicio__.setAnte(novoNo)
        novoNo.setProx(self.__inicio__)
        self.__inicio__ = novoNo
        self.__numElems__ += 1        
        return True
        
      elif novoNo.getValor() >= self.__fim__.getValor():
        novoNo.setAnte(self.__fim__)
        self.__fim__.setProx(novoNo)
        self.__fim__ = novoNo
        self.__numElems__ += 1        
        return True
      
      else:
        noCor = self.__inicio__
        while noCor.getProx() is not None and novoNo.getValor() > noCor.getProx().getValor():
          noCor = noCor.getProx()
        novoNo.setProx(noCor.getProx())
        novoNo.setAnte(noCor)
        noCor.getProx().setAnte(novoNo)
        noCor.setProx(novoNo)
        self.__numElems__ += 1        
        return True
      
# *******************************************************
# ***                                                 ***
# *******************************************************
    def buscaPos(self, pos):    
      contador = 0
      if pos > self.__numElems__ - 1:
        return False
      else:
        noCor = self.__inicio__
        while contador < pos:
          noCor = noCor.getProx()
          contador += 1
        return noCor

# *******************************************************
# ***                                                 ***
# *******************************************************
    def buscaPar(self, no):
        if self.__inicio__ == None:
          return False, None
        else:
          noCor = self.__inicio__
          while noCor.getProx() is not None and noCor.getValor() < no.getValor():
            noCor = noCor.getProx()
          if noCor.getValor() == no.getValor():
            self.removeNo(noCor)
            return True, noCor
          else:
            return False, None

# *******************************************************
# ***                                                 ***
# *******************************************************
    def verificarPares(self):
      descarte = cMonte.cMonte(self.getTamanho()*2)
      noCor = self.__inicio__
      while noCor != self.__fim__ and noCor != None:
        if noCor.getValor() == noCor.getProx().getValor():
          noProx = noCor.getProx()
          noProxProx = noProx.getProx()
          self.removeNo(noCor)
          self.removeNo(noProx)
          descarte.push(noCor)
          descarte.push(noProx)
          noCor = noProxProx
        else:
          noCor = noCor.getProx()
      return descarte
        
# *******************************************************
# ***                                                 ***
# *******************************************************
    def removeNo(self, no):
      if self.isempty():
        return False
      if no == self.__inicio__:
        self.__inicio__ = no.getProx()
        if no.getProx() != None:
          no.getProx().setAnte(None)
          no.setProx(None)  
        self.__numElems__ -= 1        
        return True
      elif no == self.__fim__:
        self.__fim__ = no.getAnte()
        no.getAnte().setProx(None)
        no.setAnte(None)
        self.__numElems__ -= 1
        return True
      else:
        no.getAnte().setProx(no.getProx())
        no.getProx().setAnte(no.getAnte())
        no.setAnte(None)
        no.setProx(None)
        self.__numElems__ -= 1
        return True
      
# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    mao = cMao()

    print(mao)
    
    rd.seed(int(datetime.now().strftime('%H%M%S')))
    for i in range(10):
      carta = cCarta.cCarta(rd.randint(1,10), 'Ouros')
      mao.setCarta(carta)
      
    print(mao)
    print(mao.getTamanho())
    
    descarte = mao.verificarPares()
    print(mao)
    print(descarte)
    
    print(mao.getTamanho())
    
    pos = rd.randint(0,mao.getTamanho()-1)
    print(pos)
    retirada = mao.buscaPos(pos)
    print(retirada)
    
    chave, carta = mao.buscaPar(cCarta.cCarta(3, 'Paus'))
    if chave:
      descarte.push(carta)
      descarte.push(cCarta.cCarta(3, 'Paus'))
      print(descarte.getUltPar())
    
    
    