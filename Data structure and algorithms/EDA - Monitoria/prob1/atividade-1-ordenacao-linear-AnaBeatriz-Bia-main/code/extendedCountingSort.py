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
    
    def extendedCountingSort(self):
        # Determina o valor máximo do vetor
        max_value = self.vet[0]
        min_value = self.vet[0]
        
        for x in self.vet:
            if x > max_value:
                max_value = x
            elif x < min_value:
                min_value = x

        # Normaliza os valores do vetor entre 0 e 1
        normalized_vet = [(x - min_value) / (max_value - min_value) for x in self.vet]
        
        # Cria lista de contagem de 0 a 1 com precisão de uma casa decimal
        count = [0] * 11 
        for x in normalized_vet: # x é um valor entre 0 e 1
            count[int(x*10)] += 1
        
        # Cria uma lista com a posição de início de cada valor normalizado
        n = 11 # n é um valor entre 0 e 1 com precisão de uma casa decimal
        pos = [0] * n 
        for i in range(1, n):
            pos[i] = pos[i-1] + count[i-1] 
        
        # Ordena o vetor
        sorted_vet = [0] * self.numObjs
        for x in normalized_vet: 
            # calcula o número de comparações
            self.numComparacoes += 1 
            # coloca o valor normalizado na posição correta
            sorted_vet[pos[int(x*10)]] = x 
            # incrementa a posição para o próximo valor normalizado
            pos[int(x*10)] += 1 
        
        # Desnormaliza os valores ordenados entre 0 e 1
        for i in range(self.numObjs):
            sorted_vet[i] = (sorted_vet[i] * (max_value - min_value)) + min_value
        
        # Substitui o vetor original pelo vetor ordenado
        self.vet = sorted_vet
        
    # Imprime o número de comparações realizadas durante a ordenação
    def imprimeNumComparacoes(self):
        print(f"O número de comparações realizadas durante a ordenação é: {self.numComparacoes}")
