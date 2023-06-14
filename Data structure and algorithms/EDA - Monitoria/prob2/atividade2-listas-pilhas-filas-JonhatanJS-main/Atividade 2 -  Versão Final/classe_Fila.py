# Lab 08 - Pilhas e Filas
# Criando uma Classe Fila

from classe_No import cNo

# *******************************************************
# ***                                                 ***
# *******************************************************
class cFila:

# *******************************************************
    def __init__(self):
        self._inicio     = None
        self._fim        = None
        self._numElems   = 0

# *******************************************************
    def size(self):
        return self._numElems

# *******************************************************
    def queue(self, n):

        novoNo = cNo(n)

        if self._inicio == None:
            self._inicio = novoNo
            self._fim    = novoNo
            self._numElems += 1
        else:
            self._fim.setProx(novoNo)
            self._fim = novoNo
            self._numElems += 1

# *******************************************************
    def dequeue(self):

        if self._inicio == None:
            return False, None

        noCorrente = self._inicio

        self._inicio = noCorrente.getProx()

        dado = noCorrente.getDado()

        del noCorrente

        self._numElems -= 1

        return True, dado

# *******************************************************
    def empty(self):
        return self._inicio == None

# *******************************************************
    def size(self):
        return self._numElems
    
    def __str__(self):
        elementos = []
        noCorrente = self._inicio
        while noCorrente:
            elementos.append(str(noCorrente.getDado()))
            noCorrente = noCorrente.getProx()
        return ', '.join(elementos)

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    numElementos = 10

    fila = cFila()

    i=100
    while( numElementos > 0):
        fila.queue(i)
        print(f'++ {i}')
        i += 3
        numElementos -= 1

    while(not fila.empty()):
        i = fila.dequeue()
        print(f'-- {i}')
