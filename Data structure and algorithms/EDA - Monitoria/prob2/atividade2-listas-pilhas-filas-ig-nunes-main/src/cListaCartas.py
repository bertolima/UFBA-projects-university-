import cLista
import cCarta
import cNo
from utils import *


# Herança da TAD cLista
# cListaCartas é uma lista ordenada (adaptada para cartas)
class cListaCartas(cLista.cLista):
    def __init__(self):
        super().__init__()

    # Override
    def __str__(self):

        outStr = ""

        if self.__inicio__ == None:
            outStr += "Mão Vazia!"
        else:
            noCor = self.__inicio__
            outStr += "["
            while noCor is not None:
                outStr += f"{noCor.__dado__}, "
                noCor = noCor.__prox__
            outStr = outStr[:-2]
            outStr += "]"

        return outStr

    def insereCartasOrd(self, n):
        novoNo = cNo.cNo(n)

        if self.__inicio__ is None:
            self.__inicio__ = novoNo

        else:
            noAnt = None
            noCor = self.__inicio__
            while noCor is not None and noCor.__dado__.getCarta() < novoNo.__dado__.getCarta():
                noAnt = noCor
                noCor = noCor.__prox__

            if noAnt is None and noCor.__dado__.getCarta() >= novoNo.__dado__.getCarta():  # Caso seja no primeiro
                self.__inicio__ = novoNo
                novoNo.__prox__ = noCor

            elif noCor is None:  # Caso seja o último
                noAnt.__prox__ = novoNo

            elif noCor.__dado__.getCarta() >= novoNo.__dado__.getCarta():

                novoNo.__prox__ = noCor
                noAnt.__prox__ = novoNo
            # elif novoNo.__dado__ <= no

            else:
                return None

        self.__numElems__ += 1
        return True

    def buscaDado(self, n):
        if self.__inicio__ is None:
            return -1

        noCor = self.__inicio__
        position = 0

        while noCor is not None and noCor.__dado__.getCarta() != n:
            noCor = noCor.__prox__
            position += 1

        if noCor is None:
            return -1

        return noCor.__dado__.imprimirCarta(), position

    def buscaDadosIguais(self):
        if self.__inicio__ is None:
            return -1

        paresIguais = cListaCartas()
        encontrado = False
        cont = 1

        while cont != 0:
            cont = 0
            posicao = 0
            noCor = self.__inicio__

            while noCor is not None and noCor.__prox__ is not None:
                if noCor.getDado().getCarta() == noCor.getProx().getDado().getCarta():
                    # Caso queira imprimir os pares encontrados
                    # print(f"Par de cartas encontrado: {noCor.getDado().getCarta()}")
                    encontrado = True
                    cont = 1
                    break

                posicao += 1
                noCor = noCor.__prox__
            if cont == 1:
                a = self.removePos(posicao)
                b = self.removePos(posicao)
                paresIguais.insereNo(a.getDado())
                paresIguais.insereNo(b.getDado())

        # Indicar se foi encontrado algum par
        if encontrado:
            print(f"{BOLD}Alguns pares foram encontrados{RESET}")

        return paresIguais


if __name__ == '__main__':
    lista = cListaCartas()

    lista.insereCartasOrd(cCarta.carta(40, 'heart'))
    lista.insereCartasOrd(cCarta.carta(40, 'heart'))
    lista.insereCartasOrd(cCarta.carta(10, 'heart'))
    lista.insereCartasOrd(cCarta.carta(10, 'heart'))
    lista.insereCartasOrd(cCarta.carta(20, 'heart'))
    lista.insereCartasOrd(cCarta.carta(20, 'heart'))
    lista.insereCartasOrd(cCarta.carta(60, 'heart'))
    lista.insereCartasOrd(cCarta.carta(50, 'heart'))
    lista.insereCartasOrd(cCarta.carta(50, 'heart'))
    lista.insereCartasOrd(cCarta.carta(50, 'heart'))
    lista.insereCartasOrd(cCarta.carta(50, 'heart'))
    lista.insereCartasOrd(cCarta.carta(30, 'heart'))
    lista.insereCartasOrd(cCarta.carta(30, 'heart'))
    lista.insereCartasOrd(cCarta.carta(60, 'heart'))

    print(lista)
    # print(lista.getTamanho())

    # print(lista.buscaDado(40))

    # print(type(lista.removePos(1)))
    #
    print(lista)
    # print(lista.getTamanho())

    obj = lista.buscaDadosIguais()

    print(lista)
    print(obj)
    # print(lista.getTamanho())
