# Atividade 2 - Simulando um Jogo de Baralho
# Aluno: Felipe S. Trebino
# Classe de cVector

import random
from datetime import datetime

class cVetor:


# *******************************************************
    def __init__(self, n):

        self.__vet        = [0] * n
        self.__maxObjs    = n
        self.__numObjs    = 0

# *******************************************************
    def insert(self, chave):
        
        if self.__numObjs < self.__maxObjs:
            self.__vet[self.__numObjs] = chave
            self.__numObjs += 1
            return True

        return False

# *******************************************************
    def __str__(self):

        outStr = "[ "

        if self.__numObjs == 0:
            outStr += "Vetor Vazio ]"
        else:
            for i in range(0, self.__numObjs-1):
                outStr += f'{self.__vet[i]} , '

            outStr += f'{self.__vet[self.__numObjs-1]} ]'

        return outStr
    
# *******************************************************
    def __len__(self):
        return self.__numObjs

# *******************************************************
    def __getitem__(self, p):
        return self.__vet[p]
    
# *******************************************************    
    def __setitem__(self, p, value):
        if p > self.__numObjs:
            self.__numObjs = p + 1
        self.__vet[p] = value

# *******************************************************   
    def clone(self):
        v = cVetor(len(self))
        for i in range(len(self)):
            v.insert(self[i])
        return v
    
# ******************************************************* 
    # Método para embaralhar as posições do vetor
    def shuffle(self):
        random.seed(int(datetime.now().strftime('%H%M%S')))
        for i in range(len(self) - 1, 0, -1):
            j = random.randint(0, i)
            self[i], self[j] = self[j], self[i] 

