import random
from baralho import Baralho

class ACE:
    def __init__(self, baralho):
        self.cartas = []
        self.baralho = baralho
    
    def gerar_ace(self):
        # Retira as cartas do baralho para formar o ACE
        while self.baralho.quantidade_cartas() > 0:
            carta = self.baralho.retirar_carta()
            self.cartas.append(carta)
    
    def retirar_mico(self):
        # Retira uma carta do ACE para ser o mico
        if self.cartas:
            indice = random.randint(0, len(self.cartas) - 1)
            return self.cartas.pop(indice)
        else:
            return None
    
    def quantidade_cartas(self):
        # Retorna a quantidade de cartas restantes no ACE
        return len(self.cartas)
