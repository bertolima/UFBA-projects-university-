# Lab 02 - Analise de Algoritmos de Busca
# Criando uma Classe Vetor

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

        self.vet        = [0] * n
        self.maxObjs    = n
        self.numObjs    = 0
        self.nRec = 0

# *******************************************************
    def insere(self, chave):
        
        if self.numObjs < self.maxObjs:
            self.vet[self.numObjs] = chave
            self.numObjs += 1
            return True

        return False

# *******************************************************
    def __str__(self):

        outStr = "[ "

        if self.numObjs == 0:
            outStr += "Vetor Vazio ]"
        else:
            for i in range(0, self.numObjs-1):
                outStr += f'{self.vet[i]} , '

            outStr += f'{self.vet[self.numObjs-1]} ]'

        return outStr

# *******************************************************
    def buscaSeq(self, chave):
        nComp = 0
        for i in range(self.numObjs):
            nComp +=1
            if (self.vet[i] == chave):
                return i, nComp
        return -1, nComp

        
        
# *******************************************************
    def buscaSeqOrd(self, chave):
        nComp = 0
        k = int(pow(self.numObjs,0.5))
        j = self.numObjs-1
        i = 0
        while(i != j):
            nComp += 1
            if (self.vet[i] > chave or self.vet[j] < chave):
                return -1, nComp
            
            while(self.vet[i] != chave or self.vet[j] != chave):
                nComp += 2
                if (self.vet[i] == chave):
                    return i, nComp
                elif (self.vet[j] == chave):
                    nComp += 1
                    return j, nComp
                nComp += 1
                
                j = j - k
                i = i + k
                nComp += 2
                if(self.vet[j] < chave):
                    while(self.vet[j] != chave):
                        nComp += 1
                        j += 1
                    return j, nComp
                elif (self.vet[i] > chave):
                    i = i - k
                    while(self.vet[i] != chave):
                        nComp += 1
                        i += 1
                    return i, nComp





        

# *******************************************************
    def buscaBinIter(self, chave):
        start = 0
        end = self.numObjs
        nComp = 0
        while (start <= end):
            mid = (start+end)//2
            if (self.vet[mid] == chave):
                nComp +=1
                return mid, nComp
            elif (self.vet[mid] < chave):
                nComp +=1
                start = mid+1
            else:
                end = mid-1
            nComp +=2

        return -1, nComp


# # *******************************************************
    def buscaBinRec(self, chave, start=None, end=None):
        if start is None:
            start = 0
        if end is None:
            end = self.numObjs
        self.nRec+= 1
        if(start <= end):
            mid = (start+end)//2
            if(self.vet[mid] == chave):
                return mid, self.nRec
            elif (self.vet[mid] < chave):
                return self.buscaBinRec(chave, mid+1, end)
            else:
                return self.buscaBinRec(chave, start, mid-1)
        return -1, self.nRec
        
        

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    n = 20
    
    v = cVetor(n)

    print(str(v))
        
    for i in range(1, n // 2):
        v.insere(i)
        print(str(v))

    print(str(v))