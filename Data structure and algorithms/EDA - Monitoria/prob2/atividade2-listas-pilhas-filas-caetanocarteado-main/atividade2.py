import random


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe


class Baralho:
    def __init__(self):
        self.cartas = []
        naipes = ['Paus', 'Copas', 'Espadas', 'Ouros']
        for naipe in naipes:
            for valor in range(1, 14):
                carta = Carta(valor, naipe)
                self.cartas.append(carta)


    def embaralhar(self):
        random.shuffle(self.cartas)


    def retirar_carta(self):
        return self.cartas.pop()


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []


    def receber_carta(self, carta):
        self.cartas.append(carta)


    def jogar_carta(self, index):
        return self.cartas.pop(index)


class JogoMico:
    def __init__(self, jogadores):
        self.baralho = Baralho()
        self.baralho.embaralhar()
        self.jogadores = jogadores
        self.mico = None


    def iniciar_partida(self):
        self.distribuir_cartas()
        self.definir_jogador_inicial()
        self.jogar()


    def distribuir_cartas(self):
        for _ in range(5):
            for jogador in self.jogadores:
                carta = self.baralho.retirar_carta()
                jogador.receber_carta(carta)


    def definir_jogador_inicial(self):
        self.jogador_atual = random.choice(self.jogadores)


    def jogar(self):
        while not self.verificar_fim_de_jogo():
            print(f"Jogador atual: {self.jogador_atual.nome}")
            print("Cartas na mão do jogador:")
            for carta in self.jogador_atual.cartas:
                print(f" - {carta.valor} de {carta.naipe}")
            # Lógica para a jogada do jogador
            self.jogador_atual = self.proximo_jogador()


    def proximo_jogador(self):
        index = self.jogadores.index(self.jogador_atual)
        proximo_index = (index + 1) % len(self.jogadores)
        return self.jogadores[proximo_index]


    def verificar_fim_de_jogo(self):
        return len(self.baralho.cartas) == 0 and all(len(jogador.cartas) == 0 for jogador in self.jogadores)




# Exemplo de uso
jogador1 = Jogador("Alice")
jogador2 = Jogador("Bob")
jogadores = [jogador1, jogador2]


jogo = JogoMico(jogadores)
jogo.iniciar_partida()

