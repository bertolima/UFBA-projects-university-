import cPilha
import cLista
import cCarta

import random


# Herança da TAD cPilha
class cBaralho(cPilha.cPilha):
    def __init__(self, n):
        super().__init__(n)
        self.montarBaralho()

    # Método monta uma pilha ordenada (baralho)
    def montarBaralho(self):
        for i in range(4):
            for j in range(1, 14):
                if i == 0:
                    self.push(cCarta.carta(j, 'Copas'))
                elif i == 1:
                    self.push(cCarta.carta(j, 'Ouros'))
                elif i == 2:
                    self.push(cCarta.carta(j, 'Paus'))
                elif i == 3:
                    self.push(cCarta.carta(j, 'Espadas'))

    # Método embaralha e retorna o mico
    def embaralhar(self):
        # Agrupamentos de Cartas Embaralhadas (ACE):
        # Criando baralhos auxiliares para embaralhar (listas Compostas de cartas)
        baralho1 = cLista.cLista()
        baralho2 = cLista.cLista()

        # Distribuicao do baralho em na lista baralho1 (ordem inversa)
        for i in range(52):
            baralho1.insereNo(self.pop())

        # Distribuicao aleatória do baralho1 em na lista baralho2
        for i in range(51, -1, -1):
            baralho2.insereNo(baralho1.removePos(random.randint(0, i)).getDado())

        # Retirada do mico no sorteio:
        mico = baralho2.removePos(random.randint(0, 51)).getDado()

        # Distribuição aleatório do baralho (sem o mico) de volta para a pilha baralho:
        for i in range(50, -1, -1):
            aux = baralho2.removePos(random.randint(0, i)).getDado()
            self.push(aux)

        return mico


if __name__ == '__main__':
    baralho = cBaralho(52)

    print(baralho)

    mico = baralho.embaralhar()

    print(f'mico: {mico}')
    print()

    print(baralho)
