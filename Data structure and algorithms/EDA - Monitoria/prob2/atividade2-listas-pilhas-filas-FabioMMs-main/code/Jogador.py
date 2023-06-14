# ###############################################################
#       Implementação da Classe Jogador baseado na Classe cNó
# ###############################################################

# ###############################################################
#                      Import das Bibliotecas 
# ###############################################################

import Baralho
import Carta
import ListaJogadores
import MaoJogador
import PilhaCartas
import random

# ###############################################################
#                  Codificação da Classe Jogador
# ###############################################################
class Jogador(object):

# ###############################################################
#                  Construtor da Classe Jogador
# ###############################################################

    def __init__(self, nomeJogador):
        self._nomeJogador = nomeJogador
        self._proxJogador = None
        self._mao = MaoJogador.MaoJogador()

# ###############################################################
#                 Métodos da Classe Jogador (cNó)
# ###############################################################

    def getNomeJogador(self):
        return self._nomeJogador

    def getProxJogador(self):
        return self._proxJogador

    def setNomeJogador(self, novoNome):
        self._nomeJogador = novoNome

    def setProxJogador(self, proxJogador):
        self._proxJogador = proxJogador

    def __repr__(self):
        outStr = ""
        outStr += f"Jogador(a): {self._nomeJogador}"

        return outStr
    
# ###############################################################
#               Métodos da Classe Jogador (Especiais)
# ###############################################################

    def maoJogador(self):
        return self._mao

# ###############################################################
#                Codificação do Programa de Testes
# ###############################################################

if __name__ == '__main__':
    teste = Jogador("Fulano")
    print(teste)

    teste.getNomeJogador()
    teste.getProxJogador()

    teste.setNomeJogador("Fulano de Tal")
    teste.setProxJogador(teste)

    teste.getProxJogador()
    print(teste)

    carta = Carta.Carta('♠', 10)
    teste.maoJogador().insereCarta(carta)
    print(teste.maoJogador().getNumCartas())
    print(teste.maoJogador())