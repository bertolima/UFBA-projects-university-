from baralho import Baralho
from jogador import Jogador

class Jogo:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.baralho = Baralho()
        self.ace = self.gerar_ace()

    def gerar_ace(self):
        ace = [self.baralho.comprar_carta() for _ in range(len(self.baralho.cartas))]
        return ace

    def distribuir_cartas(self):
        for i in range(len(self.ace)):
            jogador = self.jogadores[i % len(self.jogadores)]
            carta = self.ace[i]
            jogador.mao.adicionar_carta(carta)

    def jogar_rodada(self):
        for jogador in self.jogadores:
            outros_jogadores = [j for j in self.jogadores if j != jogador]
            jogador.jogar(outros_jogadores)

    def jogar_jogo(self):
        self.distribuir_cartas()
        while any(jogador.mao.cartas for jogador in self.jogadores):
            self.jogar_rodada()

    def imprimir_estado_jogo(self):
        for jogador in self.jogadores:
            print(f"Jogador {jogador.nome}:")
            print("  Mão:", [str(carta) for carta in jogador.mao.cartas])
            if jogador.mao.pares:
                print("  Último par:", str(jogador.mao.pares[-1][0]), "e", str(jogador.mao.pares[-1][1]))
            print()
