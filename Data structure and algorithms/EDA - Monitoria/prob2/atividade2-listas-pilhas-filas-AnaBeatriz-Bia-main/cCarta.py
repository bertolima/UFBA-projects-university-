class Carta:

  def __init__(self, naipe, valor):
    self.naipe = naipe
    self.valor = valor

  def __str__(self):
    return f"[{self.valor},{self.naipe}]"

  # def __repr__(self):
  #   return f"[{self.valor},{self.naipe}]"

if __name__ == '__main__':
  carta = Carta('♠',2)
  #print(carta)
