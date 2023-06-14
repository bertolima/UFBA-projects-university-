from cpilha import cPilha
from cfila import cFila
from cLista import lista
from cBaralho import Baralho
from cCarta import Carta

class Jogador: 
  def __init__(self, nome):
    self.nome = nome
    self.baralho = Baralho(52)
    self.valor = Carta('♠',2)
    #self.nome = cFila()
    self.mao = lista()
    self.valor = cPilha(52)
    self.pares = cPilha(52)

  def __str__(self):
    return f"{self.nome}"

if __name__ == '__main__':
  jogador1 = Jogador("Jogador 1")
  jogador2 = Jogador("Jogador 2")
  print(jogador1)
