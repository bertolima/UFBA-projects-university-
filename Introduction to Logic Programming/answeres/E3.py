# Entrada
x, y = input().split()
x = int(x)
y = int(y)
z = 0 #definindo contador z

#loop com range entre os valores de entrada x e y, aliado à lógica
for i in range(x, y+1):
  d = 2
  c = 0

#Verificação do número primo
  while d < i:
    if i % d == 0:
      c = 1
      d += 1
    else:
      d += 1

#Print do resultado
  if c == 0 and not i == 1:
    z += 1
print(int(z))