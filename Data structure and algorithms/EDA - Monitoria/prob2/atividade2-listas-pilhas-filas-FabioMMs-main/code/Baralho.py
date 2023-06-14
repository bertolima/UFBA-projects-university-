# ###############################################################
#     Implementação da Classe Baralho baseado na Classe cPilha
# ###############################################################

# ###############################################################
#                      Import das Bibliotecas 
# ###############################################################

import Carta
import Jogador
import ListaJogadores
import MaoJogador
import PilhaCartas
import random

# ###############################################################
#                   Codificação da Classe Baralho
# ###############################################################

class Baralho:

# ###############################################################
#                   Construtor da Classe Baralho
# ###############################################################

    def __init__(self, qtdCartas):
        self._vBaralho = [0] * qtdCartas
        self._maxElementos = qtdCartas
        self._topoBaralho = 0
        self._cartaMico = None

# ###############################################################
#                Métodos da Classe Baralho (Pilha)
# ###############################################################

    def empty(self):
        return self._topoBaralho == 0

    def full(self):
        return self._topoBaralho == self._maxElementos

    def size(self):
        return self._topoBaralho
    
    def push(self, obj):
        if self.full():
            outStr = ""
            outStr += "Não foi possível Adicionar uma Carta ao Baralho...\n"
            outStr += "Baralho já está Completo!"
            outStr += "\n"

            # print(outStr)
            return False

        else:
            self._vBaralho[self._topoBaralho] = obj
            self._topoBaralho += 1

            # print("Carta Adicionada com Sucesso!") 

    def pop(self):
        if self.empty():
            outStr = ""
            outStr += "Não foi possível Remover uma Carta do Baralho...\n"
            outStr += "Baralho já está Vazio!"
            outStr += "\n"

            # print(outStr)
            return False
        
        else:
            cartaRetirada = self._vBaralho[self._topoBaralho - 1]

            self._topoBaralho -= 1

            #print("Carta Retirada com Sucesso!")
            return cartaRetirada
    
    def __repr__(self):
        i = 0
        outStr = ""

        while i != self._topoBaralho:
            valor = self._vBaralho[i].getValor()

            if valor == 1:
                valor = 'A'
                
            elif valor == 11:
                valor = 'J'

            elif valor == 12:
                valor = 'Q'
                
            elif valor == 13:
                valor = 'K'

            outStr += f'[ {valor} | {self._vBaralho[i].getNaipe()} ]'
            outStr += "\n"

            i += 1

        return outStr

# ###############################################################
#              Métodos da Classe Baralho (Especiais)
# ###############################################################

    def getCartaMico(self):
        return self._cartaMico

    def geraBaralho(self):
        for naipe in range(4):
            if naipe == 0:
                naipe = '♣'
            
            elif naipe == 1:
                naipe = '♠'
            
            elif naipe == 2:
                naipe = '♥'

            else:
                naipe = '♦'

            for valor in range(1,14):
                carta = Carta.Carta(naipe, valor)
                self.push(carta) 


    def embaralhaBaralho(self):
        lenVet = self._topoBaralho
        vetAux = [0] * lenVet
        

        for i in range(lenVet):
            vetAux[i] = self.pop()

        random.shuffle(vetAux)


        for k in range(lenVet):
            self.push(vetAux[k])

        self._cartaMico = self.pop()                                # Retirada da Carta Mico (Carta Mico sempre será a carta do topo do baralho após embaralhamento)

    def distribuiCartas(self, listaJogadores):
        jogador = listaJogadores.getPrimeiroJogador()

        while not self.empty():
            jogador.maoJogador().insereCarta(self.pop())
            jogador = jogador.getProxJogador()

# ###############################################################
#                Codificação do Programa de Testes
# ###############################################################

if __name__ == '__main__':
    
    numElementos = 10

    listaJogador = ListaJogadores.ListaJogadores()
    print(listaJogador)

    jogador1 = Jogador.Jogador("Junior")
    jogador2 = Jogador.Jogador("Flavia")
    jogador3 = Jogador.Jogador("Denis")
    jogador4 = Jogador.Jogador("Lucia")

    listaJogador.inserirJogadores(jogador1)
    listaJogador.inserirJogadores(jogador2)
    listaJogador.inserirJogadores(jogador3)
    listaJogador.inserirJogadores(jogador4)


    baralho = Baralho(numElementos)
    baralho.geraBaralho()
    print(baralho)
    print("\n")

    baralho.embaralhaBaralho()
    print(baralho)

    print(baralho._cartaMico)

    baralho.distribuiCartas(listaJogador)


    jogador = listaJogador.getPrimeiroJogador()
    while True:
        print(jogador.maoJogador())
        jogador = jogador.getProxJogador()

        if jogador == listaJogador.getPrimeiroJogador():
            break



