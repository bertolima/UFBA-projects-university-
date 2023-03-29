# Entrada
x = int(input())
y = map(int, input().split())
z = int(input())

#criando uma nova lista a partir da lista y
filtro = [n for n in y if n == z]

#condicionais para  saída
if filtro:
    print(filtro[0])
else:
    print(-1)
