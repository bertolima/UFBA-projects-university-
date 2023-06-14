
import cCarta

# *******************************************************
# ***                                                 ***
# *******************************************************


class cFila:

    # *******************************************************
    def __init__(self):
        self.__inicio__ = None
        self.__fim__ = None
        self.__numElems__ = 0

# *******************************************************
    def size(self):
        return self.__numElems__

# *******************************************************
    def queue(self, nova_carta):
        if self.__inicio__ is None:
            self.__inicio__ = nova_carta
            self.__fim__ = nova_carta
        else:
            nova_carta.setAnterior(self.__fim__)
            self.__fim__.setProx(nova_carta)
            self.__fim__ = nova_carta
            self.__numElems__ += 1

    # *******************************************************
    def dequeue(self):
        if self.__numElems__ == 0:
            self.__inicio__ = None
            return False
        carta_cor = self.__inicio__
        self.__inicio__ = carta_cor.getProx()
        self.__inicio__.setAnterior(None)
        dado = carta_cor
        del carta_cor
        self.__numElems__ -= 1
        print(self.__inicio__)
        return dado

    # *******************************************************
    def empty(self):
        if self.__inicio__ is None:
            return True
        return False

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':
    numElementos = 10
    fila = cFila()
    carta = cCarta.cCarta()

    while numElementos > 0:
        fila.queue(carta)
        print(f'++ {carta}')
        numElementos -= 1

    while not fila.empty():
        i = fila.dequeue()
        print(f'-- {i}')
