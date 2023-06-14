import cListaCartas
import cPilha
import cCarta


# Classe jogador
class cJogador:

    # *******************************************************
    # *******************************************************
    def __init__(self, nome=None):
        self.mao = cListaCartas.cListaCartas()
        self.paresAbaixados = cPilha.cPilha(52)
        self.nome = nome

    def __str__(self):
        outStr = f"Jogador: {self.getNome()}"
        return outStr

    # Método para retorna a quantidade de cartas na mão do jogador
    def tamanhoMao(self):
        return self.mao.getTamanho()

    # Método para retornar a mão do jogador
    def getMao(self):
        return self.mao

    # Método para retornar o monte de cartas abaixadas
    def getParesaBaixados(self):
        return self.paresAbaixados

    # Método para mostrar a mão do jogador, de forma formatada
    def imprimirMao(self):
        if self.mao.getTamanho() == 0:
            return "Mão Vazia"
        outStr = ""
        for i in range(self.mao.getTamanho()):
            outStr += f"\n{self.mao.buscaDadoPos(i).getDado().getCarta()}, {self.mao.buscaDadoPos(i).getDado().getNaipe()}"
        return outStr

    # Retorna o nome do jogador
    def getNome(self):
        return self.nome

    # Método para setar o nome do jogador
    def setNome(self, nome):
        self.nome = nome

    # Método para o jogador receber a carta
    def receberCarta(self, carta):
        return self.mao.insereCartasOrd(carta)

    # Método para remover carta da mão do jogador
    def removerCarta(self, pos=3):
        carta = self.mao.removePos(pos)
        return carta.getDado()

    # Método para abaixar os pares formados na mão do jogador
    def abaixarPares(self):
        return self.mao.buscaDadosIguais()

    # Métodos para inserir os pares retirados no monte de pares abaixados
    def inserirParesAbaixados(self, n):
        self.paresAbaixados.push(n)


if __name__ == '__main__':
    jogador = cJogador()

    jogador.receberCarta(cCarta.carta(12, 'diamond'))
    jogador.receberCarta(cCarta.carta(7, 'heart'))
    jogador.receberCarta(cCarta.carta(12, 'diamond'))
    jogador.receberCarta(cCarta.carta(7, 'diamond'))
    jogador.receberCarta(cCarta.carta(5, 'spade'))
    jogador.receberCarta(cCarta.carta(5, 'club'))

    print(jogador.imprimirMao())

    carta = jogador.removerCarta()
    print(carta)
    print(jogador.imprimirMao())
