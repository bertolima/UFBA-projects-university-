# ##################################################
#                Jogo Mico                         #
# ##################################################
from cCarta import cCarta
from cACE import cACE
from cMao import cMao
from cBaralho import cBaralho
from time import sleep
import random

# ##################################################
num_jogadores = 2

# ##################################################
lista_jogadores = []
lista_deposito_jogadores = []

# ##################################################
if __name__ == '__main__':
    print(f'Olá! Seja bem vindo ao "Jogo Mico" V1.0')
    # sleep(1)

    print(f'-> Adquirindo o baralho do jogo...')
    # sleep(1)
    print(f'Prepare as expectativas!...')
    # sleep(1)
    baralho = cBaralho()
    print(str(baralho))
    # sleep(1)

    print(f'-> Removendo Coringas...')
    baralho.remover_coringas()
    # sleep(1)

    print('-> Embaralhando cartas...')
    monte = baralho.embaralhar()  # cACE classe
    while monte is False:
        monte = cACE(baralho.getNumCartas())
        monte = baralho.embaralhar()  # cACE classe
    # sleep(1)

    print("-> Removendo cartas do Mico...\n")
    monte_mico = cACE(8)
    pos = random.randrange(1, 14)
    for i in range(1, 4):
        if baralho.remove(pos, i) is not False:
            carta = cCarta(pos, i)
            monte_mico.push(carta)
    print("   Monte Mico do jogo:")
    print(monte_mico)
    mico = cCarta(pos, 0)
    # sleep(1)

    print(f'-> Criando jogadores...')
    Jogador_1 = cMao()
    Jogador_2 = cMao()
    Jogador_3 = cMao()
    Jogador_4 = cMao()

    if num_jogadores == 2:
        lista_jogadores.append(Jogador_1)
        lista_jogadores.append(Jogador_2)

    if num_jogadores == 4:
        lista_jogadores.append(Jogador_1)
        lista_jogadores.append(Jogador_2)
        lista_jogadores.append(Jogador_3)
        lista_jogadores.append(Jogador_4)
    # sleep(1)

    print(f'-> Distribuindo cartas...\n')
    """Gerando monte do embaralhado do tipo cACE"""
    monte = cACE(baralho.getNumCartas())
    carta_cor = baralho.getInicio()
    monte.push(carta_cor)
    while carta_cor.getProx() is not None:
        monte.push(carta_cor.getProx())
        carta_cor = carta_cor.getProx()
    while not monte.empty():
        for i in range(len(lista_jogadores)):
            if not monte.empty():
                aux = monte.pop()
                lista_jogadores[i].insere_carta(aux.getPosicao(), aux.getNaipe())

    """Gerando Monte de pares de cartas removidos de cada jogador"""
    monte_jogador_1 = cACE(Jogador_1.getNumCartas() + 1)
    monte_jogador_2 = cACE(Jogador_2.getNumCartas() + 1)
    monte_jogador_3 = cACE(Jogador_3.getNumCartas() + 1)
    monte_jogador_4 = cACE(Jogador_4.getNumCartas() + 1)

    if num_jogadores == 2:
        lista_deposito_jogadores.append(monte_jogador_1)
        lista_deposito_jogadores.append(monte_jogador_2)

    if num_jogadores == 4:
        lista_deposito_jogadores.append(monte_jogador_1)
        lista_deposito_jogadores.append(monte_jogador_2)
        lista_deposito_jogadores.append(monte_jogador_3)
        lista_deposito_jogadores.append(monte_jogador_4)
    # sleep(1)


    # *******************************************************#
    #                  TELA DO JOGO                          #
    # *******************************************************#
    # sleep(1)
    b = "\033[;1m"
    red = "\033[1;31m"
    res = "\033[0;0m"
    g = "\033[0;32m"
    rev = "\033[;7m"


    def imprimeTela():
        print(f'Mico:\n{mico}')
        for i in range(len(lista_jogadores)):
            print(f'Jogador {i + 1}:')
            # print(str(lista_jogadores[i]))
            print(f'{lista_jogadores[i].imprime_beta()} \n {lista_deposito_jogadores[i].imprime_ultimo_par()}\n')


    def imprimeTela2():
        print(f'\n  Mico:\n{mico}')
        for i in range(len(lista_jogadores)):
            print(f'{b}  Jogador {i + 1}:{res}')
            print(str(lista_jogadores[i]))
            print(f'{lista_deposito_jogadores[i].imprime_ultimo_par()}')
            # print(f'{lista_jogadores[i].imprime_beta()} \n {lista_deposito_jogadores[i].imprime_ultimo_par()}\n')




    # *******************************************************#
    #                  INICIO DO JOGO                        #
    # *******************************************************#

    print(f'{b}-> Jogo iniciado!{res}')
    imprimeTela2()

    print("-> Cada jogador revove as cartas duplicadas e as colocas no monte de lixo. \n"
          "   Obs.: Só formarão pares as cartas dos Naipes '(♥)'+'(♦)'  e '(♠)'+'(♣)'.")
    # sleep(1)
    aux = cACE()
    for i in range(num_jogadores):
        aux = lista_jogadores[i].remove_par()
        while not aux.empty():
            lista_deposito_jogadores[i].push(aux.pop())
    # sleep(1)
    imprimeTela2()

    # sleep(1)

    if num_jogadores == 2:
        while not lista_jogadores[0].empty() or not lista_jogadores[1].empty():
            print("\n-> Nova rodada: Cada Jogador escolhe aleatoriamente uma carta da Mão do outro jogador:\n")
            # sleep(1)

            print("  Jogador 1 joga rodada:")
            # sleep(1)

            Jogador_2.setApontador(random.randrange(Jogador_2.getNumCartas()))
            imprimeTela2()
            carta_escolhida = Jogador_2.buscar_carta_indice(Jogador_2.getApontador())
            print(f'  Carta escolhida: {b}{red}{carta_escolhida.imprime_beta()}{res}')
            Jogador_1.insere_carta_inicio(carta_escolhida.getPosicao(), carta_escolhida.getNaipe())
            Jogador_2.remove_carta(carta_escolhida.getPosicao(), carta_escolhida.getNaipe())
            Jogador_2.clearApontador()
            Jogador_1.setApontador(0)
            achou_par = Jogador_1.setApontador(Jogador_1.busca_par_indice(carta_escolhida.getPosicao(), carta_escolhida.getNaipe()), 1)
            imprimeTela2()
            # sleep(1)
            if achou_par:
                print(f'{b}{red}  Parabés! Jogador 1 formou par!{res}\n')
            else:
                print(f'{b}  Jogador 1 não formou par!...Segue o jogo!{res}')
            # sleep(1.5)
            aux = Jogador_1.remove_par()
            Jogador_1.clearApontador()
            Jogador_1.clearApontador(1)
            while not aux.empty():
                monte_jogador_1.push(aux.pop())
            if Jogador_2.empty():
                imprimeTela2()
                print(f'{g}{rev}  \O/ -> JOGADOR 2 É O CAMPEAO!!! <- \O/  {res}')
                break
            if Jogador_1.empty():
                imprimeTela2()
                print(f'{g}{rev}  \O/ -> JOGADOR 1 É O CAMPEAO!!! <- \O/  {res}')
                break
            imprimeTela2()
            # sleep(1)

            print("\n-> Nova rodada: Cada Jogador escolhe aleatoriamente uma carta da Mão do outro jogador:\n")
            # sleep(1)

            print("  Jogador 2 joga rodada:")
            # sleep(1)
            Jogador_1.setApontador(random.randrange(Jogador_1.getNumCartas()))
            imprimeTela2()
            carta_escolhida = Jogador_1.buscar_carta_indice(Jogador_1.getApontador())
            print(f'  Carta escolhida: {b}{red}{carta_escolhida.imprime_beta()}{res}')
            Jogador_2.insere_carta_inicio(carta_escolhida.getPosicao(), carta_escolhida.getNaipe())
            Jogador_1.remove_carta(carta_escolhida.getPosicao(), carta_escolhida.getNaipe())
            Jogador_1.clearApontador()
            Jogador_2.setApontador(0)
            achou_par = Jogador_2.setApontador(Jogador_2.busca_par_indice(carta_escolhida.getPosicao(), carta_escolhida.getNaipe()), 1)
            imprimeTela2()
            # sleep(1)
            if achou_par:
                print(f'{b}{red}  Parabés! Jogador 2 formou par!{res}\n')
            else:
                print(f'{b}  Jogador 2 não formou par!...Segue o jogo!{res}')
            # sleep(1.5)
            aux = Jogador_2.remove_par()
            Jogador_2.clearApontador()
            Jogador_2.clearApontador(1)
            while not aux.empty():
                monte_jogador_2.push(aux.pop())
            if Jogador_1.empty():
                imprimeTela2()
                print(f'{g}{rev}  \O/ -> JOGADOR 1 É O CAMPEAO!!! <- \O/  {res}')
                break
            if Jogador_2.empty():
                imprimeTela2()
                print(f'{g}{rev}  \O/ -> JOGADOR 2 É O CAMPEAO!!! <- \O/  {res}')
                break
            imprimeTela2()
            # sleep(1)
            # break
