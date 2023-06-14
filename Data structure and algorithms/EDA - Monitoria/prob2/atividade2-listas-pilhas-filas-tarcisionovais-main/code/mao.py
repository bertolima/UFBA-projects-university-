from carta import Carta

class Mao:
    def __init__(self):
        self.cartas = []
        self.pares = []

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def remover_carta(self, carta):
        self.cartas.remove(carta)

    def tem_par(self):
        for i in range(len(self.cartas)):
            for j in range(i + 1, len(self.cartas)):
                if self.cartas[i].valor == self.cartas[j].valor:
                    return True
        return False

    def adicionar_par(self, carta1, carta2):
        self.pares.append((carta1, carta2))
