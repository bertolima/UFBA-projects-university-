import random
from extendedCountingSort import Vetor

n = int(input("Digite quantos valores devem ser gerados:"))
a = int(input("Digite o valor mínimo:"))
b = int(input("Digite o valor máximo:"))
print()

vetor = Vetor(n)

for i in range(n):
    vetor.insere(random.uniform(a, b))

# Imprimindo o vetor desordenado
print("Vetor original:")
print(vetor)

# Ordenando o vetor com o algoritmo Extended Counting Sort
vetor.extendedCountingSort()

# Imprimindo o vetor ordenado
print("Vetor ordenado:")
print(vetor)
print()
vetor.imprimeNumComparacoes()
