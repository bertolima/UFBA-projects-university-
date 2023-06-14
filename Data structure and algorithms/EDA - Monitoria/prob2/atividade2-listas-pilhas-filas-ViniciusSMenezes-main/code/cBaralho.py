# ##################################################
#           Classe Baralho                         #
# ##################################################

from cCarta import cCarta
from cACE import cACE
import random

# *******************************************************
""" "cBaralho" é uma classe de baralho baseada em lista duplamente 
encadeada universal para vários tipos de jogos de carta"""


class cBaralho:

    # *******************************************************
    # *******************************************************
    def __init__(self):
        self.__inicio__ = None
        self.__numCartas__ = 0
        self.gerar_baralho()

    # *******************************************************
    # *******************************************************
    def __str__(self):
        outStr = "\n"
        if self.__inicio__ is None:
            outStr += "=====================\n"
            outStr += "|    SEM CARTAS     |\n"
            outStr += "=====================\n"
            return outStr
        else:
            outStr += "  Baralho do jogo:\n"
            outStr += f' {"=":=>111}\n'
            for i in range(4):
                carta_cor = self.__inicio__
                nipe = f'{carta_cor.lista_de_naipes[i]}'
                outStr += f' |  Naipe {nipe}: [ '
                if carta_cor.getNaipe() == i:
                    outStr += f' {carta_cor.lista_de_posicoes[carta_cor.getPosicao()]}{carta_cor.lista_de_naipes[carta_cor.getNaipe()]} '
                while carta_cor.getProx() is not None:
                    carta_cor = carta_cor.getProx()
                    if carta_cor.getNaipe() == i:
                        outStr += f' {carta_cor.lista_de_posicoes[carta_cor.getPosicao()]}{carta_cor.lista_de_naipes[carta_cor.getNaipe()]} '
                outStr += f' ]  |\n'
            outStr += f' {"=":=>111}\n'

            outStr += f'  Total de cartas: {self.__numCartas__}'
            if self.__numCartas__ == 56:
                outStr += "   ->  Baralho completo!\n"
            else:
                outStr += "\n"
            return outStr

    # *******************************************************
    # *******************************************************
    """
    Retorna o valor do atributo que contém o total de número de 
    cartas do cBaralho.
    """
    def getNumCartas(self):
        return self.__numCartas__

    # *******************************************************
    # *******************************************************
    """
    Retorna a instância do tipo cCarta (se existir) da primeira
    carta do cBaralho.
    
    Caso o cBaralho esteja vazio, valor é "None".
    """
    def getInicio(self):
        return self.__inicio__

    # *******************************************************
    # *******************************************************
    """
    Gera um novo baralho universal com 56 cartas, incluindo 
    uma carta "Coringa" para cada "Naipe" do cBaralho.
    """
    def gerar_baralho(self):
        for naipe in range(4):
            for posicao in range(0, 14):
                self.insere_carta(posicao, naipe)
        return True

    # *******************************************************
    # *******************************************************
    """
    Remove todas as cartas da lista cBaralho e gera um novo 
    baralho completo.
    """
    def reiniciar_baralho(self):
        self.deletar_baralho()
        self.gerar_baralho()
        return True

    # *******************************************************
    # *******************************************************
    """ Remove todas as cartas da lista cBaralho. """
    def deletar_baralho(self):
        for i in range(self.__numCartas__):
            self.remove_ultima_carta()
        if self.__numCartas__ == 0:
            return True
        else:
            return False

    # *******************************************************
    # *******************************************************
    """
    Este módulo insere um atributo do tipo cCarta ao final
    da lista cBaralho.
    """
    def insere_carta(self, posicao, naipe):
        if 0 <= posicao < 14 and 0 <= naipe < 4:
            nova_carta = cCarta(posicao, naipe)
            if self.__inicio__ is None:
                self.__inicio__ = nova_carta
            else:
                carta_cor = self.__inicio__
                while carta_cor.getProx() is not None:
                    carta_cor = carta_cor.getProx()
                carta_cor.setProx(nova_carta)
                nova_carta.setAnterior(carta_cor)
            self.__numCartas__ += 1
            return True
        return False

    # *******************************************************
    # *******************************************************
    """
    Busca e retrona uma instancia do tipo cCarta contida no 
    cBaralho a partir dos seus atributos "posicao" e "naipe". 
    
    Caso não seja encontrada, retorna "False".
    """
    def buscar_carta(self, posicao, nipe):
        if self.__inicio__ is None:
            return False
        carta_cor = self.__inicio__
        while carta_cor.getProx() is not None:
            if carta_cor.getNaipe() == nipe and carta_cor.getPosicao() == posicao:
                return carta_cor
            carta_cor = carta_cor.getProx()
        if carta_cor.getNaipe() == nipe and carta_cor.getPosicao() == posicao:
            return carta_cor
        return False

    # *******************************************************
    # *******************************************************
    """
    Retorna uma instancia do tipo cCarta a partir do seu indice.
    
    Caso não seja encontrada, retorna "False".
    """
    def buscar_carta_indice(self, indice):
        if indice >= self.__numCartas__:
            return False
        carta_cor = self.__inicio__
        for i in range(indice):
            carta_cor = carta_cor.getProx()
        return carta_cor

    # *******************************************************
    # *******************************************************
    """
    Retorna o índice de uma de uma cCarta objeto da busca.
    
    Caso o índice extrapole o número de cartas contidas na lista
    cBaralho, retorna "False".
    """
    def indice(self, posicao, nipe):
        if self.__inicio__ is None:
            return False
        indice = 0
        carta_cor = self.__inicio__
        while carta_cor.getProx() is not None:
            if carta_cor.getNaipe() == nipe and carta_cor.getPosicao() == posicao:
                return indice
            carta_cor = carta_cor.getProx()
            indice += 1
        if carta_cor.getNaipe() == nipe and carta_cor.getPosicao() == posicao:
            return indice
        return False

    # *******************************************************
    # *******************************************************
    """
    Remove a instancia do tipo cCarta cujos atributos "posição"
    e "naipe" são passados como argumento.

    Caso não seja elemento da lista cBaralho, retorna "False".
    """
    def remove(self, posicao, nipe):
        if self.buscar_carta(posicao, nipe) is not False:
            carta_cor = self.buscar_carta(posicao, nipe)
            if carta_cor == self.__inicio__:
                self.remove_primeira_carta()
                return True
            if carta_cor.getProx() is None:
                self.remove_ultima_carta()
                return True
            carta_ante = carta_cor.getAnterior()
            carta_post = carta_cor.getProx()
            carta_ante.setProx(carta_post)
            carta_post.setAnterior(carta_ante)
            del carta_cor
            self.__numCartas__ -= 1
            return True
        return False

    # *******************************************************
    # *******************************************************
    """
    Remove o último elemento da lista cBaralho.

    Caso a lista esteja vazia, retorna "False".
    """
    def remove_ultima_carta(self):
        if self.__inicio__ is None:
            return False
        else:
            carta_cor = self.__inicio__
            carta_ant = None
            while carta_cor.getProx() is not None:
                carta_ant = carta_cor
                carta_cor = carta_cor.getProx()
            if carta_cor == self.__inicio__:
                del carta_cor
                self.__inicio__ = None
                self.__numCartas__ -= 1
                return True
            carta_ant.setProx(None)
            del carta_cor
            self.__numCartas__ -= 1
        return True

    # *******************************************************
    # *******************************************************
    """
    Remove o primeiro elemento da lista cBaralho.

    Caso a lista esteja vazia, retorna "False".
    """
    def remove_primeira_carta(self):
        if self.__inicio__ is None:
            return False
        carta_cor = self.__inicio__
        if carta_cor.getProx() is None:
            del carta_cor
            self.__inicio__ = None
            self.__numCartas__ -= 1
            return True
        carta_prox = carta_cor.getProx()
        carta_prox.setAnterior(None)
        self.__inicio__ = carta_prox
        del carta_cor
        self.__numCartas__ -= 1
        return True

    # *******************************************************
    # *******************************************************
    """ Remove os elemento "Coringas" da lista cBaralho. """
    def remover_coringas(self):
        for i in range(4):
            while self.buscar_carta(0, i):
                self.remove(0, i)

    # *******************************************************
    # *******************************************************
    """
     Este módulo retorna um "Agrupamento de cartas embaralhadas"
    a partir da reordenação de forma randômica das cartas contidas 
    no cBaralho para posterior uso em um jogo de carta que utilize
    um cBaralho.
    
    Caso o cBaralho esteja vazio, retorna "False".
    """
    def embaralhar(self):
        import random
        n_cartas = self.__numCartas__
        if self.__inicio__ is None:
            return False
        for i in range(self.__numCartas__ * 21):
            p = random.randrange(self.__inicio__.getPosicao(), self.__numCartas__)
            n = random.randrange(0, 4)
            q = random.randrange(self.__inicio__.getPosicao(), self.__numCartas__)
            m = random.randrange(0, 4)
            prim_carta = self.__inicio__
            self.remove_primeira_carta()
            self.insere_carta(prim_carta.getPosicao(), prim_carta.getNaipe())
            self.remove(p, n)
            self.insere_carta(p, n)
            prim_carta = self.__inicio__
            self.remove_primeira_carta()
            self.insere_carta(prim_carta.getPosicao(), prim_carta.getNaipe())
            self.remove(q, m)
            self.insere_carta(q, m)
            prim_carta = self.__inicio__
            self.remove_primeira_carta()
            self.insere_carta(prim_carta.getPosicao(), prim_carta.getNaipe())
        if n_cartas != self.__numCartas__:
            return False
        return True


# *******************************************************
# ***     Programa de teste da classe cCarta          ***
# *******************************************************
if __name__ == '__main__':
    baralho = cBaralho()
    print(type(baralho))
    print(baralho.__str__())
    print(baralho.__inicio__)
    print(baralho.getInicio())
    print(baralho.buscar_carta(3, 1))
    baralho.remove_ultima_carta()
    print(str(baralho))
    baralho.remove_primeira_carta()
    print(str(baralho))
    baralho.remove(3, 1)
    print(str(baralho))
    print(baralho.buscar_carta(3, 1))
    baralho.remover_coringas()
    print(str(baralho))
    baralho2 = cBaralho()
    baralho2.remover_coringas()
    print(str(baralho2))
    print(random.randrange(3, 4))
    baralho2.remover_coringas()
    monte = cACE()
    print(str(monte))
    baralho2.reiniciar_baralho()
    if baralho2.embaralhar():
        monte = baralho2.embaralhar()
    print(str(monte))
    print(baralho2.indice(2, 0))
    print(baralho2.buscar_carta_indice(8))
