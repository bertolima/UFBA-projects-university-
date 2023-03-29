# Entrada
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
forca= x + y + z #Definindo o valor da força

#lógica(condicionais para valores de saida)
if forca > 110:
  print("Hum, parece que houve um erro")
else:
  if forca >= 110 * 0.8:
    print("Seu pokemon e uma maravilha")
  else:
    if forca >= 110 * 0.67:
     print("Seu pokemon certamente me chamou atencao")
    else:
      if forca >= 110 * 0.51:
        print("Seu pokemon esta acima da media")
      else:
        if forca >= 0:
          print("Seu pokemon nao fara progresso em batalhas")