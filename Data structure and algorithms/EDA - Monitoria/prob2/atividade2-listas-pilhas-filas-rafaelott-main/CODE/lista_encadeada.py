class cNo:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    def setProx(self, prox):
        self.prox = prox

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def estaVazia(self):
        return self.inicio is None

    def adicionar(self, dado):
        novoNo = cNo(dado)

        if self.estaVazia():
            self.inicio = novoNo
        else:
            atual = self.inicio
            while atual.prox:
                atual = atual.prox
            atual.prox = novoNo
        self.tamanho += 1

    def remover(self, dado):
        atual = self.inicio
        anterior = None

        while atual:
            if atual.dado == dado:
                if anterior:
                    anterior.prox = atual.prox
                else:
                    self.inicio = atual.prox
                self.tamanho -= 1
                return
            anterior = atual
            atual = atual.prox

    def buscar(self, dado):
        atual = self.inicio
        ocorrencia = 0

        while atual:
            if atual.dado.naipe == dado.naipe and atual.dado.posicao == dado.posicao:
                ocorrencia += 1
            atual = atual.prox
        
        return ocorrencia

    def buscarCarta(self, posicaoCarta):
        atual = self.inicio

        for i in range(1, posicaoCarta):
            atual = atual.prox
        
        return atual.dado

    def removerCarta(self, dado):
        atual = self.inicio
        anterior = None

        while atual:
            if atual.dado.naipe == dado.naipe and atual.dado.posicao == dado.posicao:
                if anterior:
                    anterior.prox = atual.prox
                else:
                    self.inicio = atual.prox
                self.tamanho -= 1
                return
            anterior = atual
            atual = atual.prox

    def Lista(self):
        atual = self.inicio
        while atual:
            print(atual.dado)
            atual = atual.prox
