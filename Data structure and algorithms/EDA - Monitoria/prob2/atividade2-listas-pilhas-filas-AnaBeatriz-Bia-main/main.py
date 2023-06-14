from cJogo import Jogo

# teste do simulador
if __name__ == '__main__':
  
  num_jogadores = int(input("Digite o número de jogadores (2-4): "))
  jogo = Jogo(num_jogadores)
  jogo.iniciar_jogo()
