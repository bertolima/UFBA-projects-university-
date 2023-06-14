import random
import time
from utils import *

import cListaC
import cJogador
import cCarta
import cBaralho


class cListaJogadores(cListaC.cListaC):
    def __init__(self):
        super().__init__()
        self.__cursor__ = None

    # Método para posicionar o cursor. Devido ao raciocínio utilizado, é iniciado no final.
    def posicionarCursorInicialmente(self):
        if self.__inicio__ is None:
            return
        self.__cursor__ = self.__fim__

    # Movimentar o cursor para o próximo jogador
    def proximoJogador(self):
        self.__cursor__ = self.__cursor__.__prox__

        return self.__cursor__

    # Método para o jogador realizar a jogada
    def realizarJogada(self, jogador):
        # Imprime a mão do jogador
        print(f"Mão do jogador: {BLUE}{jogador.getDado().getMao()}{RESET}")
        time.sleep(1)
        proxJogador = jogador.getProx()
        posicao = random.randint(0, proxJogador.getDado().tamanhoMao() - 1)

        cartaEscolhida = proxJogador.getDado().removerCarta(posicao)
        print(f"{YELLOW}{jogador.getDado().getNome()} {BOLD}pegou a carta {MAGENTA}{cartaEscolhida} "
              f"{BOLD}de {GREEN}{proxJogador.getDado().getNome()}{RESET}")
        jogador.getDado().receberCarta(cartaEscolhida)

        par = jogador.getDado().abaixarPares()
        for i in range(par.getTamanho()):
            jogador.getDado().inserirParesAbaixados(par.buscaDadoPos(i))
        print(f"Mão do jogador pós rodada: {BLUE}{jogador.getDado().getMao()}{RESET}")
        print(f'Último par abaixado: {RED}{jogador.getDado().getParesaBaixados().mostrarTopo()}{RESET}')


if __name__ == '__main__':
    listaJogadores = cListaJogadores()

    listaJogadores.insereNo(cJogador.cJogador('jogador 1'))
    listaJogadores.insereNo(cJogador.cJogador('jogador 2'))
    # listaJogadores.insereNo(cJogador.cJogador('jogador 3'))
    # listaJogadores.insereNo(cJogador.cJogador('jogador 4'))
    # listaJogadores.insereNo(cJogador.cJogador('jogador 5'))

    print(listaJogadores)

    listaJogadores.posicionarCursorInicialmente()

    print(listaJogadores.__cursor__)

    joga = listaJogadores.proximoJogador()

    # print(type(joga))
    # print(joga)

    baralho = cBaralho.cBaralho(52)
    baralho.montarBaralho()

    while not baralho.empty():
        carta = baralho.pop()
        obj = listaJogadores.proximoJogador()
        obj.__dado__.receberCarta(carta)

    print(listaJogadores)

    jogador = listaJogadores.proximoJogador()
    print(jogador)

    jogador2 = listaJogadores.proximoJogador()
    print(jogador2)
    jogador2 = listaJogadores.proximoJogador()
    print(jogador2)

    jogador2 = listaJogadores.proximoJogador()
    print(jogador2)

    jogador2 = listaJogadores.proximoJogador()
    print(jogador2)

    jogador2 = listaJogadores.proximoJogador()
    print(jogador2)



    # jogador = listaJogadores.proximoJogador()
    #
    # print(jogador.getDado().getMao())
    #
    # buscado = listaJogadores.buscaDadoPos(0)
    #
    # print(buscado)
    # print(type(buscado.getDado()))
    #
    # excluido = listaJogadores.removeNo(buscado.getDado())
    # print(excluido)
    #
    # print(listaJogadores)

    # n = listaJogadores.proximoJogador()
    # print(n)
    # print(n.__dado__)
    # print(n.getDado().getMao())

    # listaJogadores.pegarCartaProxJgdr(n)
    #
    # print(n.getDado().getMao())

    # print(n.__dado__.mao)
