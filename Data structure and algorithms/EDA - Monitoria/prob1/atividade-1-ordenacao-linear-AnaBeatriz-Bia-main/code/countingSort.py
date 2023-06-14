class Vetor:
    def __init__(self, n):
        self.vet = [0] * n
        self.maxObjs = n
        self.numObjs = 0

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
    
    def countingSort(self):
        maximo = self.vet[0]
        for i in range(1, self.numObjs):
            if self.vet[i] > maximo:
                maximo = self.vet[i]
        maximo += 1 
        count = [0] * maximo
        saida = [0] * self.numObjs
        
        for i in range(self.numObjs):
            count[self.vet[i]] += 1
        
        for i in range(1, maximo):
            count[i] += count[i - 1]
            
        for i in range(self.numObjs):
            saida[count[self.vet[i]] - 1] = self.vet[i]
            count[self.vet[i]] -= 1
        
        for i in range(self.numObjs):
            self.vet[i] = saida[i]
