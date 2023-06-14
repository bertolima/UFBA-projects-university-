
# Clase Carta
class carta:

# *******************************************************
# *******************************************************
    def __init__(self, valor, naipe):

        self.__carta__ = valor
        self.__naipe__ = naipe

    def getCarta(self):
        return self.__carta__

    def getNaipe(self):
        return self.__naipe__

    def imprimirCarta(self):
        return f'Naipe: {self.getNaipe()}; Carta: {self.getCarta()}'
        # return f'{self}'
    def __str__(self):
        return f'{self.getCarta()} de {self.getNaipe()}'  # Naipe: {self.getNaipe()};
