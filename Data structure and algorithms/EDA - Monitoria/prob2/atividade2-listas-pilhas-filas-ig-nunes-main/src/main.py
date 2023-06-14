import cCarta
import cBaralho
import cJogador
import cListaJogadores

import cVetor as vetor

import time
import random
from utils import *
from datetime import datetime


if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    print(f"{BLUE}******************************************************{RESET}")
    print(f"{BLUE}----------Bem-vindo ao simulador Mico v1.0------------{RESET}")

    print()
    print(F"Carregando informações...")
    time.sleep(1)

    # Criando o baralho com cartas ordernadas (pilha)
    print(F"Gerando o baralho e embaralhando as cartas...")
    time.sleep(1)
    baralho = cBaralho.cBaralho(52)

    # Agrupamentos de Cartas Embaralhadas (ACE) e mico:
    mico = baralho.embaralhar()

    print(f"{BOLD}O mico é a carta {RED}{mico.getCarta()} de {mico.getNaipe()}{RESET}")

    # Selecionar quantos jogadores vão jogar (de 2 a 4):
    while True:
        numeroJogadores = int(input(f"Escolha quantos jogadores irão participar {BOLD}(2 ou 3 ou 4){RESET}: \n"))
        if numeroJogadores == 2 or numeroJogadores == 3 or numeroJogadores == 4:
            break
        print(f"{RED}Valor digitado {numeroJogadores} inválido. Por favor, entre com o valor 2 ou 3 ou 4!{RESET}")

    vetorJogadores = vetor.cVetor(numeroJogadores)

    # Entrar com a identificação do jogador
    for i in range(numeroJogadores):
        aux = cJogador.cJogador()
        aux.setNome(input(f"{BOLD}Digite o nome do {i + 1}° jogador:{RESET}\n").upper())
        vetorJogadores.insert(aux)

    # Ordenação de jogadores:
    listaJogadores = cListaJogadores.cListaJogadores()

    while True:
        manterOrdem = input(f"Deseja reorganizar a ordem de jogadores? {BOLD}(sim ou nao){RESET}\n")

        if manterOrdem.lower() == "sim":
            print(f"{BOLD}Reorganizando a ordem de jogadores...{RESET}")
            for i in range(numeroJogadores):
                # Escolher aleatoriamente os jogadores e colocando na fila
                jogador = vetorJogadores.removePos(random.randint(0, numeroJogadores - 1 - i))
                listaJogadores.insereNo(jogador)
            break
        elif manterOrdem.lower() == "nao":
            print(f"{BOLD}Mantendo a ordem de jogadores...{RESET}")
            for i in range(numeroJogadores):
                # Adicionando os jogadores na ordem de entrada
                jogador = vetorJogadores.removePos(0)
                listaJogadores.insereNo(jogador)
            break
        else:
            print(F"{RED}Entrada inválida! Entre com 'sim' ou 'nao' para escolher.{RESET}")

    # Distribuir cartas para os jogadores:
    # Posicionando o cursor:
    listaJogadores.posicionarCursorInicialmente()
    print(f"Distribuindo cartas paras os jogadores...")
    print()
    time.sleep(1)
    while not baralho.empty():
        carta = baralho.pop()
        jogador = listaJogadores.proximoJogador()
        jogador.getDado().receberCarta(carta)

    # Inicio da simulação
    print(f"{BLUE}Iniciando simulação:{RESET}")
    print()
    time.sleep(1)

    # Rodada para retirar os pares iniciais de cada jogador:
    print(f"{BOLD}******************************************************{RESET}")
    print(f"{BOLD}Abaixando pares de cada jogador antes do início....{RESET}")
    for i in range(listaJogadores.getTamanho()):
        print(f"Jogador: {YELLOW}{jogador.getDado().getNome()}{RESET},", end=" ")
        # Adicionando cartas no monte de pares do jogador:
        cartas = jogador.getDado().abaixarPares()
        for j in range(cartas.getTamanho()):
            jogador.getDado().inserirParesAbaixados(cartas.removePos(0))

        jogador = listaJogadores.proximoJogador()
    print(f"{BOLD}******************************************************{RESET}")
    print()

    # Posicionando o cursor para o início das rodadas:
    listaJogadores.posicionarCursorInicialmente()
    jogador = listaJogadores.proximoJogador()
    rodada = 1
    while listaJogadores.getTamanho() > 1:
        print(f"{RED}RODADA {rodada}:{RESET} {YELLOW}{jogador.getDado().getNome()}{RESET}{BOLD}, é a sua vez!{RESET}")
        if jogador.getDado().tamanhoMao() == 0:
            print(f"{RED}Sem cartas na mão! Jogador saindo...{RESET}")
            jogadorSaindo = listaJogadores.removeNo(jogador.getDado())
            vetorJogadores.insert(jogadorSaindo)
            jogador = listaJogadores.proximoJogador()
            print(f"{GREEN}Próximo jogador: {jogador.getDado().getNome()}{RESET}")
            rodada += 1
            print()
            print()
            continue

        print(
            f"Número de cartas que {YELLOW}{jogador.getDado().getNome()}{RESET} possui: {BOLD}{jogador.getDado().tamanhoMao()}{RESET}")
        time.sleep(1)

        listaJogadores.realizarJogada(jogador)
        time.sleep(1)
        if jogador.getDado().tamanhoMao() == 0:
            print(f"{RED}{jogador.getDado().getNome()} abaixou todas as cartas!{RESET}")
            jogadorSaindo = listaJogadores.removeNo(jogador.getDado())
            vetorJogadores.insert(jogadorSaindo)
        jogador = listaJogadores.proximoJogador()
        print(f"{GREEN}Próximo jogador: {jogador.getDado().getNome()}{RESET}")
        rodada += 1
        print()
        print()

    print(f"{RED}Perdedor:{RESET} {BOLD}{jogador.getDado().getNome()}!{RESET}")
    vencedores = ''
    for i in range(vetorJogadores.size()):
        vencedores += f"{vetorJogadores.getitem(i).getDado().getNome()}, "
    print(f"{YELLOW}Vencedor(es):{RESET} {BOLD}{vencedores[:-2]}!{RESET}")

    print()
    print(f"{GREEN}Finalizando jogo...{RESET}")
    time.sleep(1)
