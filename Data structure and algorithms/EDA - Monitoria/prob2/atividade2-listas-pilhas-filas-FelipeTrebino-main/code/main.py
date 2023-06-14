
from cBaralho import cBaralho
from cJogador import cJogador
from cFilaTurno import cFilaTurno
import sys
import time
import random
from datetime import datetime

if __name__ == '__main__':

    # Definições dos parâmetros da simulação através da entradas do sistema

    nJogadores = 4
    nomesGenericos = 's'
    intervalo = 2

    if (len(sys.argv) > 1):
        nJogadores = int(sys.argv[1])
        try:
            nomesGenericos = sys.argv[2]
            intervalo = int(sys.argv[3])
        except:
            pass
        
    if nJogadores < 0 or nJogadores > 4:
        nJogadores = 4
    
    filaJogadores = cFilaTurno()

    if nomesGenericos != 's' and nomesGenericos != 'n':
        nomesGenericos = 's'

    if intervalo < -1 or type(intervalo) != int:
        intervalo = 2

    if nomesGenericos != 'n':
        for i in range(nJogadores):
            nome = f"Jogador {i+1}"
            filaJogadores.queue(cJogador(nome))  
    else:
        for i in range(nJogadores):
            nome = input(f"Digite o nome do {i+1}º Jogador: ")
            filaJogadores.queue(cJogador(nome))  


    # Criação do deck de cartas
    deck = cBaralho()

    # Geração das cartas do baralho ordenadas 
    deck.generateDeck()

    # Embaralhamento do deck (ACE)
    deck.shuffle()

    # Retirada da carta par do mico
    par_mico = deck.pop()

    # Distribuição das cartas entre os jogadores
    while(not deck.empty()):
        carta = deck.pop()
        if carta != None:
            filaJogadores.dequeue().getMao().insereCarta(carta)

    # Randomização simples para decidir quem começa o jogo
    random.seed(int(datetime.now().strftime('%H%M%S')))
    # "Rodar a fila"
    for _ in range(random.randint(0,nJogadores)):
        filaJogadores.dequeue()

    # Mão inicial dos jogadores
    print("\n\n-------------------------- Mão inicial dos jogadores --------------------------\n\n")
    for i in range(len(filaJogadores)):
        print(f"     \n{filaJogadores.dequeue()}\n\n")

    # Inicialização do jogo
    turno = 1
    fim = False
    print('-------------------------- O Jogo iniciou --------------------------\n\n ')
    while(not fim):
        if turno == 1:
            # Remoção inicial dos pares
            print(f"------------------- Resultado da remoção inicial dos pares dos jogadores -------------------\n\n")
            for _ in range(len(filaJogadores)):
                jogador = filaJogadores.dequeue()
                jogador.getMao().removePares()
                if len(jogador.getMao()) == 0:
                    print('\n_______________________________________________________________________________________________\n')
                    print(f"     O jogador {jogador.getName()} naõ possui mais cartas na mão!\n")
                    print('\n_______________________________________________________________________________________________\n')
                else:
                    print(f"    Jogador: {jogador.getName()}: {jogador.getMao()}\n\n")
            print('\n_______________________________________________________________________________________________\n')
        

        # Jogador do turno
        jogador =  filaJogadores.dequeue()

        #Verificação da mão do jogador
        if(len(jogador.getMao()) > 0):

            # Timer para turnos
            time.sleep(intervalo)

            # Mão inicial
            print(f"Turno {turno}:\n\n     Jogador (Mão inicial): {jogador}\n")
            
            # Proximo Jogador
            prox_jogador = jogador.getProx()

            #Verificação do proximo jogador
            while len(prox_jogador.getMao()) == 0:
                prox_jogador = prox_jogador.getProx()
                if prox_jogador == jogador:
                    prox_jogador = None
                    fim = True
                    break

            if prox_jogador is not None:

                # Retirar uma carta escolhida do próximo jogador da fila
                n = random.randint(0,len(prox_jogador.getMao()) - 1)
                carta_retirada = prox_jogador.getMao().removeCartaEscolhida(n)

                # Verifica se o proximo jogador ainda possui cartas na mão
                if len(prox_jogador.getMao()) == 0:
                    print('\n_______________________________________________________________________________________________\n')
                    print(f"     O jogador {prox_jogador.getName()} não possui mais cartas na mão!")
                    print('\n_______________________________________________________________________________________________\n')

                # Insere a carta do próximo jogador na mão
                jogador.getMao().insereCarta(carta_retirada)
                print(f"     A {n + 1}ª carta foi retirada de {prox_jogador.getName()}: {carta_retirada}\n")

                # Verifica a formação de pares e armazena as cartas caso tenha formado um novo par
                par = jogador.getMao().removePares()

                if par:
                    print(f"     Um par foi formado: {jogador.getMao().getUltimoPar()}\n")
                
                # Verifica se o jogador atual ainda possui cartas na mão
                if len(jogador.getMao()) == 0:
                    print('\n_______________________________________________________________________________________________\n')
                    print(f"     O jogador {jogador.getName()} não possui mais cartas na mão!\n")
                    print('\n_______________________________________________________________________________________________\n')

                # Imprime os resultados finais do turno
                else:
                    print(f"     Jogador (Mão Final): {jogador}\n")
                    print('\n_______________________________________________________________________________________________\n')
                if len(jogador.getMao().getUltimoPar()) > 0:
                    print(f"     Ultimo par retirado pelo jogador {jogador.getName()}: {jogador.getMao().getUltimoPar()}")
                    print('\n_______________________________________________________________________________________________\n')
                turno += 1

            #Final da simulação, sobrou um jogador com uma carta na mão
            else:
                print('\n_______________________________________________________________________________________________\n')
                print(f"##### O jogador {jogador.getName()} perdeu no turno {turno}! Mão final (Mico): {jogador.getMao()} #####\n")
                print(f"#### Par do mico: {par_mico} ####")
                print('\n_______________________________________________________________________________________________\n')
        
        
        