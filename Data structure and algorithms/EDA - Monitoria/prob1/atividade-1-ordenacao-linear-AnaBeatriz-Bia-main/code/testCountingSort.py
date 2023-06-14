import random
from countingSort import Vetor

# Criar um objeto da classe Vetor
v = Vetor(10)

# Inserir valores aleatórios no vetor
for i in range(10):
    v.insere(random.randint(1, 100))

# Imprimir o vetor antes da ordenação
print("Antes da ordenação:")
print(v)

# Ordenar o vetor 
v.countingSort()

# Imprimir o vetor depois da ordenação
print("\nDepois da ordenação:")
print(v)
