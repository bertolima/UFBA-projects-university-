# Ruan Cardoso dos Santos 220121212 04/06/2023

import random
from baralho import Carta, Baralho
from jogador import Jogador

def jogarMico():
    baralho = Baralho() # Inicia o jogo com o baralho completamente ordenado
    ace = baralho.ACE() # ace recebe o conjunto de cartas do baralho, porém já embaralhadas pelo próprio método ACE()
    mico = baralho.sorteiaMico() # Remove o 'mico' do baralho apartir de um número index gerado aleatoriamente

    
    jogadores = [] # lista de jogares

    numJogadores = int(input('Digite o número de jogadores: '))
    if 0 < numJogadores < 4: # Caso o número de jogadores esteja no intervalo esperado irá executar o bloco de código
        for i in range(numJogadores):
            nomeJogador = input(f'Digite o nome no jogador {i+1}')
            jogadores.append(Jogador(nomeJogador, i+1)) # adiciona na lista 'jogadores' o jogador gerado pela classe Jogador(), cada jogador é construido com um nome, um número, e uma lista das cartas que possui, a princípio vazia.
    else:
        print('A quantidade de jogadores inserida é inválida !')

    while baralho.vazio() is False: # Irá realizar a distribuição das cartas enquanto o baralho não estiver vazio
        for jogador in jogadores: # Cada jogador contido na lista 'jogadores' irá receber uma carta do topo da pilha de cartas
            carta = baralho.distCartas()
            jogador.receberCarta(carta)
    
    for jogador in jogadores: # Exibe todas as cartas que cada jogador possui
        jogador.mostrarCartas()

    jogadorAtual = jogadores[0] # O jogadorAtual recebe o primeiro jogador da lista 'jogadores'.
    indiceAtual = 0
    print(f"\nJogador atual: {jogadorAtual.nome}")
    while True:
        jogadorAtual = jogadores[indiceAtual] # Seleciona o jogador atual com base no índice atual
        print(f'Jogador atual: {jogadorAtual.nome}')
        jogadorAlvo = input("Digite o nome do jogador que você deseja pegar a carta (ou 'fim' para encerrar o jogo): ")
        if jogadorAlvo == "fim":
            break

        jogadorAlvo = next((j for j in jogadores if j.nome == jogadorAlvo), None) # Busca o jogador alvo com base no nome digitado

        if jogadorAlvo:
            jogadorAtual.mostrarCartas() # Mostra as cartas do jogador atual
            posicaoCarta = int(input("Digite a posição da carta que você deseja pegar: ")) - 1
            cartaPegada = jogadorAlvo.removerCarta(posicaoCarta) # Remove a carta escolhida do jogador alvo
            if cartaPegada:
                jogadorAtual.receberCarta(cartaPegada) # Recebe a carta do jogador alvo
                print(f"\n{cartaPegada} foi pega do jogador {jogadorAlvo.nome}")

                if jogadorAtual.temMico(): # Verifica se o jogador atual possui o "mico"
                    print(f"\n{jogadorAtual.nome} foi revelado com o 'mico'!")
                    break # Interrompe o loop se o jogador atual tiver o "mico"

                print("\nCartas atualizadas do jogador atual:")
                jogadorAtual.mostrarCartas() # Mostra as cartas atualizadas do jogador atual
            else:
                print("\nPosição inválida. Nenhuma carta foi removida.")

            indiceAtual += 1 # Incrementa o índice atual para passar para o próximo jogador
            if indiceAtual >= len(jogadores):
                indiceAtual = 0 # Reinicia o índice para 0 quando chegar ao final da lista de jogadores

        print("\nCartas atualizadas dos jogadores:")
        for jogador in jogadores:
            jogador.mostrarCartas() # Mostra as cartas atualizadas de todos os jogadores
