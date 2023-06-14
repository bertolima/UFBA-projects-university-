import random
from Carta import Carta
from Pilha import Pilha


class JogoMico:
    def __init__(self, num_jogadores):
        self.num_jogadores = num_jogadores
        self.jogadores = []
        self.baralho = self.gerar_baralho()
        self.embaralhar_baralho()
        self.mico = None
        self.montes = [Pilha() for _ in range(num_jogadores)]
        self.mao_jogadores = [[] for _ in range(num_jogadores)]

    def gerar_baralho(self):
        naipes = ["Copas", "Espadas", "Ouros", "Paus"]
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        baralho = [Carta(valor, naipe) for naipe in naipes for valor in valores]
        return baralho

    def embaralhar_baralho(self):
        random.shuffle(self.baralho)

    def distribuir_cartas(self):
        jogador_atual = 0
        while self.baralho:
            carta = self.baralho.pop(0)
            self.mao_jogadores[jogador_atual].append(carta)
            jogador_atual = (jogador_atual + 1) % self.num_jogadores

    def verificar_par(self, carta1, carta2):
        return carta1.valor == carta2.valor

    def remover_par(self, jogador):
        mao = self.mao_jogadores[jogador]
        monte = self.montes[jogador]
        i = 0
        while i < len(mao) - 1:
            j = i + 1
            while j < len(mao):
                if self.verificar_par(mao[i], mao[j]):
                    monte.empilhar(mao.pop(j))
                    monte.empilhar(mao.pop(i))
                    i -= 1
                    break
                j += 1
            i += 1

    def jogador_anterior(self, jogador_atual):
        return (jogador_atual - 1) % self.num_jogadores

    def jogador_proximo(self, jogador_atual):
        return (jogador_atual + 1) % self.num_jogadores

    def realizar_jogada(self, jogador_atual):
        jogador_anterior = self.jogador_anterior(jogador_atual)
        carta_escolhida = random.choice(self.mao_jogadores[jogador_anterior])
        self.mao_jogadores[jogador_atual].append(carta_escolhida)
        self.mao_jogadores[jogador_anterior].remove(carta_escolhida)
        self.remover_par(jogador_atual)

        print(f"\n--- Jogada do Jogador {self.jogadores[jogador_atual]} ---")
        print(f"Jogador {self.jogadores[jogador_atual]} pegou uma carta do Jogador {self.jogadores[jogador_anterior]}")
        print(f"Carta selecionada: {carta_escolhida}\n")

    def jogar(self):
        jogador_atual = 0
        rodada = 1
        while True:
            if self.fim_de_jogo():
                break
            print(f"--- Rodada {rodada} ---")
            self.realizar_jogada(jogador_atual)
            jogador_atual = self.jogador_proximo(jogador_atual)
            rodada += 1
            self.exibir_estado_jogo()
        self.exibir_estado_jogo()
        self.verificar_perdedor()

    def fim_de_jogo(self):
        count = 0
        for i, mao in enumerate(self.mao_jogadores):
            if len(mao) == 1 and all(len(m) == 0 for j, m in enumerate(self.mao_jogadores) if j != i):
                count += 1
        return count == 1

    def verificar_perdedor(self):
        for i, mao in enumerate(self.mao_jogadores):
            if len(mao) == 1:
                perdedor = self.jogadores[i]
                print(f"\nJogador {perdedor} é o perdedor!")
                return

    def exibir_estado_jogo(self):
        print("\n--- Estado Atual do Jogo ---")
        for i, jogador in enumerate(self.jogadores):
            print(f"Jogador {jogador}:")
            print("Cartas:", end=" ")
            for carta in self.mao_jogadores[i]:
                print(carta, end=" ")
            print()
            print("Monte de Cartas:", end=" ")
            monte = self.montes[i]
            if not monte.vazia():
                print(monte.exibir_topo(), end=" ")
            print()
        print()

    def iniciar_jogo(self):
        for i in range(self.num_jogadores):
            nome = input(f"Digite o nome do jogador {i + 1}: ")
            self.jogadores.append(nome)
        self.mico = self.baralho.pop(0)
        self.distribuir_cartas()
        self.remover_par(0)  # Remover pares do primeiro jogador
        self.jogar()
        print("\nJogo encerrado.")