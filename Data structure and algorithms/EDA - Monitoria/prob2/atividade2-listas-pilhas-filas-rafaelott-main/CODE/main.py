from cBaralho import gerarBaralho, embaralhar
from Jogador import cJogador

def exibir_mao(jogador):
    print(f"Mão de {jogador.nome}:")
    jogador.mao.Lista()
    print()

def main():
    # Criação do baralho e embaralhamento
    baralho = gerarBaralho()
    mico = embaralhar(baralho)

    # Criação dos jogadores
    jogadores = []
    num_jogadores = int(input("Digite o número de jogadores (2 a 4): "))
    for i in range(1, num_jogadores + 1):
        nome_jogador = input(f"Digite o nome do jogador {i}: ")
        jogadores.append(cJogador(nome_jogador))

    # Distribuição das cartas
    num_cartas_por_jogador = baralho.size() // num_jogadores
    for _ in range(num_cartas_por_jogador):
        for jogador in jogadores:
            carta = baralho.pop()
            jogador.recebeCarta(carta)

    # Jogo
    jogador_atual = jogadores[0]
    while not baralho.empty():
        exibir_mao(jogador_atual)

        if jogador_atual == jogadores[0]:
           
            carta_retirada = jogador_atual.retirarCarta(posicao_carta, jogador_atual)
            print(f"{jogador_atual.nome} retirou a carta: {carta_retirada}")
        else:
            carta_retirada = jogador_atual.retirarCarta(1, jogador_atual)
            print(f"{jogador_atual.nome} retirou uma carta.")

        for jogador in jogadores:
            if jogador != jogador_atual:
                jogador.recebeCarta(carta_retirada)

        jogador_atual.organizaMao()

        jogador_atual = jogadores[(jogadores.index(jogador_atual) + 1) % num_jogadores]

    print("Fim do jogo!")

if __name__ == "__main__":
    main()
