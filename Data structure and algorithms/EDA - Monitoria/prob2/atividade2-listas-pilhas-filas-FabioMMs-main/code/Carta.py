# ###############################################################
#       Implementação da Classe Carta baseado na Classe cNó
# ###############################################################

# ###############################################################
#                      Import das Bibliotecas 
# ###############################################################

import Baralho
import Jogador
import ListaJogadores
import MaoJogador
import PilhaCartas
import random

# ###############################################################
#                   Codificação da Classe Carta
# ###############################################################

class Carta:

# ###############################################################
#                   Construtor da Classe Carta
# ###############################################################

    def __init__(self, naipe, valor):
        self._naipe = naipe
        self._valor = valor
        self._proxCarta = None

# ###############################################################
#                  Métodos da Classe Carta (cNó)
# ###############################################################

    def getNaipe(self):
        return self._naipe

    def getValor(self):
        return self._valor

    def getProxCarta(self):
        return self._proxCarta


    def setNaipe(self, novoNaipe):
        self._naipe = novoNaipe

    def setValor(self, novoValor):
        self._valor = novoValor

    def setProxCarta(self, novoProxCarta):
        self._proxCarta = novoProxCarta

    def __eq__(self, other):
        if isinstance(other, Carta):
            return ((self._naipe == other._naipe) and (self._valor == other._valor))
        
        else:
            return False

    def __repr__(self):
        outStr = ""
        outStr += f'[ {self._valor} | {self._naipe} ]'
        outStr += "\n"

        return outStr
    
# ###############################################################
#               Métodos da Classe Carta (Especiais)
# ###############################################################



# ###############################################################
#                Codificação do Programa de Testes
# ###############################################################

if __name__ == '__main__':
    
    teste = Carta("E", 10)
    print(teste)

    teste.getNaipe()
    teste.getProxCarta()
    teste.getValor()

    teste.setNaipe("P")
    teste.setValor(2)
    teste.setProxCarta(teste)

    teste.getProxCarta()
    print(teste)