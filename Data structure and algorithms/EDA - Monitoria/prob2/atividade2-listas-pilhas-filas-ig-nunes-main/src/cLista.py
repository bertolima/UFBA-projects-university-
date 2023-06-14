# ############################################################
# Classe que implementa uma Lista Simplesmente Encadeada - LSE
# ############################################################

import cNo



# *******************************************************
# ***                                                 ***
# *******************************************************
class cLista:

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    def __init__(self):
        self.__inicio__ = None
        self.__numElems__ = 0

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    def getTamanho(self):
        return self.__numElems__

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    def __str__(self):

        outStr = ""

        if self.__inicio__ == None:
            outStr += "=====================\n"
            outStr += "|   LISTA   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            noCor = self.__inicio__
            outStr += "["
            while noCor is not None:
                outStr += f"{noCor.__dado__}, "
                noCor = noCor.__prox__
            outStr = outStr[:-2]
            outStr += "]"

        return outStr

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    # Insere nó no Fim
    def insereNo(self, n):
        novoNo = cNo.cNo(n)

        if self.__inicio__ is None:
            self.__inicio__ = novoNo
        else:
            noCor = self.__inicio__

            while noCor.__prox__ is not None:
                noCor = noCor.__prox__

            noCor.__prox__ = novoNo
        self.__numElems__ += 1
        return True

    # Inserir nó no inicio:
    def insereIni(self, n):
        novoNo = cNo.cNo(n)

        if self.__inicio__ is None:
            self.__inicio__ = novoNo
        else:
            noCor = self.__inicio__
            self.__inicio__ = novoNo
            novoNo.__prox__ = noCor
        self.__numElems__ += 1
        return True


    # Busca pela posição:
    def buscaDadoPos(self, pos):
        if self.__inicio__ is None:
            return -1
        if pos >= self.__numElems__ or pos < 0:
            return -1
        noCor = self.__inicio__
        for i in range(pos):
            noCor = noCor.__prox__
        return noCor
        # return noCor.__dado__

    # *******************************************************
    # ***                                                 ***
    # *******************************************************
    # Remove Nó a partir de posição
    def removePos(self, pos):
        if self.__inicio__ is None:
            return False
        elif pos >= self.__numElems__:
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
            # del noAnt

            self.__numElems__ -= 1
            return noAnt

        if noCor is None:
            noAnt.__prox__ = noCor
            self.__numElems__ -= 1

            return noAnt

        noAnt.__prox__ = noCor.__prox__

        # del noCor
        self.__numElems__ -= 1
        return noCor

    # Remove Nó a partir de dado
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
            del noAnt
            return True
        if noCor is None:
            return False

        noAnt.__prox__ = noCor.__prox__

        self.__numElems__ -= 1
        return noCor

    # Remove Nó no inicio ou no fim
    def removeNoIniFim(self, ini=True):
        if self.__inicio__ is None:
            return False
        noCor = self.__inicio__
        noAnt = noCor
        if self.__numElems__ == 1:
            self.__inicio__ = None
            del noCor
            return True
        if ini:
            noCor = noCor.__prox__
            self.__inicio__ = noCor
            del noAnt
            return True
        else:
            while noCor.__prox__ is not None:
                noAnt = noCor
                noCor = noCor.__prox__
            noAnt.__prox__ = None
            del noCor
            return True


# *******************************************************
# ***                                                 ***
# *******************************************************

if __name__ == '__main__':
    lista = cLista()

    print(lista)


    print(lista.insereNo(40))
    print(lista.insereNo(10))
    print(lista.insereNo(78))
    # print(lista.insereNo(78))
    # print(lista.insereNo(20))
    # print(lista.insereNo(30))
    # print(lista.insereNo(100))

    #
    #
    #
    # lista.insereIni(40)
    # lista.insereIni(40)
    # lista.insereIni(40)
    # lista.insereIni(10)
    # lista.insereIni(78)
    # lista.insereIni(20)
    # lista.insereIni(30)
    # lista.insereIni(100)

    # if lista.buscaDado(10):
    #     print("Busca com sucesso")
    # else:
    #     print("Busca sem sucesso")

    # print(lista.buscaDado(80))

    print(lista)
    print(lista.getTamanho())

    lista.removePos(0)
    lista.removePos(0)
    lista.removePos(0)
    # lista.removePos(1)

    print(lista)
    print(lista.getTamanho())

    # if lista.removeNo(40):
    #     print("Remoção com sucesso")
    # else:
    #     print("Remoção sem sucesso")

    # print(lista)

    # print(lista.buscaDadosIguais(50).buscaDadoPos(0))
    #
    # print(lista.buscaDadoPos(3))

    # lista.removeNoIniFim(ini=True)
    # print(lista)
    #
    # lista.removeNoIniFim(ini=False)
    # print(lista)

    # print(lista.removePos(3))
    # print(lista)
