''' Bucket sort adaptado para números reais e implementado na classe cVetor '''

class cVetor:

    def __init__(self, n):

        self.vet        = [0] * n
        self.maxObjs    = n
        self.numObjs    = 0

    def insere(self, chave):
        """Insere um elemento no final do vetor
        
        Parâmetros:
        chave -- lista de inteiros/floats ou um
                 valor do tipo inteiro/float
        """
        
        if self.numObjs < self.maxObjs:
            self.vet[self.numObjs] = chave
            self.numObjs += 1
            return self.vet

    def __str__(self):

        outStr = "[ "

        if self.numObjs == 0:
            outStr += "Vetor Vazio ]"
        else:
            for i in range(0, self.numObjs-1):
                outStr += f'{self.vet[i]} , '

            outStr += f'{self.vet[self.numObjs-1]} ]'

        return outStr
    
    def __getitem__(self, position):

        return self.vet[position]
    
    def __setitem__(self, chave,i):

        self.vet[i]=chave
        return self.vet[i]

    def max(self):
        '''Retorna o valor do maior elemento do vetor'''

        maior=self.vet[0]
        ind=0
        for i in range (1,self.numObjs):
          if self.vet[i]>maior:
            maior=self.vet[i]

        return maior

    def insertionSort(self, num_comp=0):
        '''Ordena o vetor pelo método insertion e retorna o número de comparações
        
        Parâmetros:
        num_comp -- número de comparações (default 0)
        '''

        n=self.numObjs # Tamanho do vetor
        vet=self.vet 

        # Percorre o vetor a partir do segundo elemento
        for i in range (1, n):

            chave=vet[i] # Valor atual

            j=i-1 # Inicializa o índice a ser comparado 

            # Desloca os elementos maiores que o valor atual para a direita
            while j>=0 and chave<vet[j]:
                vet[j+1]=vet[j]
                j=j-1
                num_comp+=1
            
            # Insere o elemento na posição correta
            vet[j+1]=chave

        # Retorna o número de comparações
        return num_comp
    
    def bucketSort(self,k=1):
        '''Ordena um vetor no intervalo [0,1) pelo método bucket sort e retorna 
        o número de comparações
        
        Parâmetros:
        k -- valor do divisor dos elementos do vetor no caso do método ter sido 
             chamado pelo método 'bucket_sort_reais()' (default 1)
        '''
        vet= self.vet 
        n= self.numObjs # Tamanho do vetor

        # Cria os buckets e distribui os elementos
        num_buckets=10
        buckets=cVetor(10)

        # Insere um vetor com 'n' posições em cada bucket
        for i in range (10):
            a=cVetor(n) 
            buckets.insere(a)

        # Insere os elementos do vetor em seu bucket correspondente
        for i in range(n):
            bucket_idx = int(vet[i] * num_buckets)
            buckets[bucket_idx].insere(vet[i])

        # Inicializa o número de comparações como 0
        num_comp=0

        # Ordena os elementos de cada bucket usando o Insertion Sort
        for i in range(num_buckets):

            # Ordena os elementos apenas dos buckets não vazios
            if buckets[i].numObjs>1: 
                num_comp=buckets[i].insertionSort(num_comp)
        

        # Junta os buckets ordenados em um único vetor 'sorted'
        sorted = cVetor(n)
        for i in range(num_buckets):

            # Insere os elementos apenas dos buckets não vazios
            if buckets[i].numObjs!= 0:
                sorted.__insere_sorted(buckets[i],k) # Insere cada elemento de 'bucket[i]' em 'sorted'
        
        self.vet = sorted.vet # Atualiza o vetor ordenado

        return num_comp # Retorna o número de comparações
    
    def __insere_sorted(self,chave,k=1):
        """Esse método de inserção organiza a saída do bucket sort, adicionando 
        os elementos de cada bucket individualmente no vetor sorted e multiplicando 
        pela constante 'k'
        
        Parâmetros:
        chave -- Objeto da classe cVetor
            k -- Divisor dos elementos de cVetor (default 1)
        """

        # Verifica se a chave é do tipo cVetor
        if isinstance(chave, cVetor):

            # Insere cada elemento do cVetor 'chave' individualmente em self.vet
            for i in range(chave.numObjs):
                self.vet[self.numObjs]=chave[i]*k # Multiplica novamente por k 
                self.numObjs += 1

        return self.vet # Retorna o vetor com as inserções

    def bucket_sort_reais (self):
        '''Implementa o algoritmo bucket sort para valores fora do intervalo [0,1),
        incluindo números negativos'''

        n=self.numObjs # Tamanho
        num_comp=0 # Armazenar o número de comparações

        neg=cVetor(n) # Armazenar a parte negativa do vetor
        pos=cVetor(n) # Armazenar a parte positiva do vetor
        sorted=cVetor(n) # Armazenar o vetor ordenado 

        # Separa a parte negativa e a positiva do vetor nos vetores 'pos' e 'neg'
        for i in range(n):
            if self.vet[i]<0:
                # Insere o módulo dos elementos negativos em 'neg'
                neg.insere(-(self.vet[i])) 
            else:
                pos.insere(self.vet[i]) # Insere os elementos positivos em 'pos'


        # Normaliza os elementos positivos do vetor no intervalo de [0,1)
        k=int(pos.max())+1 # Inicializa a constante 'k'
        for i in range (pos.numObjs):
            pos.vet[i]= (pos.vet[i]/k) # Divide cada elemento pela constante 'k'


        # Normaliza os elementos negativos do vetor no intervalo de [0,1)
        m=int(neg.max())+1 # Inicializa a constante 'm'
        for i in range (neg.numObjs):
            neg.vet[i]= (neg.vet[i]/m) # Divide cada elemento pela constante 'm'


        # Ordena os elementos do vetor 'neg' e atualiza a variável 'num_comp'
        num_comp+=neg.bucketSort(m) # Retorna o número de comparações 

        # Insere o vetor 'neg' ordenado em 'sorted' 
        for i in range (neg.numObjs-1,-1,-1): # Ordem decrescente
            
            # Insere transformando novamente em negativo
            sorted.insere(-(neg.vet[i]))  
            
        # Ordena os elementos do vetor 'pos' e atualiza a variável 'num_comp' 
        num_comp+=pos.bucketSort(k)

        # Insere o vetor 'pos' ordenado em 'sorted'
        for i in range (pos.numObjs):
            sorted.insere(pos.vet[i])

        self = sorted

        return sorted, num_comp # Retorna o vetor ordenado e o número de comparações
    
    def selection_sort(self):
        '''Ordena o vetor pelo método selection e retorna o número de comparações'''

        n = self.numObjs # Tamanho
        num_comp = 0 # Armazenar o número de comparações 

        # Percorre o vetor do primeiro até o penúltimo elemento
        for i in range(n):
            menor = i
            # Encontra o índice do menor elemento no restante do vetor
            for j in range(i+1, n):
                num_comp += 1 # Incrementa o número de comparações
                if self.vet[j] < self.vet[menor]:
                    menor = j
            if menor != i:
                # Troca o menor elemento encontrado com o elemento na posição 'i'
                self.vet[i], self.vet[menor] = self.vet[menor], self.vet[i]
        return num_comp
    
if __name__=='__main__':
    vet=cVetor(10)
    vet.insere(0.344418738)
    vet.insere(90000000000)
    vet.insere(0.35290812)
    vet.insere(0.32)
    vet.insere(0.977790932849)
    vet.insere(1.931425421)
    vet.insere(-4444444444420)
    print(vet)
    vet,n=vet.bucket_sort_reais()
    print("O vetor ordenado em ordem crescente é:",vet)
    print("e o número de comparações foi:", n)

