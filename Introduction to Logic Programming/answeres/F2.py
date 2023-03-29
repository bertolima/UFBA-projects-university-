# Entrada
x1, x2 = input().split()
y1, y2 = input().split()

#condionais junto à logica para os valores de saida
if not x1 == y1:
  print("Bloqueado")
else:
  if x1 == y1 and not x2 == y2:
    print("Driblado")
    print("...e o goleiro pega")
  else:
    if x1 == y1 and x2 == y2:
      print("Driblado")
      print("Gol")