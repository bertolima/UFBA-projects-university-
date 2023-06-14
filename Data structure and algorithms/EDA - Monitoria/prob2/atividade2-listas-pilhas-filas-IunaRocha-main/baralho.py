import random

class Baralho:
    def __init__(self):
        # Inicializa o baralho com todas as cartas
        naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
        valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
        self.cartas = [(naipe, valor) for naipe in naipes for valor in valores]
    
    def embaralhar(self):
        # Embaralha as cartas do baralho
        random.shuffle(self.cartas)
    
    def retirar_carta(self):
        # Retira a primeira carta do baralho
        if self.cartas:
            return self.cartas.pop(0)
        else:
            return None
    
    def quantidade_cartas(self):
        # Retorna a quantidade de cartas restantes no baralho
        return len(self.cartas)
