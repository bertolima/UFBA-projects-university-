# Entrada
x = int(input())

#definindo variaveis
y = 0
z = 0

#loop para definir o valor de n que vai resultar numa condiciona de saída
for i in range(x):
  n = int(input())
  if n == 1:
    y = y + 1
  if n == 2:
    z = z + 1
print(y)
print(z)