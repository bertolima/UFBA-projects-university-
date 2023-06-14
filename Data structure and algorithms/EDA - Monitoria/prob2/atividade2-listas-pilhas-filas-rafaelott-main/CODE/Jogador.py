import lista_encadeada
import pilha


class cJogador:
    def __init__(self, nome):
        self.nome = nome
        self.pilha = pilha.cPilha(100)
        self.mao = lista_encadeada.ListaEncadeada()

    def retirarCarta(self, posicao, jogador):
        posicao = max(1, posicao)
        carta = jogador.dado.mao.buscarCarta(posicao)
        jogador.dado.mao.remover(carta)
        self.mao.adicionar(carta)
        return carta

    
    def recebeCarta(self, carta):
        self.mao.adicionar(carta)

    def organizaMao(self):
        ocorrencias = {}
        novoNo = self.mao.inicio

        # Contar o número de ocorrências de cada carta na mão
        while novoNo:
            carta = novoNo.dado
            if carta in ocorrencias:
                ocorrencias[carta] += 1
            else:
                ocorrencias[carta] = 1
            novoNo = novoNo.prox

        # Remover cartas duplicadas e adicionar à pilha
        novoNo = self.mao.inicio
        while novoNo:
            carta = novoNo.dado
            if ocorrencias[carta] == 2:
                self.mao.removerCarta(carta)
                self.pilha.push(carta)
                self.mao.removerCarta(carta)
                self.pilha.push(carta)
            novoNo = novoNo.prox

        return


    