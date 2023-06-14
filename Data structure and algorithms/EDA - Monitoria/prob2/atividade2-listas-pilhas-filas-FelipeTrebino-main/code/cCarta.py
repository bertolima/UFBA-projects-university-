# Atividade 2 - Simulando um Jogo de Baralho
# Aluno: Felipe S. Trebino
# Classe de cCarta

class cCarta:

# *******************************************************
    def __init__(self, valor, naipe):
        self.__valor = valor
        self.__naipe = naipe

# *******************************************************
    def getValor(self):
        return self.__valor

# *******************************************************
    def getNaipe(self):
        return self.__naipe

# *******************************************************
    def __eq__(self, carta):
        if type(carta) == cCarta or issubclass(type(carta), cCarta):
            return carta.getNaipe() == self.getNaipe() and carta.getValor() == self.getValor()
        return False
    
# *******************************************************
    # Método verifica se uma outra carta possui o mesmo valor
    def compareValue(self, carta):
        if type(carta) == cCarta or issubclass(type(carta), cCarta):
            return carta.getValor() == self.getValor()
        return False
    
# *******************************************************
    def __str__(self):
        return f"({self.getValor()} de {self.getNaipe()})"