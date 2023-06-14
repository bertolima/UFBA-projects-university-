# Lab 08 - Pilhas e Filas
# Criando uma Classe No para uma Fila baseada em Lista Simplesmente Encadeada

class No:

    def __init__(self, dado=None):

        self.__dado = dado
        self.__prox = None

    @property
    def dado(self):
        return self.__dado
    @dado.setter
    def dado(self, value):
        self.__dado = value
    
    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self, value):
        self.__prox = value
        
    def setDado(self, dado):
            self.__dado = dado

    def setProx(self, prox):
         self.__prox__ = prox

    def getDado(self):
        return self.__dado

    def getProx(self):
        return self.__prox 
