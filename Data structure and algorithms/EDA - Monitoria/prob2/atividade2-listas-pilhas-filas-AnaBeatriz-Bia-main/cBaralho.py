import random
#from listaBaralho import listaBaralho
from cCarta import Carta
import random
from cpilha import cPilha
#from cLista import lista

# distribuindo uso pilha
# na mão uso lista
# fila para a ordem do jogo


class Baralho(cPilha):

  def __init__(self, n):
    # herança: vou herdar tudo que a pilha faz
    super().__init__(n)
    self.criar_baralho()
    self.embaralhar()

  def criar_baralho(self):
    naipes = ['♠', '♣', '♦', '♥']
    valores = [
      'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
    ]

    for naipe in naipes:
      for valor in valores:
        carta = Carta(naipe, valor)
        self.push(carta)

  def embaralhar(self):
    for i in self.vPilha:
      sorteio = random.randint(0, self.size() - 1) #posição aleatoria
      cartaAleatoria = i 
      i = self.vPilha[sorteio] 
      self.vPilha[sorteio] = cartaAleatoria
  
  # como tirar o par e deixar o mico?
  # retorno o par do mico 
  
  def mico(self):
    self.criar_baralho() 
    carta_removida = self.pop()
    if carta_removida is None:
      pass
    for carta in self.vPilha:
      if carta.valor == carta_removida.valor:
          return carta
    return None

if __name__ == "__main__":
  baralho = Baralho(52)
  baralho.criar_baralho()
  # print("Baralho Desembaralhado", baralho.vPilha)
  baralho.embaralhar()
  # print()
  # print("Baralho Embaralhado", baralho.vPilha)
  # print()
