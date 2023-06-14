class Dados:
    def __init__(self, n, mini, maxi):#recebe o tamanho e maior e menor valores
        self.valores = []
        self.n = n
        self.mini = mini
        self.maxi = maxi

    def gerador(self): #gera os valores a serem ordenados
        for i in range(self.n):
            value = random.uniform(self.mini, self.maxi)
            self.valores.append(value)

    def imprimir(self):# método de impressão do conjunto 
        for value in self.valores:
            print(value, end=" ")
        print()
        
class RadixSort: #classe para realizar a operação com o algoritmo Radix
    def __init__(self, conjunto):
        self.conjunto = conjunto

    def ordenar(self):
        # Encontra o valor máximo do conjunto para definir o número de passagens total
        max_value = max(self.conjunto.valores)
        # Realiza uma contagem para cada dígito em cada passagem
        exp = 1
        while max_value // exp > 0:
            count = [0] * 10
            for value in self.conjunto.valores:
                index = (value // exp) % 10
                count[index] += 1
            # Atualiza as contagens indicando a posição final de cada dígito
            for i in range(1, 10):
                count[i] += count[i-1]
            #  novo conjunto é criado, agora ordenado usando as contagens atualizadas
            sorted_array = [0] * self.conjunto.n
            for i in range(self.conjunto.n-1, -1, -1):
                value = self.conjunto.valores[i]
                index = (value // exp) % 10
                count[index] -= 1
                sorted_array[count[index]] = value
            # Atualização do conjunto original com o novo conjunto ordenado
            self.conjunto.valores = sorted_array
            # Incrementa a posição do dígito para a próxima passagem
            exp *= 10
#código submeter as entradas
import random

n = int(input())
mini = float(input(" valor mínimo: "))
maxi = float(input(" valor máximo: "))

conjunto = Dados(n, mini, maxi)
conjunto.gerador()


conjunto.imprimir()

radix_sort = RadixSort(conjunto)
radix_sort.ordenar()
print(" ")
conjunto.imprimir()