# Entrada
x = int(input())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
D = list(map(int, input().split()))

#criando nova lista a partir da soma dos valores de cada elementos das listas u e v
U = [u[i] + v[i] for i in range (x)]

#condicionais para saida de valores
if U == D:
  print("OK")
else:
  print("NOPE :(")