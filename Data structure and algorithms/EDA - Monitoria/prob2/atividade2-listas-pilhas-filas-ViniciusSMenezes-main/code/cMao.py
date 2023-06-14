# ##################################################
#              Classe Mão                          #
# ##################################################
from cCarta import cCarta
from cBaralho import cBaralho
from cACE import cACE

# *******************************************************
""" "cMao" é uma classe baseada em lista duplamente encadeada para 
comportar o leque de cartas (da classe cCartas) de cada jogador"""


class cMao:

    # *******************************************************
    # *******************************************************
    def __init__(self):
        self.__inicio__ = None
        self.__numCartas__ = 0
        self.__apontador__ = None
        self.__apontador2__ = None

    # *******************************************************
    # *******************************************************
    def __str__(self):
        outStr = ""
        if self.__inicio__ is None:
            outStr += "  ===================\n"
            outStr += "  |   SEM CARTA     |\n"
            outStr += "  ===================\n"
            return outStr

        outStr += f'  Total de cartas: {self.__numCartas__}\n'
        for k in range(self.__numCartas__):
            if k == self.__apontador__ or k == self.__apontador2__:
                n = "\033[;1m"
                c = "\033[1;31m"
                r = "\033[0;0m"
            else:
                n = ""
                c = ""
                r = ""
            outStr += f'  {n}{c}{"":.^8}{" ":<1}{r}'
        carta_cor = self.__inicio__
        if self.indice(carta_cor.getPosicao(), carta_cor.getNaipe()) == self.__apontador__ :
            n = "\033[;1m"
            c = "\033[1;31m"
            r = "\033[0;0m"
        else:
            n = ""
            c = ""
            r = ""
        outStr += f'\n{n}{c}  |{carta_cor.lista_de_posicoes[carta_cor.getPosicao()]:<6}{"| ":>2}{r}'
        while carta_cor.getProx() is not None:
            carta_cor = carta_cor.getProx()
            if self.indice(carta_cor.getPosicao(), carta_cor.getNaipe()) == self.__apontador__:
                n = "\033[;1m"
                c = "\033[1;31m"
                r = "\033[0;0m"
            else:
                n = ""
                c = ""
                r = ""
            outStr += f'{n}{c}  |{carta_cor.lista_de_posicoes[carta_cor.getPosicao()]:<6}{"| ":>2}{r}'
        carta_cor = self.__inicio__
        if self.indice(carta_cor.getPosicao(), carta_cor.getNaipe()) == self.__apontador__:
            n = "\033[;1m"
            c = "\033[1;31m"
            r = "\033[0;0m"
        else:
            n = ""
            c = ""
            r = ""
        outStr += f'\n   {n}{c}{carta_cor.lista_de_naipes[carta_cor.getNaipe()]:^6}{r}{"":<2}'
        while carta_cor.getProx() is not None:
            carta_cor = carta_cor.getProx()
            if self.indice(carta_cor.getPosicao(), carta_cor.getNaipe()) == self.__apontador__:
                n = "\033[;1m"
                c = "\033[1;31m"
                r = "\033[0;0m"
            else:
                n = ""
                c = ""
                r = ""
            outStr += f'   {n}{c}{carta_cor.lista_de_naipes[carta_cor.getNaipe()]:^6}{r}{"":<2}'
        carta_cor = self.__inicio__
        if self.indice(carta_cor.getPosicao(), carta_cor.getNaipe()) == self.__apontador__:
            n = "\033[;1m"
            c = "\033[1;31m"
            r = "\033[0;0m"
        else:
            n = ""
            c = ""
            r = ""
        outStr += f'\n{n}{c}  |{carta_cor.lista_de_posicoes[carta_cor.getPosicao()]:>6}{"| ":>2}{r}'
        while carta_cor.getProx() is not None:
            carta_cor = carta_cor.getProx()
            if self.indice(carta_cor.getPosicao(), carta_cor.getNaipe()) == self.__apontador__:
                n = "\033[;1m"
                c = "\033[1;31m"
                r = "\033[0;0m"
            else:
                n = ""
                c = ""
                r = ""
            outStr += f'{n}{c}  |{carta_cor.lista_de_posicoes[carta_cor.getPosicao()]:>6}{"| ":>2}{r}'
        outStr += f'\n'
        for m in range(self.__numCartas__):
            if m == self.__apontador__:
                n = "\033[;1m"
                c = "\033[1;31m"
                r = "\033[0;0m"
            else:
                n = ""
                c = ""
                r = ""
            outStr += f'  {n}{c}{"":¨^8} {r}'
        outStr += "\n"
        for j in range(self.__numCartas__):
            if j == self.__apontador__:
                n = "\033[;1m"
                c = "\033[1;31m"
                r = "\033[0;0m"
            else:
                n = ""
                c = ""
                r = ""
            outStr += f'  {n}{c}{j:^8} {r}'
        outStr += ""
        return outStr

    # *******************************************************
    def imprime_beta(self):
        outStr = ""
        if self.__inicio__ is None:
            outStr += f'{"":_>25}\n'
            outStr += f'| Cartas:  -> {"Vazio":^4} <-  |\n'
            outStr += f'{"":¨>25}\n'
            return outStr
        else:
            outStr += f'Total de cartas: {self.__numCartas__}\n'
            outStr += f'{"":_>280}\n'
            outStr += f'| Cartas: ->'
            carta_cor = self.__inicio__
            if self.indice(carta_cor.getPosicao(), carta_cor.getNaipe()) == self.__apontador__:
                n = "\033[;1m"
                c = "\033[1;31m"
                r = "\033[0;0m"
            else:
                n = ""
                c = ""
                r = ""
            outStr += f' {n}{c}{carta_cor.lista_de_posicoes[carta_cor.getPosicao()]:^1}{r}'
            outStr += f'{n}{c}{carta_cor.lista_de_naipes[carta_cor.getNaipe()]:<3}{r} '
            while carta_cor.getProx() is not None:
                carta_cor = carta_cor.getProx()
                if self.indice(carta_cor.getPosicao(), carta_cor.getNaipe()) == self.__apontador__:
                    n = "\033[;1m"
                    c = "\033[1;31m"
                    r = "\033[0;0m"
                else:
                    n = ""
                    c = ""
                    r = ""
                outStr += f' {n}{c}{carta_cor.lista_de_posicoes[carta_cor.getPosicao()]:<1}{r}'
                outStr += f'{n}{c}{carta_cor.lista_de_naipes[carta_cor.getNaipe()]:<3}{r} '
            outStr += f'{"<-":>3}\n'
            outStr += f'{"":¨>280}'
            return outStr

    # *******************************************************
    # *******************************************************
    """
    Retorna o valor do atributo apontador "Apontador". 
    """
    def getApontador(self, i=0):
        if i == 1:
            return self.__apontador2__
        return self.__apontador__

    # *******************************************************
    # *******************************************************
    """
    Modifica e retorna o valor do atributo apontador para auxiliar
    na indicação da carta apontada pelo indice da lista do tipo cMao.
    
    Caso o indice exceda o numero de cartas da lista, retorna "False". 
    """
    def setApontador(self, a, i=0):
        if a <= self.__numCartas__:
            if i == 1:
                self.__apontador2__ = a
                return self.__apontador2__
            self.__apontador__ = a
            return self.__apontador__
        return False

    # *******************************************************
    # *******************************************************
    """
    Altera o atributo apontador para valor "None". 
    """
    def clearApontador(self, i=0):
        if i == 1:
            self.__apontador2__ = None
            return True
        self.__apontador__ = None
        return True

    # *******************************************************
    # *******************************************************
    """
    Retorna o valor do atributo que contém o total de número de 
    cartas da cMao.
    """
    def getNumCartas(self):
        return self.__numCartas__

    # *******************************************************
    # *******************************************************
    """ Retorna o valor verdadeiro de lista cMao está vazia."""
    def empty(self):
        return self.__numCartas__ == 0

    # *******************************************************
    # *******************************************************
    """
        Retorna a instância do tipo cCarta (se existir) da primeira
        carta da cMao.

        Caso a cMao esteja vazia, valor é "None"
        """
    def getInicio(self):
        return self.__inicio__

    # *******************************************************
    # *******************************************************
    """
    Este módulo insere um atributo do tipo cCarta ao final
    da lista cMao.
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
    Este módulo insere um atributo do tipo cCarta no início
    da lista cMao.
     """
    def insere_carta_inicio(self, posicao, naipe):
        if 0 <= posicao < 14 and 0 <= naipe < 4:
            nova_carta = cCarta(posicao, naipe)
            carta_co = self.__inicio__
            carta_co.setAnterior(nova_carta)
            nova_carta.setProx(carta_co)
            self.__inicio__ = nova_carta
            self.__numCartas__ += 1
            return True
        return False

    # *******************************************************
    # *******************************************************
    """
    Busca e retrona uma instancia do tipo cCarta contida na 
    lista cMao a partir dos seus atributos "posicao" e "naipe". 

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

    Caso o indice extrapole o número de cartas contidas na lista
    cMao, retorna "False".
    """
    def buscar_carta_indice(self, indice):
        if indice >= self.__numCartas__:
            return False
        carta_cor = self.__inicio__
        for a in range(indice):
            carta_cor = carta_cor.getProx()
        return carta_cor

    # *******************************************************
    # *******************************************************
    """
    Retorna o indice de uma de uma cCarta objeto da busca.

    Caso não esteja contida na lista, retorna "False".
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

    # ************************************************************************************************************
    # ************************************************************************************************************
    """Busca carta que forma par com a carta argumento e retorna a carta par, se houver."""
    def busca_par(self, posicao, naipe):
        if naipe // 2 > 0:
            if naipe == 2:
                indice_carta = self.indice(posicao, 0)
            else:
                indice_carta = self.indice(posicao, 1)
        else:
            if naipe == 0:
                indice_carta = self.indice(posicao, 2)
            else:
                indice_carta = self.indice(posicao, 3)

        if indice_carta is not False:
            carta = self.buscar_carta_indice(indice_carta)
            return carta
        return False

    # ************************************************************************************************************
    # ************************************************************************************************************
    """Busca carta que forma par com a carta argumento passada e retorna o indice da carta que forma par, se houver."""
    def busca_par_indice(self, posicao, naipe):
        if naipe // 2 > 0:
            if naipe == 2:
                indice_carta = self.indice(posicao, 0)
            else:
                indice_carta = self.indice(posicao, 1)
        else:
            if naipe == 0:
                indice_carta = self.indice(posicao, 2)
            else:
                indice_carta = self.indice(posicao, 3)

        if indice_carta is not False:
            return indice_carta
        return False

    # ************************************************************************************************************
    # ************************************************************************************************************
    """Busca as cartas que formam par na lista cMao, remove estas cartas, se existirem. Se existirem retorna uma 
    pilha do tipo cMao, retorna a pilha vazia."""
    def remove_par(self):
        lixo = cACE(self.__numCartas__)
        carta_cor = self.__inicio__
        while carta_cor.getProx() is not None:
            carta = self.busca_par(carta_cor.getPosicao(), carta_cor.getNaipe())
            if carta is not False:
                lixo.push(carta_cor)
                lixo.push(carta)
                carta_aterior = carta_cor
                carta_cor = carta_cor.getProx()
                # if carta_cor == carta:
                self.remove_carta(carta_aterior.getPosicao(), carta_aterior.getNaipe())
                self.remove_carta(carta.getPosicao(), carta.getNaipe())
            else:
                carta_cor = carta_cor.getProx()
        if not lixo.empty():
            return lixo
        return lixo

    # *******************************************************
    # *******************************************************
    """
    Remove a instancia do tipo cCarta cujos atributos "posição"
    e "naipe" são passados como argumento.

    Caso não seja elemento da lista cMao, retorna "False".
    """
    def remove_carta(self, posicao, nipe):
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

    # **********************************************************************************************************
    # ************************************************************************************************************
    """
    Remove o último elemento da lista cMao.

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
    def remove_indice(self, indice):
        carta_cor = self.buscar_carta_indice(indice)
        if carta_cor is not False:
            if carta_cor == self.__inicio__:
                self.remove_primeira_carta()
                return carta_cor
            if carta_cor.getProx() is None:
                self.remove_ultima_carta()
                return carta_cor
            carta_ante = carta_cor.getAnterior()
            carta_post = carta_cor.getProx()
            carta_ante.setProx(carta_post)
            carta_post.setAnterior(carta_ante)
            del carta_cor
            self.__numCartas__ -= 1
            return True
        return False


# *******************************************************
# ***     Programa de teste da classe cCarta          ***
# *******************************************************

if __name__ == '__main__':

    baralho = cBaralho()
    print(type(baralho))
    baralho.remover_coringas()

    monte = cACE(baralho.getNumCartas())
    carta_cor = baralho.getInicio()
    monte.push(carta_cor)
    while carta_cor.getProx() is not None:
        monte.push(carta_cor.getProx())
        carta_cor = carta_cor.getProx()

    aux = cCarta()
    print(str(monte))
    jogador1 = cMao()
    jogador2 = cMao()
    print(type(jogador1))
    print(type(monte))
    print(type(aux))
    while not monte.empty():
        aux = monte.pop()
        jogador1.insere_carta(aux.getPosicao(), aux.getNaipe())
        jogador2.insere_carta(aux.getPosicao(), aux.getNaipe())
    print(str(jogador1))
    print(str(jogador2))
    teste = cMao()

    print(teste.imprime_beta())
    jogador2.setApontador(3)
    print(str(jogador2))
    print(jogador2.imprime_beta())
    jogador2.clearApontador()
    print(str(jogador2))
    print(jogador2.imprime_beta())
    lixo = jogador2.remove_par()
    print(lixo)
    print(jogador2.imprime_beta())
