# Atividade 2 - Simulando um Jogo de Baralho
# Aluno: Felipe S. Trebino
# Classe de cCartNo

from cCarta import cCarta

class cCartaNo(cCarta):

# *******************************************************

    def __init__(self, valor, naipe):
        super().__init__(valor, naipe)
        self.__prox = None

# *******************************************************
    def setProx(self, prox):
        if type(prox) == cCartaNo:
            self.__prox = prox
        else:
            self.__prox = None

# *******************************************************
    def getProx(self):
        return self.__prox

# *******************************************************    
    def __eq__(self, carta):
        if type(carta) == cCarta or type(carta) == cCartaNo:
            return carta.getNaipe() == self.getNaipe() and carta.getValor() == self.getValor()
        return False 