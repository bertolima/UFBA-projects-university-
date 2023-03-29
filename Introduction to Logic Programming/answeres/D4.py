# Entrada
jogadores = int(input())
assassinato_jogadores = list(map(int, input().split()))

#organiza a lista em ordem crescente
assassinato_jogadores.sort()

#valor de saida
print(*assassinato_jogadores, sep=" ")
      