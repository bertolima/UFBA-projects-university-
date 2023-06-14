# ############################################################
# Classe que implementa uma Vetor
# Utilizada para criar um deck ordenado de cartas 
# ############################################################

import cCarta
import random as rd
from datetime import datetime

class cDeckOrd:

# *******************************************************
# ***                                                 ***
# *******************************************************
    def __init__(self, n):
        self.contador = 0
        self.n = n
        self.vet = [0] * n

    def setCarta(self, carta):
        if self.contador < self.n:
            self.vet[self.contador] = carta
            self.contador += 1
            return True
        else:
            return False

    def __str__(self):
        texto = '['
        for i in range(self.contador):
            if i == 0:
                texto += self.vet[i].getDado()
            else:
                texto += ', '
                texto += self.vet[i].getDado()
        texto += ']'
        return texto

    def __len__(self):
        return self.contador
    
    def embaralhar(self):
        rd.seed(int(datetime.now().strftime('%H%M%S')))
        for i in range(self.n):
            j = rd.randint(i, self.n-1)
            self.vet[i], self.vet[j] = self.vet[j], self.vet[i]
        return

    def getCarta(self, i):
        if i <= self.contador:
            return self.vet[i]
        else:
            return False

    def remove(self, i):
        if i <= self.contador:
            self.vet[i] = 0
            for p in range(i, self.contador-1):
                self.vet[p], self.vet[p+1] = self.vet[p+1], self.vet[p]
            self.contador -= 1
            return True
        else:
            return False

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':
    deck = cDeckOrd(10)
    
    for i in range (10):
        carta = cCarta.cCarta(i+1, 'Copas')
        deck.setCarta(carta)
        
    print(deck)
    print(len(deck))
    deck.embaralhar()
    print(deck)
    
    print(deck.getCarta(3))
    deck.remove(3)
    print(deck)