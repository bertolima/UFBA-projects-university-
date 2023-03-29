#Entrada
x = int(input())
import math
#logica(condicionais para os valores de entrada) e saida
if x == 1:
  print("Chapeuzinho Vermelho", x)
  print("Vovozinha", 0)
  print("Lobo Mau", 0)
else:
  if x == 2:
    print("Chapeuzinho Vermelho", x - 1)
    print("Vovozinha", x - 1)
    print("Lobo Mau", 0)
  else:
    if x >= 3:
     print("Chapeuzinho Vermelho", math.ceil(x / 3))
     print("Vovozinha", round(x / 3))
     print("Lobo Mau", int(x / 3))

     #Reprise do código
#Entrada
x = int(input())
import math
#lógica(condicionais) e saida - muito menor
print("Chapeuzinho Vermelho", math.ceil(x / 3))
print("Vovozinha", round(x / 3))
print("Lobo Mau", int(x / 3))