# Pilhas e Filas
# Criando uma Classe Fila

import cNo

# *******************************************************
# ***                                                 ***
# *******************************************************
class cFila:

# *******************************************************
    def __init__(self):
        self.__inicio__ = None
        self.__numElems__ = 0
        self.__fim__ = None
        return

# *******************************************************
    def __str__(self):
        outStr = ""

        if self.__inicio__ == None:
            outStr += "=====================\n"
            outStr += "|   Fila   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            noCor = self.__inicio__
            outStr = "["
            while noCor is not None:
                outStr += f"{noCor.__dado__}, "
                noCor = noCor.__prox__
            outStr = outStr[:-2]
            outStr += "]"

        return outStr

# *******************************************************
    def size(self):
        return

# *******************************************************
    def queue(self, n):
        noNovo = cNo.cNo(n)
        if self.__inicio__ is None:
            self.__inicio__ = noNovo
        else:
            fim = self.__fim__
            fim.__prox__ = noNovo

        self.__numElems__ += 1
        self.__fim__ = noNovo
        return


# *******************************************************
    def dequeue(self):
        if self.empty():
            return False
        if self.__inicio__ == self.__fim__:
            self.__fim__ = None
        noCor = self.__inicio__
        dadoRetornado = noCor.__dado__
        self.__inicio__ = noCor.__prox__
        del noCor
        self.__numElems__ -= 1
        return dadoRetornado

# *******************************************************
    def empty(self):
        return self.__numElems__ == 0


# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    fila = cFila()
    print(fila)
    print(f'Está vazio: {fila.empty()}')
    print(fila.__numElems__)
    # print(fila.__fim__)

    i=20
    while i > 0:
        fila.queue(i)
        print(f'++ {i}')
        i -= 3

    print(fila)
    print(f'Está vazio: {fila.empty()}')
    print(fila.__numElems__)
    # print(fila.__fim__)

    while not fila.empty():
        j = fila.dequeue()
        print(fila)
        print(f'Está vazio: {fila.empty()}')
        print(f'-- {j}')

    # print(fila)
    # print(f'Está vazio: {fila.empty()}')
    # print(fila.__numElems__)
    # # print(fila.__fim__)
