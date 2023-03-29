# Entrada
sapos, pedras = map(int, input().split())

#criando elementos nunma lista a partir da quantiade de pedras
pedras_list = [0] * pedras

#listas vazias para adicionar valores no loop
pulos = []
final = []


for i in range(sapos):
  pulo = int(input())
  #adiciona o valor "pulo" para dentro da lista pulos
  pulos.append(pulo)

  for n in range(0, pedras, pulo):
     #adiciona 1 aos elementos que o range 0, pedras, pulo passa "por cima"
     pedras_list[n] += 1

#adiciona os valores 0 ou 1 a lista final em cada posição    
for n in range(0, pedras):
    if pedras_list[n] != 0:
        final.append(1)
    else:
        final.append(0)

#valor de saida
print(*final, sep=" ")