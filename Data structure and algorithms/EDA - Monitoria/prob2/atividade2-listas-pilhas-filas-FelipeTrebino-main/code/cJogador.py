# Atividade 2 - Simulando um Jogo de Baralho
# Aluno: Felipe S. Trebino
# Classe de cJogador

from cMao import cMao
from cBaralho import cBaralho

class cJogador:

    def __init__(self, name):
        self.__name = name
        self.__mao = cMao()
        self.__pilhaCartas = cBaralho()

# *******************************************************
    def getName(self):
        return self.__name

# *******************************************************
    def getMao(self):
        return self.__mao
    
# *******************************************************
    def setMao(self, mao):
        if type(mao) == cMao:
            self.__mao = mao

# *******************************************************
    def __str__(self):
        return f"{self.getName()} - Mão: {self.getMao()}"

# *******************************************************