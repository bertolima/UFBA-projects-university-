from sorting import *
import time

class Placas:

    def __init__(self, arquivo):

        self.numComp = 0
        self.vet = []
        self.arquivo = arquivo
        

        self.preencherLista()

        self.inicio = time.time()
        self.ordenar()
        self.final = time.time() - self.inicio

        self.gerarLista()
        

    def preencherLista(self):
        with open(self.arquivo, 'r') as documento:
            for placa in documento:
                self.vet.append(placa)
        return self.vet



    def ordenar(self):
        inicio = time.time()
        radixSort(self.vet)
        fim = time.time()
        total = fim-inicio
        
        
    
    def gerarLista(self):
        with open ('resultado.piv', 'w') as documento:
            for placa in self.vet:
                documento.write(placa)
            documento.close()


        
    def ordenarSort(self):
        inicio = time.time()
        self.vet.sort()
        return print(time.time()-inicio)



    def quicksort(self, inicio=0, fim=None):
        if fim is None:  # necessario pra saber o tamanho da lista
            fim = len(self.vet)-1
        if inicio < fim:  # necessario pra que evite situações esquisitas com sublistas de só um elemento e/ou elementos repetidos
            # atribui posição do pivot retornada à varivel p
            p = self.partition(inicio, fim)
            # quicksort a esquerda do pivot (recurssao)
            self.quicksort(inicio, p-1)
            # quicksort a direita do pivot (recurssao)
            self.quicksort(p+1, fim)

    def partition(self, inicio, fim):
        # definimos o pivot como a ultima variavel da lista
        pivot = self.vet[fim]
        i = inicio
        for j in range(inicio, fim):
            self.numComp += 1
            if self.vet[j] <= pivot:  # comparamos cada elemento da lista com o pivot
                # caso seja menor que o pivot, fazemos a troca de posições de modo que os elementos menores que o pivot fiquem mais a esquerda possivel
                self.vet[j], self.vet[i] = self.vet[i], self.vet[j]
                i += 1
        # colocamos o pivot a direita do ultimo elemento menor que ele, de modo que o pivot esteja ordenado.
        self.vet[i], self.vet[fim] = self.vet[fim], self.vet[i]
        return i  # retorna posição do pivot