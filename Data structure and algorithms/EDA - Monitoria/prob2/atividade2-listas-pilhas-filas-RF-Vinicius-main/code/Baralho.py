from ListaEncadeada import LEncadeada
import random

class Baralho:
    
    
    def __init__(self, listNaipes=['(P) [Paus]', '(V) [Ouros]', '(V) [Copas]', '(P) [Espadas]'], listValores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']):
        
        self.__baralho = LEncadeada()
        self.__listNaipes = listNaipes
        self.__listValores = listValores
        
    @property
    def baralho(self):
        return self.__baralho
    @baralho.setter
    def baralho(self, valor):
        self.__baralho = valor
        
    @property
    def listNaipes(self):
        return self.__listNaipes
    @listNaipes.setter
    def listNaipes(self, valor):
        self.__listNaipes = valor
        
    @property
    def listValores(self):
        return self.__listValores
    @listValores.setter
    def listValores(self, valor):
        self.__listValores = valor
    
            
    # Percorre todos os naipes e valores para criar as cartas ordenadas por naipe e número
    def createBaralhoOrdenado(self):
        for naipe in self.__listNaipes:
            for valor in self.__listValores:
                carta = f'{valor}{naipe}'
                self.__baralho.insereNo(carta)
        return self.__baralho

    def embaralhar(self): #Criando ACE
        ace = LEncadeada()
        for i in range(self.__baralho.size()):
            valor = random.randint(0, self.__baralho.size() - 1) #Seleciona um valor aleatório entre 0 e o tamanho do baralho
            ace.insereNo(self.__baralho.removePorindex(int(valor))) # Remove do baralho a carta, criando o novo baralho ACE
        return ace
    
    def printBaralho(self):
        # Imprime o baralho
        print(self.__baralho)