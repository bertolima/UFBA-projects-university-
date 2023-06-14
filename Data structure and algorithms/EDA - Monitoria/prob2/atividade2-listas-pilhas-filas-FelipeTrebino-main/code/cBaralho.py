# Atividade 2 - Simulando um Jogo de Baralho
# Aluno: Felipe S. Trebino
# Classe de cBaralho

from cCarta import cCarta
from cVetor import cVetor

class cBaralho:

# *******************************************************
    def __init__(self, n = 52):
        self.__vPilha   = [0] * n
        self.__maxElem  = n 
        self.__topo     = 0
        return

# *******************************************************
    def push(self, carta):

        if self.full():
            return

        self.__vPilha[self.__topo] = carta
        self.__topo += 1

        return

# *******************************************************
    def pop(self):

        if self.empty():
            return None

        self.__topo -= 1
        return self.__vPilha[self.__topo]

# *******************************************************
    def empty(self):
        return self.__topo == 0

# *******************************************************
    def full(self):
        return self.__topo == self.__maxElem

# *******************************************************
    def __len__(self):
        return self.__topo

# *******************************************************  
    # Método para gerar as 52 cartas do baralho
    def generateDeck(self):
        for i in range(4):
            match(i):
                case 0:
                    naipe = 'Copas'
                case 1:
                    naipe = 'Ouros'
                case 2:
                    naipe = 'Espadas'
                case _:
                    naipe = 'Paus'

            for j in range(1,14):
                match j:
                    case 1:
                        valor = 'Ás'
                    case 11:
                        valor = 'Valete'
                    case 12:
                        valor = 'Dama'
                    case 13:
                        valor = 'Rei'
                    case _:
                        valor = j
                self.push(cCarta(valor, naipe))
        return
    
# *******************************************************
    # Método para embaralhar cartas utilizando vetor
    def shuffle(self):
        vetor = cVetor(len(self))
        for i in range(len(self)):
           vetor.insert(self.pop())
        vetor.shuffle()
        for i in range(len(vetor)):
            self.push(vetor[i])
        return

# *******************************************************
    # Método para clonar o baralho, utilizado para visualização das cartas sem afetar o baralho original
    def clone(self):
        vetor = cVetor(len(self))
        for i in range(len(self)):
            vetor.insert(self.pop()) 
        cloneV = vetor.clone()
        cloneB = cBaralho()
        for i in range(len(vetor)-1,-1,-1):
            self.push(vetor[i])
            cloneB.push(cloneV[i])

        return cloneB
        
# *******************************************************
if __name__ == '__main__':
    # Criar e gerar baralho
    baralho = cBaralho()
    baralho.generateDeck()

    print('Baralho Gerado\n')

    # Visualizar baralho através de clone
    baralho2 = baralho.clone()

    while(not baralho2.empty()):
        print(baralho2.pop())

    # Embaralhar Baralho e visualizar resultado
    baralho.shuffle()

    print('\n\nBaralho Embaralhado\n')
    while(not baralho.empty()):
        print(baralho.pop())

