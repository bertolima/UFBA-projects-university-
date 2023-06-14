import cNo
class cCartas:
    def __init__(self):
        self.__inicio__ = cNo.cNo()
        self.monte = []
        self.numCartas = 0
        self.numMonte = 0

    def __str__(self):
        outStr = "[ "

        noAtual = self.__inicio__
        elementos = []

        while noAtual.__prox__ is not None:
            noAtual = noAtual.__prox__
            dado = [noAtual.__dado__]
            elementos += dado
        if self.numCartas == 0:
            outStr += "Jogador Sem Cartas ]"
        else:
            for i in range(0, self.numCartas - 1):
                outStr += f'{elementos[i]} , '
            outStr += f'{elementos[self.numCartas - 1]} ]'
        return outStr

    def removeNo(self, n: cNo):
        """Remove das cartas recebidas a primeira carta que faz par com a carta passada como parametro"""

        noAnterior = n
        noAtual = noAnterior.__prox__
        while noAtual:
            # Compara o primeiro caracter da string.
            if noAtual.__dado__[0] == n.__dado__[0]:
                noAnterior.__prox__ = noAtual.__prox__

                # Adiciona a carta a lista monte e deleta o No Atual.
                self.monte += [n.__dado__]
                self.monte += [noAtual.__dado__]
                del(noAtual)

                # Incrementa o monte e decrementa a quantidade de cartas.
                self.numMonte += 2
                self.numCartas -= 1
                return True
            noAnterior = noAtual
            noAtual = noAtual.__prox__
        return False

    def separaPar(self):
        """Separa os pares de cartas."""

        # Percorre a lista
        noAnterior = self.__inicio__
        noAtual = noAnterior.__prox__
        while noAtual is not None:
            if self.removeNo(noAtual):
                noAnterior.__prox__ = noAtual.__prox__

                # Deleta o No atual se for encontrado um par para a carta.
                del(noAtual)
                self.numCartas -= 1
                noAtual = noAnterior.__prox__
            else:
                noAnterior = noAtual
                noAtual = noAtual.__prox__

        if self.numCartas == 0:
            return True
        return False

    def insereNoFim(self, n):
        """Insere um novo No no fim da lista"""

        novoNo = cNo.cNo(n)
        if self.__inicio__ == None:
            self.__inicio__ = novoNo
            self.numCartas += 1
            return True
        noAtual = self.__inicio__
        while noAtual.__prox__ is not None:
            noAtual = noAtual.__prox__
        noAtual.__prox__ = novoNo
        self.numCartas += 1
        return True

    def removeCartaEscolhida(self, n):
        """Remove a carta no Indice escolhido."""

        noAnterior = self.__inicio__
        noAtual = noAnterior.__prox__
        for c in range(n):
            if noAtual.__prox__ is not None:
                noAnterior = noAtual
                noAtual = noAtual.__prox__

        noAnterior.__prox__ = noAtual.__prox__
        no = noAtual
        del(noAtual)
        self.numCartas -= 1
        return no.__dado__