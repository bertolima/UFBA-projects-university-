#Módulo para testes;

from pessoas import Jogador
from jogo import Jogo
from objetos import Carta

#Para o teste, aqui será colocado o nome dos 3 jogadores que escolhi para simular;
nome_jogador1 = input("Digite o nome do jogador 1: ")
nome_jogador2 = input("Digite o nome do jogador 2: ")
nome_jogador3 = input("Digite o nome do jogador 3: ")

# Tendo os nomes, basta atribuir ao jogador1, jogador 2 e jogador3;
jogador1 = Jogador(nome_jogador1)
jogador2 = Jogador(nome_jogador2)
jogador3 = Jogador(nome_jogador3)

# Agora, adicionando os jogadores ao jogo;
jogo = Jogo([jogador1, jogador2, jogador3])


jogador1.adicionar_carta(Carta("A", "♠"))
jogador1.adicionar_carta(Carta("A", "♥"))

jogador2.adicionar_carta(Carta("A", "♦"))
jogador2.adicionar_carta(Carta("A", "♣"))

jogador3.adicionar_carta(Carta("2", "♦"))
jogador3.adicionar_carta(Carta("2", "♣"))

# Para iniciar a partida;
jogo.iniciar_partida()

# Para executar as rodadas do jogo;
num_cartas_total = len(jogo.baralho.cartas)  # Número total de cartas
for _ in range(num_cartas_total):
    jogo.jogar_rodada()

# Para verificar o vencedor após todas as rodadas;
vencedor = None
pontuacao_maxima = 0

for jogador in jogo.jogadores:
    pontuacao = len(jogador.monte)
    if pontuacao > pontuacao_maxima:
        pontuacao_maxima = pontuacao
        vencedor = jogador.nome

if vencedor:
    print(f"O/A jogador(a) {vencedor} venceu o jogo! :)")
else:
    print("O jogo terminou em empate. :(")
