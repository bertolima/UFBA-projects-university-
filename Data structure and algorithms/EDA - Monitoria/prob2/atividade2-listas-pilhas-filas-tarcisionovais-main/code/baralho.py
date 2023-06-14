import random
from carta import Carta

class Baralho:
    def __init__(self):
        self.cartas = self.gerar_baralho()

    def gerar_baralho(self):
        naipes = ["Copas", "Espadas", "Ouros", "Paus"]
        valores = [str(i) for i in range(1, 10)] + ["Dama", "Valete", "Rei"]
        baralho = [Carta(naipe, valor) for naipe in naipes for valor in valores]
        random.shuffle(baralho)
        return baralho

    def comprar_carta(self):
        return self.cartas.pop()
