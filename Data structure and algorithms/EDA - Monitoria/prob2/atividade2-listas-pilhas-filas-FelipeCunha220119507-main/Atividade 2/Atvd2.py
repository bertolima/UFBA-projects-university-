import random

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def adicionar_carta(self, carta):
        self.mao.append(carta)

    def remover_carta(self, indice):
        return self.mao.pop(indice)

    def possui_par(self):
        valores = {}
        for carta in self.mao:
            if carta.valor in valores:
                return True
            valores[carta.valor] = True
        return False

class JogoMico:
    def __init__(self, num_jogadores):
        self.num_jogadores = num_jogadores
        self.baralho = []
        self.jogadores = []
        self.monte_visivel = []

        naipes = ['Paus', 'Espadas', 'Copas', 'Ouros']
        valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

        # Criar baralho
        for naipe in naipes:
            for valor in valores:
                self.baralho.append(Carta(naipe, valor))

    def embaralhar(self):
        random.shuffle(self.baralho)

    def distribuir_cartas(self):
        for i in range(len(self.baralho)):
            jogador = self.jogadores[i % self.num_jogadores]
            jogador.adicionar_carta(self.baralho[i])

    def jogar(self):
        jogador_atual = random.choice(self.jogadores)

        while True:
            print("Vez do jogador:", jogador_atual.nome)
            print("Cartas na mão:", [carta.valor for carta in jogador_atual.mao])
            print("Carta no topo do monte:", self.monte_visivel[-1].valor if self.monte_visivel else "N/A")
            print()

            if jogador_atual.possui_par():
                print("O jogador", jogador_atual.nome, "fez um par!")
                par = []
                for i in range(len(jogador_atual.mao)):
                    if jogador_atual.mao[i].valor in par:
                        par_index = par.index(jogador_atual.mao[i].valor)
                        self.monte_visivel.append(jogador_atual.remover_carta(i))
                        self.monte_visivel.append(par.pop(par_index))
                        break
                    par.append(jogador_atual.mao[i].valor)
            else:
                jogador_alvo = random.choice(self.jogadores)
                while jogador_alvo == jogador_atual or len(jogador_alvo.mao) == 0:
                    jogador_alvo = random.choice(self.jogadores)

                carta_indice = random.randint(0, len(jogador_alvo.mao) - 1)
                carta = jogador_alvo.remover_carta(carta_indice)
                jogador_atual.adicionar_carta(carta)

                if isinstance(carta, Carta):
                    self.monte_visivel.append(carta)

            if len(self.baralho) == 0:
                print("O jogo acabou!")
                print("Jogador", jogador_atual.nome, "é o vencedor!")
                break

            jogador_atual = self.proximo_jogador(jogador_atual)

    def proximo_jogador(self, jogador_atual):
        index = self.jogadores.index(jogador_atual)
        return self.jogadores[(index + 1) % self.num_jogadores]


# Criar jogadores
num_jogadores = 3
jogadores = []
for i in range(num_jogadores):
    jogadores.append(Jogador("Jogador " + str(i+1)))

# Criar jogo e iniciar
jogo = JogoMico(num_jogadores)
jogo.embaralhar()
jogo.jogadores = jogadores
jogo.distribuir_cartas()
jogo.jogar()
