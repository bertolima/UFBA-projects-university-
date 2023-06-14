class Pilha:
    def __init__(self):
        self.cartas = []

    def empilhar(self, carta):
        self.cartas.append(carta)

    def desempilhar(self):
        if not self.vazia():
            return self.cartas.pop()

    def vazia(self):
        return len(self.cartas) == 0

    def exibir_topo(self):
        if not self.vazia():
            return self.cartas[-1]

    def tamanho(self):
        return len(self.cartas)