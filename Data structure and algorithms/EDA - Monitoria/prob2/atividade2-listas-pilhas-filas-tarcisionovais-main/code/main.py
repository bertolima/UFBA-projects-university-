import random
from jogador import Jogador
from jogo import Jogo

if __name__ == "__main__":
    num_jogadores = random.randint(2, 4)
    jogadores = [Jogador(f"Jogador {i+1}") for i in range(num_jogadores)]

    jogo = Jogo(jogadores)
    jogo.jogar_jogo()
    jogo.imprimir_estado_jogo()
