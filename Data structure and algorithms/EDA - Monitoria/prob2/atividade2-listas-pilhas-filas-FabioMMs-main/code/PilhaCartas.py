# ###############################################################
#   Implementação da Classe PilhaCartas baseado na Classe cPilha
# ###############################################################

# ###############################################################
#                      Import das Bibliotecas 
# ###############################################################

import Baralho
import Carta
import Jogador
import ListaJogadores
import MaoJogador
import random

# ###############################################################
#                   Codificação da Classe Baralho
# ###############################################################

class PilhaCartas:

# ###############################################################
#                   Construtor da Classe Baralho
# ###############################################################

    def __init__(self, qtdCartas):
        self._vPilhaCartas = [0] * qtdCartas
        self._maxPares = qtdCartas
        self._topoPilhaCartas = 0

# ###############################################################
#                Métodos da Classe Baralho (Pilha)
# ###############################################################

    def pilhaEmpty(self):
        return self._topoPilhaCartas == 0

    def pilhaFull(self):
        return self._topoPilhaCartas == self._maxPares

    def pilhaSize(self):
        return self._topoPilhaCartas
    
    def pilhaPush(self, obj):
        if self.pilhaFull():
            outStr = ""
            outStr += "Não foi possível Adicionar uma Carta ao Baralho...\n"
            outStr += "Baralho já está Completo!"
            outStr += "\n"

            # print(outStr)
            return False

        else:
            self._vPilhaCartas[self._topoPilhaCartas] = obj
            self._topoPilhaCartas += 1

    def pilhaPop(self):
        if self.pilhaEmpty():
            outStr = ""
            outStr += "Não foi possível Remover uma Carta do Baralho...\n"
            outStr += "Baralho já está Vazio!"
            outStr += "\n"

            # print(outStr)
            return False
        
        else:
            cartaRetirada = self._vPilhaCartas[self._topoPilhaCartas - 1]

            self._topoPilhaCartas -= 1

            #print("Carta Retirada com Sucesso!")
            return cartaRetirada
    
    def __repr__(self):
        i = 0
        outStr = ""

        while i != self._topoPilhaCartas:
            valor = self._vPilhaCartas[i].getValor()

            if valor == 1:
                valor = 'A'
                
            elif valor == 11:
                valor = 'J'

            elif valor == 12:
                valor = 'Q'
                
            elif valor == 13:
                valor = 'K'

            outStr += f'[ {valor} | {self._vPilhaCartas[i].getNaipe()} ]'
            outStr += "\n"

            i += 1

        return outStr
    
# ###############################################################
#              Métodos da Classe Baralho (Especiais)
# ###############################################################



# ###############################################################
#                Codificação do Programa de Testes
# ###############################################################
if __name__ == '__main__':

    baralho = Baralho.Baralho(22)
    baralho.geraBaralho()
    print(baralho)

    pilhaCarta = PilhaCartas(baralho.size() - 1)
    maoTeste = MaoJogador.MaoJogador()
    print(maoTeste)
    print(pilhaCarta)

    while not baralho.empty():
        maoTeste.insereCarta(baralho.pop())
    print(maoTeste)

    maoTeste.buscaPar(pilhaCarta)
    print(maoTeste)
    print(pilhaCarta)