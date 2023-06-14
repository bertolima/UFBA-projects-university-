import random
from mao import Mao

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = Mao()

    def jogar(self, outros_jogadores):
        if not self.mao.cartas:
            return

        indice_carta = random.randint(0, len(self.mao.cartas) - 1)
        carta = self.mao.cartas.pop(indice_carta)

        for jogador in outros_jogadores:
            jogador.verificar_carta(carta)

    def verificar_carta(self, carta):
        if carta in self.mao.cartas:
            self.mao.remover_carta(carta)
            self.mao.adicionar_par(carta, self.mao.cartas[-1])
