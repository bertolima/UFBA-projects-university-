

from JogoMico import JogoMico


num_jogadores = int(input("Digite o número de jogadores (entre 2 e 4): "))
jogo = JogoMico(num_jogadores)
jogo.iniciar_jogo()