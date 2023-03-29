#Entrada
x1, x2 = input().split()
y1, y2 = input().split()
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

#logica e saida
if x1 > 1000 or x2 > 1000 or y1 > 1000 or y2 > 1000 or x1 < 1 or x2 < 1 or y1 < 1 or y2 < 1:
  print("Nao soltar pacote")
else:
  if x1 == y1 and x2 == y2:
    print("Soltar pacote")
  else:
    print("Nao soltar pacote")