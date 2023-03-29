#Entrada
a, b, c = (input().split())
a = int(a)
b = int(b)
c = int(c)
#logica e saida
pessoas = a * b
if pessoas > c:
  print("S")
else:
  print("N")