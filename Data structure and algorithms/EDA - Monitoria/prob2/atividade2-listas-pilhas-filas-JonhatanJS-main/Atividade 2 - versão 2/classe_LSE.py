from classe_No import cNo
import random
class cLSE:
    def __init__(self):
        self.__inicio__ = None
        self.__numElems__ = 0

    def getTamanho(self):
        return self.__numElems__

    def __str__(self):
        outStr = ""

        if self.__inicio__ == None:        
            outStr += "=====================\n"
            outStr += "|   LISTA   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            atual = self.__inicio__
            while atual is not None:
                outStr += str(atual.__dado__) + " "
                atual = atual.__prox__
            outStr += "\n"

        return outStr

    def insereNo(self, n):
        novo_no = cNo(n)
        if self.__inicio__ is None:
            self.__inicio__ = novo_no
        else:
            novo_no.__prox__ = self.__inicio__
            self.__inicio__ = novo_no
        self.__numElems__ += 1
        return True

    def buscaDado(self, n):
        atual = self.__inicio__
        while atual is not None:
            if atual.__dado__ == n:
                return True
            atual = atual.__prox__
        return False

    def removeNo(self, n):
        if self.__inicio__ is None:
            return False

        if self.__inicio__.__dado__ == n:
            self.__inicio__ = self.__inicio__.__prox__
            self.__numElems__ -= 1
            return True

        atual = self.__inicio__
        while atual.__prox__ is not None:
            if atual.__prox__.__dado__ == n:
                atual.__prox__ = atual.__prox__.__prox__
                self.__numElems__ -= 1
                return True
            atual = atual.__prox__

        return False        
    def RemoveNoAleatorio(self):
            if self.__inicio__==None:
                return None

            posicao = random.randint(0, self.__numElems__ - 1)

            if posicao == 0:
                removido = self.__inicio__
                self.__inicio__ = self.__inicio__.__prox__
            else:
                anterior = None
                atual = self.__inicio__
                for _ in range(posicao):
                    anterior = atual
                    atual = atual.__prox__
                removido = atual
                anterior.__prox__ = atual.__prox__

            self.__numElems__ -= 1
            removido.__prox__ = None
            return removido

if __name__ == '__main__':
    lista = cLSE()

    print(lista)

    lista.insereNo(40)
    lista.insereNo(10)
    lista.insereNo(78)

    if lista.buscaDado(10):
        print("Busca com sucesso")
    else:
        print("Busca sem sucesso")

    if lista.removeNo(78):
        print("Remoção com sucesso")
    else:
        print("Remoção sem sucesso")

    print(lista)