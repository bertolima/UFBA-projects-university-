class Vetor:

    def __init__(self, n):
        self.vet = [0] * n
        self.maxObjs = n
        self.numObjs = 0
        self.numComparacoes = 0

    def insere(self, chave):
        if self.numObjs < self.maxObjs:
            self.vet[self.numObjs] = chave
            self.numObjs += 1
            return True
        return False

    def __str__(self):
        outStr = "[ "
        if self.numObjs == 0:
            outStr += "Vetor Vazio"
        else:
            for i in range(0, self.numObjs-1):
                outStr += f'{self.vet[i]} , '
            outStr += f'{self.vet[self.numObjs-1]} ]'
        return outStr

    # Transforma o vetor em uma heap
    def heapify(self, n, i):
        largest = i # Define o maior elemento como sendo o pai
        l = 2 * i + 1 # Calcula o índice do filho esquerdo
        r = 2 * i + 2 # Calcula o índice do filho direito

        if l < n and self.vet[l] > self.vet[largest]: # Se o filho esquerdo for maior que o pai, atualiza o maior elemento
            largest = l
            self.numComparacoes += 1
            
        if r < n and self.vet[r] > self.vet[largest]: # Se o filho direito for maior que o pai ou o filho esquerdo, atualiza o maior elemento
            largest = r
            self.numComparacoes += 1

        if largest != i: # Se o maior elemento não for o pai, troca os elementos de lugar e chama a função recursivamente para o filho afetado
            self.vet[i], self.vet[largest] = self.vet[largest], self.vet[i]
            self.heapify(n, largest)
        return self.numComparacoes

    # Ordena o vetor utilizando o algoritmo Heap Sort
    def heapSort(self):
        n = self.numObjs
        for i in range(n // 2 - 1, -1, -1): # Transforma o vetor em uma heap
            self.heapify(n, i)
        for i in range(n - 1, 0, -1): # Extrai os maiores elementos da heap e os coloca no final do vetor
            self.vet[i], self.vet[0] = self.vet[0], self.vet[i]
            self.heapify(i, 0)

    # Imprime o número de comparações realizadas durante a ordenação
    def imprimeNumComparacoes(self):
        print(f"O número de comparações realizadas durante a ordenação é: {self.numComparacoes}")
