#import random
from cJogador import Jogador
from cBaralho import Baralho
# from cfila import cFila
from cpilha import cPilha
from cCarta import Carta
from cLista import lista

#self.baralho.vPilha = TODAS AS CARTAS

class Jogo:
  def __init__(self, num_jogadores):
    self.baralho = Baralho(52)
    self.baralho.embaralhar()
    self.carta = Carta('♠',2)
    self.mao = lista()
    self.pares = Jogador('ana')
    self.pares = cPilha(52)
    self.jogadores = lista()
    self.num_jogadores = num_jogadores
    self.mico = self.baralho.mico() # retorno o par do mico
    self.valor = self.carta.valor

  def criar_jogadores(self):
    if self.num_jogadores == 2:
      n = 2
      for i in range(n):
        nome = input(f"Informe o nome do jogador {i+1}: ")
        jogador = Jogador(nome)
        self.jogadores.insereNoFinal(jogador)
    return self.jogadores

  def distribuir_cartas(self):
    if self.num_jogadores == 2:
      # distribuir 26 cartas para cada jogador
      for i in range(26):
        for jogador in self.jogadores: #fila
          carta = self.jogadores.mao.pop()
          jogador.mao.insereNoFinal(carta) #insereNoFinal
              
  def jogar_rodada(self):
    for jogador in self.jogadores:
      carta = jogador.mao
      if self.verificar_pares(carta) == True:
        self.remover_pares(carta)
        # colocar na pilha de pares a carta
        self.pares.push(carta)
        #jogador.pares.push(carta)

  def iniciar_jogo(self):
    print()
    print('==========================')
    print('Simulador do jogo do Mico!')
    print()
    self.criar_jogadores()
    self.distribuir_cartas()
    
    self.mico = self.baralho.mico()
    self.baralho.pop()
    print()
    print("Mico:", self.mico)
    print()
    print("Iniciando o jogo do MICO!")
    print()
    for jogador in self.jogadores:
      print(f"Cartas de {jogador.nome}: {jogador.mao}")
    
    while not self.fim_de_jogo():
      for jogador in self.jogadores:
        print(f"{jogador.nome}: {jogador.mao}")
        print("RODADA")
        print()
        # while True:
        for jogador in self.jogadores:
          print(f"Turno de {jogador.nome}:")
          self.jogar_rodada()
          self.mostrar_estado_jogo()
        
          mico_jogador = self.verificar_mico(jogador.mao)  
          jogador_mico = jogador.nome
          if mico_jogador is True: # se tiver o joador mico
            print(f"{jogador_mico} perdeu o jogo!")
            break
              
  def verificar_pares(self, carta):
    for outra_carta in self.mao: #lista
      #print('outra_carta',outra_carta)
      if self.carta.valor == self.outra_carta.valor:
        return True
    return False

  def remover_pares(self, carta):
    # adicionar as cartas pares a pilha de pares e removelas da mão
    for outra_carta in self.mao:
      if carta.valor == outra_carta.valor:
        self.pares.push(outra_carta)
        self.pares.push(carta)

        self.mao.removeNo(outra_carta)
        self.mao.removeNo(carta)

  def fim_de_jogo(self):
    for jogador in self.jogadores:
      if jogador.mao.getTamanho() == 1:
        for i in jogador.mao:
          if i == self.baralho.mico():
            return True
        return False
        # se o jogador tiver na mão só uma carta e ela for o mico
        # fim de jogo
  
  def mostrar_estado_jogo(self):
    #carta = Carta(valor, naipe)
    for jogador in self.jogadores: 
      print("Mão:", jogador.mao)
      print("Cartas:", end=" ")
      #carta = jogador.mao
      for carta in self.mao:  
        print(f"{carta.valor}{carta.naipe}", end=" ") #não tá passando .valor
      print()
        
      if self.pares.size() > 0:
        print("Pares formados:", end=" ")
        for carta in self.pares:
          print(f"{carta.valor}{carta.naipe}", end=" ")
        print()
    print()
  
  def verificar_mico(self, carta):
    if carta == self.mico: # se a carta for o par do mico True
      return True
    return False

  # def getPar(self, carta_removida):
  #   for carta in self.vPilha:
  #     if carta.valor == carta_removida.valor:
  #       return True

if __name__ == "__main__":

  jogador = int(input("Digite o número de jogadores (2-4): "))
  jogo = Jogo(jogador)
  jogo.iniciar_jogo()
