# ###############################################################
#  Implementação da Classe ListaJogadores baseado na Classe cLSEC
# ###############################################################

# ###############################################################
#                      Import das Bibliotecas 
# ###############################################################

import Baralho
import Carta
import Jogador
import MaoJogador
import PilhaCartas
import random

# ###############################################################
#              Codificação da Classe ListaJogadores
# ###############################################################

class ListaJogadores:

# ###############################################################
#              Construtor da Classe ListaJogadores
# ###############################################################

    def __init__(self):
        self._primeiroJogador = None
        self._numJogadores = 0

# ###############################################################
#              Métodos da Classe ListaJogadores (cLSEC)
# ###############################################################

    def getNumJogadores(self):
        return self._numJogadores
    
    def getPrimeiroJogador(self):
        return self._primeiroJogador

    def inserirJogadores(self, jogador):
        novoJogador = jogador

        if self._primeiroJogador is None:
            self._primeiroJogador = novoJogador
            novoJogador.setProxJogador(novoJogador)

        else:
            jogadorAtual = self._primeiroJogador

            while jogadorAtual.getProxJogador() != self._primeiroJogador:
                jogadorAtual = jogadorAtual.getProxJogador()

            jogadorAtual.setProxJogador(novoJogador)
            novoJogador.setProxJogador(self._primeiroJogador)
            
        self._numJogadores += 1
        print("Novo Jogador Inserido com Sucesso!")


    def removerJogadores(self, jogador):
        if self._primeiroJogador is None:
            return False
        
        else:
            jogadorAtual = self._primeiroJogador
            jogadorAnterior = None

            while jogadorAtual.getProxJogador() != self._primeiroJogador and jogador.getNomeJogador() != jogadorAtual.getNomeJogador():
                jogadorAnterior = jogadorAtual
                jogadorAtual = jogadorAtual.getProxJogador()

            if jogador.getNomeJogador() == jogadorAtual.getNomeJogador():
                if jogadorAnterior is None:                                                           # Condição Remoção do Primeiro Elemento
                    if self._primeiroJogador.getProxJogador() == self._primeiroJogador:               # Caso Ele Seja Elemento Único
                        self._primeiroJogador = None
                    
                    else:
                        jogadorAtual = self._primeiroJogador

                        while jogadorAtual.getProxJogador() != self._primeiroJogador:
                            jogadorAtual = jogadorAtual.getProxJogador()

                        jogadorAtual.setProxJogador(self._primeiroJogador.getProxJogador())
                        self._primeiroJogador = self._primeiroJogador.getProxJogador()


                elif jogadorAtual.getProxJogador() == self._primeiroJogador:                               # Condição de Remoção do Último Elemento
                    if self._primeiroJogador.getProxJogador() == self._primeiroJogador:                    # Caso Ele Seja Elemento Único
                        self._primeiroJogador = None    
                    
                    else:
                        jogadorAtual = self._primeiroJogador

                        while jogadorAtual.getProxJogador().getProxJogador() != self._primeiroJogador:
                            jogadorAtual = jogadorAtual.getProxJogador()

                        jogadorAtual.setProxJogador(self._primeiroJogador)
                    

                else:                                                                   # Condição de Remoção de Elemento Central
                    jogadorAnterior.setProxJogador(jogadorAtual.getProxJogador())
            
        
                self._numJogadores -= 1
                print("Jogador Removido com Sucesso!")
                return True
            
            else:
                print("Jogador Não Encontrado!")
                return False
            
    def __repr__(self):
        if self._primeiroJogador is None:
                outStr = "Não há Jogadores!"
                outStr += "\n"

                return outStr

        else:
            outStr = ""

            jogadorAtual = self._primeiroJogador

            while True:
                outStr += f'[{jogadorAtual._nomeJogador}]'
                outStr += "\n"

                jogadorAtual = jogadorAtual.getProxJogador()

                if jogadorAtual == self._primeiroJogador:
                    break
                
            return outStr

# ###############################################################
#            Métodos da Classe ListaJogadores (Especiais)
# ###############################################################
            
            
# ###############################################################
#                Codificação do Programa de Testes
# ###############################################################

if __name__ == '__main__':

    listaJogador = ListaJogadores()
    print(listaJogador)

    jogador1 = Jogador.Jogador("Junior")
    jogador2 = Jogador.Jogador("Flavia")
    jogador3 = Jogador.Jogador("Denis")
    jogador4 = Jogador.Jogador("Lucia")
    

    listaJogador.inserirJogadores(jogador1)
    print(listaJogador)

    listaJogador.inserirJogadores(jogador2)
    print(listaJogador)

    listaJogador.inserirJogadores(jogador3)
    print(listaJogador)

    listaJogador.inserirJogadores(jogador4)
    print(listaJogador)

    listaJogador.removerJogadores(jogador3)
    print(listaJogador)

    listaJogador.removerJogadores(jogador1)
    print(listaJogador)

    listaJogador.removerJogadores(jogador4)
    print(listaJogador)

    listaJogador.removerJogadores(jogador2)
    print(listaJogador)