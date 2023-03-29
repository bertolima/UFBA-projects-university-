# Entrada
s2 = "0"
while True:
#entrada de valores dentro do loop
  n, s1 = input().split()
  s1 = int(s1)
#condicionais para a saída com base nos valores de entrada
  if s1 >= 90:
    s2 = "Alta"
  else:
    s2 = "Internar"
    if s1 == 0:
     break
    
  print(n, s2)
  