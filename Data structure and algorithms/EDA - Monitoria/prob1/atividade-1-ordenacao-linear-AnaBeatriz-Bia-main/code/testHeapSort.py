import random
from heapSort import Vetor

# Criar um objeto Vetor
v = Vetor(10)

# Inserir valores aleatórios no vetor
for i in range(10):
    v.insere(random.randint(1, 50))

# Imprimir o vetor antes da ordenação
print("Antes da ordenação:")
print(v)

# Ordenar o vetor usando HeapSort
v.heapSort()

# Imprimir o vetor depois da ordenação
print("\nDepois da ordenação:")
print(v)
print()
v.imprimeNumComparacoes()
