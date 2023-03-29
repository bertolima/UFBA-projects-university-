# Entrada
t = int(input())
maior = -1 #Definição de variavel

#Loop pra fazer a lógica
while True:
  p = int(input())
  maior = max(maior, p)
  if p == 0:
    break

#condicionais para os valores de saida
if maior > t:
  print("ALARME")
else:
  print("O Havai pode dormir tranquilo")