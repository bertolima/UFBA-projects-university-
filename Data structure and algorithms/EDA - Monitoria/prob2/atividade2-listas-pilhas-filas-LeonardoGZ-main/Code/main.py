import TADs
from MICO import Carta, Jogador, JogoMico

# Função para criar jogadores com nomes personalizados
def criar_jogadores(n):
    jogadores = []
    for i in range(n):
        nome = input(f"Informe o nome do jogador {i+1}: ")
        jogador = Jogador(nome)
        TADs.add(jogadores, jogador)
    return jogadores

def main():
    print("Bem-vindo ao jogo de Mico!")

    # Solicita o número de jogadores ao usuário e valida o valor
    num_jogadores = int(input("Informe o número de jogadores (2-4): "))
    while num_jogadores < 2 or num_jogadores > 4:
        print("Número inválido de jogadores. Tente novamente.")
        num_jogadores = int(input("Informe o número de jogadores (2-4): "))

    # Cria os jogadores com nomes personalizados
    jogadores = criar_jogadores(num_jogadores)

    # Inicia o jogo de Mico com os jogadores criados
    jogo = JogoMico(jogadores)
    jogo.iniciar_jogo()

if __name__ == "__main__":
    main()
