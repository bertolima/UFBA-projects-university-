# ##################################################
#              Classe cCarta                       #
# ##################################################

class cCarta:

    # *******************************************************
    # *******************************************************
    def __init__(self, posicao=0, naipe=0):
        self.__naipe__ = naipe
        self.__posicao__ = posicao
        self.__proximo__ = None
        self.__anterior__ = None
        self.lista_de_naipes = ["(♥)", "(♠)", "(♦)", "(♣)"]
        self.lista_de_posicoes = ["Joker", "A", "2", "3", "4", "5", "6", "7",
                                  "8", "9", "10", "J", "Q", "K"]

    # *******************************************************
    # *******************************************************
    def __str__(self):
        if self.__posicao__ == 0:
            outStr = "\n"
            outStr += f' {"":.^9}\n'
            outStr += f' | {self.lista_de_posicoes[self.__posicao__]:4} |\n'
            outStr += f' |  {self.lista_de_naipes[self.__naipe__]:^4} |\n'
            outStr += f' | {self.lista_de_posicoes[self.__posicao__]:4} |\n'
            outStr += f' {"":¨>9}'
            return outStr
        outStr = ""
        outStr += f'  {"":.^9}\n'
        outStr += f'  | {self.lista_de_posicoes[self.__posicao__]:<5} |\n'
        outStr += f'  | {self.lista_de_naipes[self.__naipe__]:^5} |\n'
        outStr += f'  | {self.lista_de_posicoes[self.__posicao__]:>5} |\n'
        outStr += f'  {"":¨>9}\n'
        return outStr

    # *******************************************************
    # *******************************************************
    def imprime_beta(self):
        outStr = f' {self.lista_de_posicoes[self.__posicao__]}{self.lista_de_naipes[self.__naipe__]}\n'
        return outStr

    # *******************************************************
    # *******************************************************
    def setProx(self, prox):
        if type(prox) == cCarta:
            self.__proximo__ = prox
        else:
            self.__proximo__ = None

    # *******************************************************
    # *******************************************************
    def setAnterior(self, anterior):
        if type(anterior) == cCarta:
            self.__anterior__ = anterior
        else:
            self.__anterior__ = None

    # *******************************************************
    # *******************************************************
    def getNaipe(self):
        return self.__naipe__

    # *******************************************************
    # *******************************************************
    def getPosicao(self):
        return self.__posicao__

    # *******************************************************
    # *******************************************************
    def getProx(self):
        return self.__proximo__

    # *******************************************************
    # *******************************************************
    def getAnterior(self):
        return self.__anterior__


# *******************************************************
# ***         Programa de teste                       ***
# *******************************************************


if __name__ == '__main__':
    carta = cCarta(1, 3)
    print(carta.__str__())
