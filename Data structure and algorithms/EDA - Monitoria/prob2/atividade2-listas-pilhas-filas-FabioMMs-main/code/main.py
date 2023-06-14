# ###############################################################
#               Implementação da Main do Jogo Mico
# ###############################################################

# ###############################################################
#                      Import das Bibliotecas 
# ###############################################################

import Baralho
import Carta
import Jogador
import ListaJogadores
import MaoJogador
import PilhaCartas
import random

# ###############################################################
#                   Codificação do Programa Main
# ###############################################################
numCartas = 52

# Geração do Baralho
baralho = Baralho.Baralho(numCartas)
baralho.geraBaralho()
baralho.embaralhaBaralho()
print(baralho)
print(baralho.getCartaMico())

print("-----------------------------------------------------------------")

pilha = PilhaCartas.PilhaCartas(numCartas - 1)
print(pilha)

print("-----------------------------------------------------------------")

# Distribuição das Cartas
listaJogador = ListaJogadores.ListaJogadores()

jogador1 = Jogador.Jogador("Junior")
jogador2 = Jogador.Jogador("Flavia")
jogador3 = Jogador.Jogador("Denis")
jogador4 = Jogador.Jogador("Lucia")

listaJogador.inserirJogadores(jogador1)
listaJogador.inserirJogadores(jogador2)
listaJogador.inserirJogadores(jogador3)
listaJogador.inserirJogadores(jogador4)
print(listaJogador)

print("-----------------------------------------------------------------")

baralho.distribuiCartas(listaJogador)
print(jogador1.maoJogador())
print(jogador2.maoJogador())
print(jogador3.maoJogador())
print(jogador4.maoJogador())

print("-----------------------------------------------------------------")

# Formação e Armazenamento dos Pares
jogador1.maoJogador().buscaPar(pilha)
jogador2.maoJogador().buscaPar(pilha)
jogador3.maoJogador().buscaPar(pilha)
jogador4.maoJogador().buscaPar(pilha)

print(pilha)

print("-----------------------------------------------------------------")

print(jogador1.maoJogador())
print(jogador2.maoJogador())
print(jogador3.maoJogador())
print(jogador4.maoJogador())

print("-----------------------------------------------------------------")

# Jogador Pega Carta de Outro Jogador:
print(jogador2.maoJogador().buscaPosicao(2))
jogador1.maoJogador().insereCarta(jogador2.maoJogador().buscaPosicao(2))
jogador2.maoJogador().removeCarta(jogador2.maoJogador().buscaPosicao(2))

print(jogador1.maoJogador())
print(jogador2.maoJogador())
