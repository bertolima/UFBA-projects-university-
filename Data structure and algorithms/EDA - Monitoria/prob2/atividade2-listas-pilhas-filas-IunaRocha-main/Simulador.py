from random import shuffle
from baralho import Baralho
from ACE import ACE
from MaoJogador import MaoJogador
from MonteCartas import MonteCartas

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = MaoJogador()
        self.monte = MonteCartas()

    def jogar(self, jogador_alvo):
        # O jogador escolhe uma carta para jogar contra o jogador alvo
        carta_escolhida = self.escolher_carta(jogador_alvo)
        self.mao.remover_carta(carta_escolhida)
        self.monte.adicionar_carta(carta_escolhida)
        return carta_escolhida

    def escolher_carta(self, jogador_alvo):
        # O jogador escolhe uma carta aleatória do jogador alvo
        return jogador_alvo.mao.obter_carta_aleatoria()

    def possui_par(self):
        # Verifica se o jogador possui um par de cartas em sua mão
        return self.mao.possui_par()

class JogoMico:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.baralho = Baralho()
        self.ace = ACE()

    def distribuir_cartas(self):
        # Embaralha o baralho, preenche o ACE com as cartas embaralhadas e retira o mico
        self.baralho.embaralhar()
        self.ace.preencher(self.baralho)
        self.ace.retirar_mico()

        # Distribui as cartas entre os jogadores de forma alternada
        num_jogadores = len(self.jogadores)
        for i, carta in enumerate(self.ace):
            jogador = self.jogadores[i % num_jogadores]
            jogador.mao.adicionar_carta(carta)

    def realizar_jogada(self, jogador):
        # Realiza a jogada de um jogador escolhendo uma carta para jogar contra um jogador alvo
        jogador_alvo = self.escolher_jogador_alvo(jogador)
        carta_jogada = jogador.jogar(jogador_alvo)
        
        # Verifica se o jogador possui um par de cartas e o adiciona ao monte do jogador
        if jogador.possui_par():
            self.adicionar_par(jogador)
        return jogador_alvo, carta_jogada

    def escolher_jogador_alvo(self, jogador):
        # Escolhe o jogador alvo para uma jogada, excluindo o próprio jogador
        jogadores_disponiveis = [j for j in self.jogadores if j != jogador]
        return jogadores_disponiveis[0] if jogadores_disponiveis else None

    def adicionar_par(self, jogador):
        # Obtém o par de cartas do jogador e adiciona ao monte do jogador
        par = jogador.mao.obter_par()
        jogador.monte.adicionar_par(par)

    def verificar_fim_jogo(self):
        # Verifica se algum jogador possui apenas uma carta na mão, indicando o fim do jogo
        for jogador in self.jogadores:
            if len(jogador.mao) == 1:
                return True
        return False

    def exibir_estado_jogo(self):
        # Exibe o estado atual do jogo, mostrando a mão e o monte de cada jogador
        for jogador in self.jogadores:
            print(f"Jogador: {jogador.nome}")
            print("Mão:", jogador.mao)
            print("Monte:", jogador.monte)
            print()

    def executar(self):
        # Executa o jogo
        self.distribuir_cartas()
        jogo_em_andamento = True

        while jogo_em_andamento:
            for jogador in self.jogadores:
                jogador_alvo, carta_jogada = self.realizar_jogada(jogador)
                print(f"{jogador.nome} jogou a carta {carta_jogada}")
                print(f"Jogador alvo: {jogador_alvo.nome}")
                print()

                self.exibir_estado_jogo()

                if self.verificar_fim_jogo():
                    jogo_em_andamento = False
                    perdedor = self.obter_perdedor()
                    print(f"O jogador {perdedor.nome} perdeu o jogo!")
                    break

    def obter_perdedor(self):
        # Obtém o jogador perdedor, ou seja, aquele que possui apenas uma carta na mão
        for jogador in self.jogadores:
            if len(jogador.mao) == 1:
                return jogador

        return None

