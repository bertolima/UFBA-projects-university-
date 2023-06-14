

if __name__ == '__main__':
    import random
    import cCartas
    import cBaralho

    print('\033[1;33m', f'\nSimulação de partida de 4 jogadores:\n'
          f'Uma carta é considerada igual a outra quando elas começam com a mesma letra ou número.\n'
          f'Sentido: J1 pega de J2, J2 pega de J3, J3 pega de J4 e J4 pega de J1. e começa o ciclo novamente.\n'
          f'Fim do Jogo: O jogo termina quando apenas um jogador possui carta e está carta é o Mico.\n', '\033[m')

    baralho = cBaralho.cBaralho(4)
    print('Baralho: ', baralho.vPilha)
    print(f'Número de cartas no baralho: {baralho.topo + 1}')
    print('Mico: ', baralho.mico, '\n')

    baralho.distribuiCartas()

    for jogador in baralho.jogadores:
        print(f'Cartas iniciais do {jogador.nome}: {jogador.cartas} {jogador.cartas.numCartas}')

    for jogador in baralho.jogadores:
        jogador.cartas.separaPar()

    print('\n')
    baralho.mostraCartas()
    print('\n', '*' * 150)
    baralho.iniciaRodada()
