from cNo import No
import random

class cFila:
  
  def __init__(self):
    self._inicio     = None
    self._fim        = None
    self._numElems   = 0
  
  # Retorna o tamano da fila
  def size(self):
    return self._numElems
  
  # Adiciona elementos a fila
  def queue(self, n):
    novoNo = No(n)
    if self._inicio == None:
      self._inicio = novoNo
      self._fim    = novoNo
    else:
      self._fim.setProx(novoNo)
      self._fim = novoNo
    self._numElems += 1

  # Remove elementos da fila
  def dequeue(self):
    if self._inicio == None:
      return False
    noCorrente = self._inicio
    self._inicio = noCorrente.getProx()
    dado = noCorrente.getDado()
    del noCorrente
    self._numElems -= 1
    return dado
    
  ## Adicionar método "proximo" na TAD fila; proxJogador = fila.proximo()
  def proximo(self):
    if self._inicio == None:
      return False
    noCorrente = self._inicio
    self._inicio = noCorrente.getProx()
    dado = noCorrente.getDado()
    del noCorrente
    self._numElems -= 1
    return dado
  
  # Verifica se a fila está vazia
  def empty(self): 
    return self._inicio == None

  def primeiro(self):
    if self._inicio is None:
      return None
    return self._inicio.getDado()

  def __iter__(self):
    noCorrente = self._inicio
    while noCorrente is not None:
      yield noCorrente.getDado()
      noCorrente = noCorrente.getProx()
    
  def obter_aleatorio(self):
    if not self.empty():
      indice_aleatorio = random.randint(0, self.size() - 1)
      jogador_aleatorio = self._inicio
      for _ in range(indice_aleatorio):
        jogador_aleatorio = jogador_aleatorio.getProx()
      return jogador_aleatorio.getDado()
      #return [indice_aleatorio]
      
  def __str__(self):
    return f"[{self._inicio},{self._fim}]"
  

valor_aleatorio = cFila()
#valor_aleatorio.obter_aleatorio()
#print(valor_aleatorio.obter_aleatorio()) 
