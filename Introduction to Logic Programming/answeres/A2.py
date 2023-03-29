#Entrada
pl, pp = input().split()
pl1, pp1 = input().split()
pl2, pp2 = input().split()
pl = int(pl)
pl1 = int(pl1)
pl2 = int(pl2)
pp = int(pp)
pp1= int(pp1)
pp2 = int(pp2)

#logica
totall = pl + pl1 +pl2
totalp = pp + pp1 + pp2

#logica e saida
if totall == totalp:
  print( "Empate")
else:
  if totall > totalp:
    print("Lucas")
  else:
    print("Pedro")