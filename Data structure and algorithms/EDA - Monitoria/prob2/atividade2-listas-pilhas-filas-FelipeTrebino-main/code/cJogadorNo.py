# Atividade 2 - Simulando um Jogo de Baralho
# Aluno: Felipe S. Trebino
# Classe de cJogadorNo

from cJogador import cJogador

class cJogadorNo(cJogador):
    def __init__(self, name):
        super().__init__(name)
        self.__prox = None

# *******************************************************
    def setProx(self, prox):
        if type(prox) == cJogadorNo:
            self.__prox = prox
        else:
            self.__prox = None

# *******************************************************
    def getProx(self):
        return self.__prox
