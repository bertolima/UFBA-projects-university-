########################################################################


import sys
import random
import math
from datetime import datetime
import array


# *******************************************************
# ***                                                 ***
# *******************************************************
class cVetor:

    # *******************************************************
    def __init__(self, n):

        self.vet = [0] * n
        self.maxElem = n
        self.numElem = 0
        self.quickSortComp = 0
        self.mergeSortComp = 0

    # *******************************************************
    def __str__(self):

        outStr = "[ "

        if self.numElem == 0:
            outStr += "Vetor Vazio ]"
        else:
            for i in range(0, self.numElem - 1):
                outStr += f'{self.vet[i]} , '

            outStr += f'{self.vet[self.numElem - 1]} ]'

        return outStr

    # *******************************************************
    def size(self):
        return self.numElem

    # *******************************************************
    def getitem(self, key):
        if key > self.numElem:
            return -1
        return self.vet[key]

    # *******************************************************

    def setitem(self, key, value):
        if key > self.numElem - 1:
            print('Chave inválida')
        else:
            self.vet[key] = value

    # *******************************************************
    def getmin(self):
        mini = self.vet[0]
        for i in range(self.numElem):
            if mini > self.vet[i]:
                mini = self.vet[i]
        return mini

    # *******************************************************
    def getmax(self):
        maxi = self.vet[0]
        for i in range(self.numElem):
            if maxi < self.vet[i]:
                maxi = self.vet[i]
        return maxi

    # *******************************************************
    def insert(self, value):
        if self.numElem == self.maxElem:
            return "Vetor sem espaço disponível"
        self.vet[self.numElem] = value
        self.numElem += 1

    # *******************************************************
    def reverse(self):
        aux = cVetor(self.numElem)
        for i in range(self.numElem - 1, -1, -1):
            aux.insert(value=self.vet[i])
        for j in range(self.numElem):
            self.vet[j] = aux.getitem(j)

    # *******************************************************
    def search(self, value):
        result = False
        position = 0
        for i in range(self.numElem):
            if self.vet[i] == value:
                result = True
                break
            position += 1
        return f"Foi encontrado na posição {position}." if result else "Não foi encontrado."

    # *******************************************************
    def occurrence(self, value):
        occurrence = 0
        for i in range(self.numElem):
            if self.vet[i] == value:
                occurrence += 1
        return occurrence

    # *******************************************************
    def remove(self, value):
        if self.numElem == 0:
            return "Não foi possível remover, vetor não possui elementos"
        position = 0
        result = True
        for i in range(self.numElem):
            if self.vet[i] == value:
                result = False
                break
            position += 1
        if result:
            return "Não foi possível encontrar o valor no vetor"
        else:
            aux = cVetor(self.numElem - 1)
            condition = True
            for i in range(self.numElem):
                if self.vet[i] == value:
                    if condition:
                        condition = False
                        continue
                aux.insert(self.vet[i])
            self.numElem = 0
            for i in range(aux.numElem):
                self.insert(aux.vet[i])
            return "Operação realizada com sucesso"

    # *******************************************************
    def removePos(self, pos):
        elemento = None
        if self.numElem == 0:
            return "Não foi possível remover, vetor não possui elementos"
        if pos < 0 or pos > self.numElem:
            return "Posição inválida"

        aux = cVetor(self.numElem - 1)
        for i in range(self.numElem):
            if i == pos:
                elemento = self.vet[i]
                continue
            aux.insert(self.vet[i])
        self.numElem = 0
        for i in range(aux.numElem):
            self.insert(aux.vet[i])
        return elemento


    # *******************************************************
    def statistics(self):
        media = 0
        a = 0
        for i in range(self.size()):
            media += self.vet[i]
        media /= self.size()
        for element in self.vet:
            a += (element - media) ** 2
        variance = a / (self.size() - 1)
        standardDeviation = variance ** (1 / 2)

        return f'Média do vetor: {media}; Variância: {variance}; Desvio Padrão: {standardDeviation}'

    # *******************************************************
    def busca_seq(self, chave):
        comp = 0
        for i in range(self.numElem):
            comp += 1
            if self.vet[i] == chave:
                return i, comp
        return -1, comp

    # *******************************************************
    def busca_seq_ord(self, chave):
        comp = 0
        for i in range(self.numElem):
            comp += 1
            if self.vet[i] > chave:
                return -1, comp
            comp += 1
            if self.vet[i] == chave:
                return i, comp
        return -1, comp

    # *******************************************************

    def busca_bin_iter(self, chave):
        comp = 0
        inicio = 0
        fim = self.numElem - 1
        meio = (inicio + fim) // 2
        if chave < self.vet[inicio] or chave > self.vet[fim]:
            return -1, 0
        while inicio <= fim:
            comp += 1
            if self.vet[meio] == chave:
                return meio, comp
            comp += 1
            if self.vet[meio] < chave:
                inicio = meio + 1
                meio = (inicio + fim) // 2
                continue
            comp += 1
            if self.vet[meio] > chave:
                fim = meio - 1
                meio = (inicio + fim) // 2
        return -1, comp

    # *******************************************************

    def busca_bin_rec_ini(self, chave):
        comp = 0
        inicio = 0
        fim = self.numElem - 1
        if chave < self.vet[inicio] or chave > self.vet[fim]:
            return -1, 0
        return self.busca_bin_rec(inicio, fim, chave, comp)

    def busca_bin_rec(self, inicio, fim, chave, comp):
        meio = (inicio + fim) // 2
        if inicio > fim:
            return -1, comp
        comp += 1
        if self.vet[meio] == chave:
            return meio, comp
        comp += 1
        if self.vet[meio] < chave:
            inicio = meio + 1
            meio = (inicio + fim) // 2
            return self.busca_bin_rec(inicio, fim, chave, comp)
        comp += 1
        if self.vet[meio] > chave:
            fim = meio - 1
            meio = (inicio + fim) // 2
            return self.busca_bin_rec(inicio, fim, chave, comp)
        return -1, comp

    # *******************************************************

    def ordenacao_selecao(self):
        comp = 0
        for i in range(self.numElem - 1):
            menorPosicaoAtual = i
            for j in range(i + 1, self.numElem):
                comp += 1
                if self.vet[menorPosicaoAtual] > self.vet[j]:
                    menorPosicaoAtual = j
            if menorPosicaoAtual != i:
                self.vet[i], self.vet[menorPosicaoAtual] = self.vet[menorPosicaoAtual], self.vet[i]
        return self.__str__(), comp

    # *******************************************************

    def ordencao_insercao(self):
        comp = 0
        for i in range(1, self.numElem):
            j = i
            while j > 0:
                comp += 1
                if self.vet[j - 1] > self.vet[j]:
                    self.vet[j - 1], self.vet[j] = self.vet[j], self.vet[j - 1]
                else:
                    break
                j -= 1
        return self.__str__(), comp

    # *******************************************************

    def ordenacao_bolha(self):
        comp = 0
        for final in range(self.numElem, 0, -1):
            condicao = False
            for atual in range(final - 1):
                comp += 1
                if self.vet[atual] > self.vet[atual + 1]:
                    self.vet[atual], self.vet[atual + 1] = self.vet[atual + 1], self.vet[atual]
                    condicao = True
            if not condicao:
                break
        return self.__str__(), comp

    # *******************************************************

    def quick_sort(self):
        self.quickSortComp = 0
        return self.quick_sort_aux( 0, self.numElem - 1)

    def quick_sort_aux(self, inicio, fim):
        if inicio >= fim:
            return
        else:
            pivo = self.partition(inicio, fim)
            self.quick_sort_aux(inicio, pivo - 1,)
            self.quick_sort_aux(pivo + 1, fim)
        return self.__str__(), self.quickSortComp

    def partition(self, inicio, fim):
        i = inicio
        for u in range(inicio, fim):
            self.quickSortComp += 1
            if self.vet[u] <= self.vet[fim]:
                self.vet[i], self.vet[u] = self.vet[u], self.vet[i]
                i += 1
        self.vet[i], self.vet[fim] = self.vet[fim], self.vet[i]

        return i

    # *******************************************************

    def merge_sort(self):
        aux = self.vet[:]
        self.merge_sort_aux(aux, 0, self.numElem - 1)

    def merge_sort_aux(self, aux, i, f):
        if i == f:
            return
        m = (i + f) // 2
        self.merge_sort_aux(aux, i, m)
        self.merge_sort_aux(aux, m + 1, f)
        self.merge(aux, i, m, f)

    def merge(self, aux, i, m, f):
        esq = i
        esq_fim = m
        direi = m + 1
        direi_fim = f
        posicao = i
        while esq <= esq_fim or direi <= direi_fim:
            if esq > esq_fim:
                aux[posicao] = self.vet[direi]
                direi += 1
                posicao += 1
            elif direi > direi_fim:
                aux[posicao] = self.vet[esq]
                esq += 1
                posicao += 1
            elif self.vet[esq] < self.vet[direi]:
                aux[posicao] = self.vet[esq]
                esq += 1
                posicao += 1
            else:
                aux[posicao] = self.vet[direi]
                direi += 1
                posicao += 1

        for j in range(i, f + 1):
            self.vet[j] = aux[j]

    # *******************************************************
    # Bucket Sort
    # Fazendo usando apenas a classe cVetor:
    def bucket_sort(self, n=10):
        comp = 0
        return self.bucket_sort_aux(n=n, comp=comp)

    def bucket_sort_aux(self, n=10, comp=0):
        # Cria um balde cVetor com 10 espaços dentro, também cVetores
        bucket = cVetor(10)

        for i in range(10):
            bucket.insert(cVetor(n))

        # Inserir elementos nos baldes:
        for j in range(self.numElem):
            # index_b = int(((10 ** rec) * self.vet[j]) % 10 // 1)
            index_b = int(10 * self.vet[j])
            bucket.vet[index_b].insert(self.vet[j])

        # Ordena os elementos de cada balde:
        for i in range(bucket.numElem):
            # Ordenando usando o metodo de insercao:
            x = bucket.vet[i].ordencao_insercao()
            comp += x[1]

            # Ordenado usando o método selecao()
            # x = bucket.vet[i].ordenacao_selecao()
            # comp += x[1]

            # Ordenado usando o método bubble sort()
            # x = bucket.vet[i].ordenacao_bolha()
            # comp += x[1]

            # Ordenado usando o método quick sort()
            # x = bucket.vet[i].quick_sort()
            # comp += x[1]

            # Ordenado usando o método merge sort()
            # x = bucket.vet[i].merge_sort()
            # comp += x[1]

        # Ordena o vetor original:
        k = 0
        for i in range(bucket.numElem):
            for j in range(bucket.vet[i].numElem):
                self.vet[k] = bucket.vet[i].vet[j]
                k += 1
        return comp


# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    n = 40

    v = cVetor(n)
    s = cVetor(n)
    r = cVetor(n)
    t = cVetor(n)

    print(str(v))

    # for i in range(n // 2, 0, -1):
    #     v.insere(i)
    # print(str(v))

    for i in range(n // 2):
        if i <= 40:
            v.insert(random.randint(0, 100))
        if i <= 50:
            s.insert(round(random.uniform(0, 1.0), 3))
        if i <= 200:
            r.insert(round(random.uniform(0, 1.0), 3))
        if i <= 1000:
            t.insert(round(random.uniform(0, 1.0), 3))
        # print(str(v))

        # print(str(v))

    print(v)

    print(v.removePos(10))

    print(v)

    # print(f'vetor original: {v}')
    # a = v.ordenacao_bolha()
    # print(f'vetor ordenado: {v}')
    # print(f'número de comparações no total: {a[1]}')
    #
    # print()
    #
    # print(f'Estatísticas: {v.statistics()}')
