import random
import array

# *******************************************************
# ***                                                 ***
# *******************************************************
class cVetor:

# *******************************************************
    def __init__(self, n):
        self.vet = [0] * n
        self.cont = 0
        self.maxSize = n

    def print(self):
        for i in range(self.cont-1):
            print(self.vet[i],", ", sep="", end='')

        print(self.vet[self.cont-1],".", sep="")

    def getTamanho(self):
        return self.cont
    
    def getElemento(self, i):
        if(self.vet[i] != 0):
            return self.vet[i]
        return False
    
    def setElemento(self, elemento, i):
        if (i < self.maxSize):
            self.vet[i] = elemento
        else:
            print("O vetor não contem o índice informado")

    def minimum(self):
        min = self.vet[0]
        for i in range(1, self.cont):
            if (self.vet[i] < min):
                min = self.vet[i]

        return min
    
    def maximum(self):
        max = self.vet[0]
        for i in range(1, self.cont):
            if (self.vet[i] > max):
                max = self.vet[i]

        return max
    
    def inserir(self, elemento):
        self.vet[self.cont] = elemento
        self.cont += 1

    def inverter(self):
        new_vet = [0] * self.maxSize
        j = self.cont-1
        i = 0

        while (j >= 0):
            new_vet[i] = self.vet[j]
            i += 1
            j -= 1

        self.vet = new_vet

    def search(self, elemento):
        for i in range(self.cont):
            if (self.vet[i] == elemento):
                return True, i
        return False
    
    def getOcorrencias(self, elemento):
        cont = 0
        for i in range(self.cont):
            if(v[i] == elemento):
                cont += 1
        return cont
    
    def remover(self, elemento):
        for i in range(self.cont):
            if (self.vet[i] == elemento):
                for j in range(i, self.cont-1):
                    self.vet[j] = self.vet[j+1]
                self.cont -= 1
                return True
        return False

    def GerarEstatisticas(self):
        total = 0
        
        for i in range (self.cont):
            total = total + self.vet[i]
        media = total/self.cont

        desvioParcial = 0
        for i in range (self.cont):
            desvioParcial = desvioParcial + (pow(2,(self.vet[i] - media)))
        
        desvioParcial = desvioParcial/self.cont
        desvioPadrao = pow(desvioParcial, 1/2)

        return media, round(desvioPadrao,2)
    
    def E_Identico(self, other):
        for i in range(self.cont):
            if(other[i] != self.vet[i]):
                return False
        return True
            

v = cVetor(10)

v.inserir(5)
v.inserir(15)
v.inserir(30)
v.inserir(2)
v.inserir(7)

v.print()
v.inverter()
v.print()



        
            
    
