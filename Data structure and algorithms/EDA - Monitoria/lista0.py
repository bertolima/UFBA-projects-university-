import sys
import random

try:
    size = int(sys.argv[1])
    start = int(sys.argv[2])
    end = int(sys.argv[3])
except:
    size = 10
    start = 0
    end = 100


rang = end-size
limit = random.randint(start, rang)
vet = [0] * size
for i in range(size):
    vet[i] = limit
    limit += 1

for j in range(len(vet)-1):
    print(str(j) + ", ", end='')

print(vet[len(vet)-1])