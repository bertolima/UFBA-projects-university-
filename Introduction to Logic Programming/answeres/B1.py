#entrada
t1, d1 = input().split()
t2, d2 = input().split()
t1 = int(t1)
d1 = int(d1)
t2 = int(t2)
d2 = int(d2)

#logica
valorkm = t1 * t2
valorkm = int(valorkm)
qtdpedagio = t1 / d1
qtdpedagio = int(qtdpedagio)
valorpedagio = qtdpedagio * d2
valorpedadio = int(valorpedagio)
valortotal = valorpedagio + valorkm
valortotal = int(valortotal)

#saida
print(valortotal)
