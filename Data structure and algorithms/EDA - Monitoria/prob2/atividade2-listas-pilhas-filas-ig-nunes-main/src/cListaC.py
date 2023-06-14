import cNo as cNo
import cJogador

class cListaC:
    def __init__(self):
        self.__inicio__ = None
        self.__fim__ = None
        self._numeroElementos = 0

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    def getTamanho(self):
        return self._numeroElementos

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    def __str__(self):

        outStr = ""

        if self.__inicio__ is None:
            outStr += "=====================\n"
            outStr += "|   LISTA   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            noCor = self.__inicio__
            outStr = "["
            while noCor.__prox__ != self.__inicio__:
                outStr += f"{noCor.__dado__}, "
                noCor = noCor.__prox__

            outStr += f"{noCor.__dado__}]"

        return outStr

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    # Insere nó no Fim
    def insereNo(self, n):
        novoNo = cNo.cNo(n)

        if self.__inicio__ is None:
            self.__inicio__ = novoNo
            novoNo.__prox__ = self.__inicio__
            self.__fim__ = self.__inicio__


        else:
            noCor = self.__inicio__

            while noCor.__prox__ != self.__inicio__:
                noCor = noCor.__prox__

            noCor.__prox__ = novoNo
            novoNo.__prox__ = self.__inicio__
            self.__fim__ = novoNo
        self._numeroElementos += 1
        # self.__cursor__ = self.__inicio__
        return True

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    def inserePos(self, pos, n):
        novoNo = cNo.cNo(n)

        if self.__inicio__ is None:
            self.__inicio__ = novoNo
            novoNo.__prox__ = self.__inicio__
            self.__fim__ = self.__inicio__

        if pos >= self._numeroElementos or pos < 0:
            return False

        noAnt = None
        noCor = self.__inicio__
        cont = 0
        while cont != pos:
            noAnt = noCor
            noCor = noCor.__prox__
            cont += 1

        if cont == 0:
            novoNo.__prox__ = noCor
            self.__inicio__ = novoNo
            self.__fim__.__prox__ = novoNo

        elif cont < self._numeroElementos - 1:
            novoNo.__prox__ = noCor
            noAnt.__prox__ = novoNo
        else:
            novoNo.__prox__ = self.__inicio__
            noCor.__prox__ = novoNo

        self._numeroElementos += 1
        return True

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    def buscaDadoPos(self, pos):
        if self.__inicio__ is None:
            return -1
        if pos >= self._numeroElementos or pos < 0:
            return -1
        noCor = self.__inicio__
        for i in range(pos):
            noCor = noCor.__prox__
        return noCor

    # *******************************************************
    # ***                                                 ***
    # *******************************************************

    def removePos(self, pos):
        if self.__inicio__ is None:
            return False
        elif pos >= self._numeroElementos:
            return False
        noAnt = None
        noCor = self.__inicio__
        cont = 0
        while cont != pos:
            noAnt = noCor
            noCor = noCor.__prox__
            cont += 1

        if cont == 0:
            noAnt = noCor
            self.__inicio__ = noCor.__prox__
            self.__fim__.__prox__ = self.__inicio__
            # del noAnt
            self._numeroElementos -= 1
            return noAnt

        if noCor is None:
            noAnt.__prox__ = noCor
            self._numeroElementos -= 1
            return noAnt

        noAnt.__prox__ = noCor.__prox__

        self._numeroElementos -= 1
        return noCor

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    # Remover Nó
    def removeNo(self, n):
        if self.__inicio__ is None:
            return False
        noAnt = None
        noCor = self.__inicio__
        cont = 0
        while noCor is not None and noCor.__dado__ != n:
            cont += 1
            noAnt = noCor
            noCor = noCor.__prox__

        if cont == 0:
            noAnt = noCor
            self.__inicio__ = noCor.__prox__
            self.__fim__.__prox__ = self.__inicio__
            # del noAnt
            self._numeroElementos -= 1
            return noAnt
        if noCor is None:
            return False

        if cont == self.getTamanho() - 1:
            noAnt.__prox__ = self.__inicio__
            self.__fim__ = noAnt
            self._numeroElementos -= 1
            return noCor
        noAnt.__prox__ = noCor.__prox__

        self._numeroElementos -= 1
        return noCor


if __name__ == '__main__':
    lista = cListaC()

    # lista.insereNo(40)
    # lista.insereNo(70)
    # lista.insereNo(60)
    # lista.insereNo(10)
    # lista.insereNo(90)
    # lista.insereNo(30)
    # lista.insereNo(20)
    # lista.insereNo(800)

    lista.insereNo(cJogador.cJogador("igor"))
    lista.insereNo(cJogador.cJogador("fernanda"))
    lista.insereNo(cJogador.cJogador("maya"))
    lista.insereNo(cJogador.cJogador("hannay"))
    lista.insereNo(cJogador.cJogador("remy"))

    print(lista)
    # print(lista.__inicio__)
    # print(lista.__inicio__.__prox__)
    # print(lista.__fim__)
    # print(lista.__fim__.__prox__)
    # obj = lista.buscaDadoPos(0)
    # print(obj)

    lista.removePos(0)

    print(lista)

    # lista.inserePos(0, 100)

    # print(lista.__fim__.__prox__)

    # lista.inserePos(0, 100)
    # print(lista)

    # lista.removeNo(100)
    # lista.removeNo(100)
    # lista.removeNo(40)
    # lista.removeNo(90)

    # print(lista)
    # print(lista.__fim__)
    # print(lista.__fim__.getProx())

    # lista.removePos(8)
    # lista.removePos(7)
    # lista.removePos(0)
    # [100, 40, 70, 60, 10, 90, 30]
    # [40, 70, 60, 10, 90, 30, 100]
    # print(lista)

    # lista.removePos(0)

    # print(lista.__fim__.__prox__)
    # print(lista)
