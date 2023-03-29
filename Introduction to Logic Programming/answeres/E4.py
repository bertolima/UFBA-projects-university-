# Entrada
esferas = int(input())
n_estrelas = list(map(int, input().split()))

# definindo uma lista verdadeira para todas as esferas
esferas_true = [1, 2, 3, 4, 5, 6, 7]

# adicionando as esferas verdadeiras encontradas na lista esfera_estrela
esfera_estrela = [n_estrelas[i] for i in range(0, esferas) if n_estrelas[i] == 1 or n_estrelas[i] == 2 or n_estrelas[i]
                  == 3 or n_estrelas[i] == 4 or n_estrelas[i] == 5 or n_estrelas[i] == 6 or n_estrelas[i] == 7]

# bubble_sort para organizar a lista de forma crescente
n = len(esfera_estrela)
for j in range(n-1):
    for i in range(n-1):
        if esfera_estrela[i] > esfera_estrela[i + 1]:
            esfera_estrela[i], esfera_estrela[i +
                                              1] = esfera_estrela[i + 1], esfera_estrela[i]

# valores de saida com condicionais
if esfera_estrela == esferas_true:
    print(*esfera_estrela, sep=" ")
    print("Saia Shenlong e realize o meu desejo")
else:
    print(*esfera_estrela, sep=" ")
    print("Nao encontramos todas")
