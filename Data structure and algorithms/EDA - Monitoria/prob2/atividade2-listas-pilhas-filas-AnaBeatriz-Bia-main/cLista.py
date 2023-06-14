from cNo import No

class lista:
  
  def __init__(self, ordem=False):
    self.__inicio__     = None
    self.__numElems__   = 0
    self.listaOrdenada = ordem 

  def getTamanho(self):
    return self.__numElems__

  def __str__(self):
    outStr = ""

    if self.__inicio__ == None:        
        outStr += "=====================\n"
        outStr += "|   LISTA   VAZIA   |\n"
        outStr += "=====================\n"
    else:
        # Percorre a lista encadeada, imprimindo cada elemento
        noCorrente = self.__inicio__
        while noCorrente != None:
          outStr += str(noCorrente.__dado__) + "\n"
          noCorrente = noCorrente.__prox__

    return outStr

  def insereNoFinal(self, n):
    novoNo = No(n)
    if self.__inicio__ == None:
      self.__inicio__ = novoNo
    else:
      noCorrente = self.__inicio__
      while noCorrente.__prox__ != None:
        noCorrente = noCorrente.__prox__
      noCorrente.__prox__ = novoNo
    self.__numElems__ += 1
    return True

  def buscaDado(self, n):
    noCorrente = self.__inicio__
    while noCorrente != None:
      if noCorrente.__dado__ == n:
        return True
      noCorrente = noCorrente.__prox__
    return False

  def removeNo(self, n):
    if self.__inicio__ == None:
      return False 
    noCorrente = self.__inicio__
    noAnterior = None
    while noCorrente != None and noCorrente.__dado__ != n:
      noAnterior = noCorrente
      noCorrente = noCorrente.__prox__
    if noCorrente == None:
      return False
    if noAnterior == None:
      self.__inicio__ = noCorrente.__prox__
    else:
      noAnterior.__prox__ = noCorrente.__prox__
    del noCorrente
    self.__numElems__ -= 1
    return True

  def __iter__(self):
    self.__noCorrente__ = self.__inicio__
    return self

  def __next__(self):
    if self.__noCorrente__ is None:
      raise StopIteration
    dado = self.__noCorrente__.__dado__
    self.__noCorrente__ = self.__noCorrente__.__prox__
    return dado

  def remove(self, n):
    if self.listaOrdenada == True:
      if self.__inicio__ is None:
        return False

      if self.__inicio__.getDado() == n:
        self.__inicio__ = self.__inicio__.getProx()
        self.__numElems__ -= 1
        return True

      noCorrente = self.__inicio__.getProx()
      noAnterior = self.__inicio__
      
      while noCorrente is not None:
        if noCorrente.getDado() == n:
          noAnterior.setProx(noCorrente.getProx())
          self.__numElems__ -= 1
          return True
      
        noAnterior = noCorrente
        noCorrente = noCorrente.getProx()
    
    return False


  
if __name__ == '__main__':

  lista = lista()
  print(lista)
  lista.insereNoFinal(10)
  lista.insereNoFinal(40)
  lista.insereNoFinal(78)
  print("Lista")
