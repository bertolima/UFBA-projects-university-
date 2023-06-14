# ###############################################################
#    Implementação da Classe MaoJogador baseado na Classe cLSE
# ###############################################################

# ###############################################################
#                      Import das Bibliotecas 
# ###############################################################

import Baralho
import Carta
import Jogador
import ListaJogadores
import PilhaCartas
import random

# ###############################################################
#                   Codificação da Classe MaoJogador
# ###############################################################

class MaoJogador:

# ###############################################################
#                   Codificação da Classe MaoJogador
# ###############################################################

    def __init__(self):
        self._cartaInicial = None
        self._numCartas = 0

# ###############################################################
#                  Métodos da Classe MaoJogador (cLSE)
# ###############################################################

    def getNumCartas(self):
        return self._numCartas
    
    def getCartaInicial(self):
        return self._cartaInicial
    
    def insereCarta(self, carta):
        novaCarta = carta

        if self._cartaInicial is None:
            self._cartaInicial = novaCarta

        else:
            cartaAtual = self._cartaInicial
            cartaAnterior = None

            while cartaAtual.getProxCarta() is not None and novaCarta.getValor() > cartaAtual.getValor():
                cartaAnterior = cartaAtual
                cartaAtual = cartaAtual.getProxCarta()

            if novaCarta.getValor() <= cartaAtual.getValor():
                if cartaAnterior is None:
                    novaCarta.setProxCarta(cartaAtual)
                    self._cartaInicial = novaCarta

                else:
                    novaCarta.setProxCarta(cartaAtual)
                    cartaAnterior.setProxCarta(novaCarta)

            else:
                cartaAtual.setProxCarta(novaCarta)

        self._numCartas += 1
        print("Carta Inserida na Mão com Sucesso!")
        return True

    def buscaCarta(self, carta):
        if self._cartaInicial is None:
            return print("Mão Vazia!")
        
        else:
            cartaAtual = self._cartaInicial

            while cartaAtual.getProxCarta() is not None and cartaAtual != carta:
                cartaAtual = cartaAtual.getProxCarta()

            if cartaAtual is None:
                return False
            
            elif cartaAtual == carta:
                return True

            else:
                return False
            
    def removeCarta(self, carta):
        if self._cartaInicial is None:
            outStr = ""
            outStr += "Não Foi Possível Remover a Carta\n"
            outStr += "Mão Está Vazia!\n"

            print(outStr)
            return False
        
        else:
            cartaAtual = self._cartaInicial
            cartaAnterior = None

            while cartaAtual.getProxCarta() is not None and cartaAtual.getValor() != carta.getValor():
                cartaAnterior = cartaAtual
                cartaAtual = cartaAtual.getProxCarta()

            if cartaAtual is None:
                return False

            elif cartaAtual.getValor() != carta.getValor():
                return False
            
            elif cartaAnterior is None:
                self._cartaInicial = cartaAtual.getProxCarta()

            else:
                cartaAnterior.setProxCarta(cartaAtual.getProxCarta()) 
                del cartaAtual

                self._numCartas -= 1
                print("Nó Removido com Sucesso!")
                return True
    

    def __repr__(self):
        if self._cartaInicial is None:
                outStr = "Mão Vazia!"
                outStr += "\n"

                return outStr

        else:
            cartaAtual = self.getCartaInicial()
            outStr = ""

            while cartaAtual is not None:
                outStr += f'[ {cartaAtual._valor} | {cartaAtual._naipe} ]'
                outStr += "\n"

                cartaAtual = cartaAtual.getProxCarta()
                
            return outStr
        
# ###############################################################
#               Métodos da Classe MaoJogador (Especiais)
# ###############################################################

    def buscaPosicao(self, posicao):
        if posicao > self.getNumCartas():
            print("Posição fora da Lista!")
            return False
        
        else:
            contador = 1
            cartaAtual = self.getCartaInicial()

            while contador != posicao:
                contador += 1
                cartaAtual = cartaAtual.getProxCarta()

            if contador == posicao:
                print(f"Elemento {posicao} é {cartaAtual}")
                return cartaAtual
            
            else:
                print("Elemento Não Encontrado!")
                return False

    def buscaPar(self, pilhaCartas):
        cartaAtual = self.getCartaInicial()

        while cartaAtual is not None:
            buscaCarta = cartaAtual.getProxCarta()

            while buscaCarta is not None:
                if buscaCarta.getValor() == cartaAtual.getValor():
                    aux1 = buscaCarta
                    aux2 = cartaAtual

                    pilhaCartas.pilhaPush(aux1)
                    pilhaCartas.pilhaPush(aux2)

                    self.removeCarta(aux1)
                    self.removeCarta(aux2)

                buscaCarta = buscaCarta.getProxCarta()
            
            cartaAtual = cartaAtual.getProxCarta()

        
# ###############################################################
#                Codificação do Programa de Testes
# ###############################################################

if __name__ == '__main__':

    baralho = Baralho.Baralho(5)
    baralho.geraBaralho()
    print(baralho)

    pilhaTeste = PilhaCartas.PilhaCartas(baralho.size() - 1)
    maoTeste = MaoJogador()
    print(maoTeste)

    while not baralho.empty():
        maoTeste.insereCarta(baralho.pop())
    print(maoTeste)

    carta = Carta.Carta('♣', 5)
    print(maoTeste.buscaCarta(carta))

    carta2 = Carta.Carta('♦', 1)
    print(maoTeste.buscaCarta(carta2))

    carta3 = Carta.Carta('♥', 5)
    maoTeste.insereCarta(carta3)
    print(maoTeste)

    maoTeste.buscaPosicao(1)
    maoTeste.buscaPosicao(7)

    maoTeste.buscaPar(pilhaTeste)
    print(maoTeste)

    print(maoTeste.removeCarta(carta))
    print(maoTeste)
