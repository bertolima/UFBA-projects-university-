class cPilha:

  def __init__(self, n):
    self.vPilha     = [0] * n 
    self.maxElem    = n 
    self.topo       = 0
    return

  # Empilha
  def push(self, k): 
    if self.full():
      return
    self.vPilha[self.topo] = k
    self.topo += 1
    return

  # Desempilhar 
  def pop(self):
    if self.empty():
      return
    self.topo -= 1
    return self.vPilha[self.topo]

  def empty(self):
    return self.topo == 0

  def full(self):
    return self.topo == self.maxElem

  def size(self):
    return self.topo

if __name__ == '__main__':
  pilha = cPilha(10)
  pilha.push(2)
  #print(pilha)
