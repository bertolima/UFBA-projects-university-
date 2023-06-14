# Lab 08 - Pilhas e Filas
# Criando uma Classe No para uma Fila baseada em Lista Simplesmente Encadeada

class cNo:

# *******************************************************
# *******************************************************
    def __init__(self, dado=None):

        self.__dado__ = dado
        self.__prox__ = None

# *******************************************************
# *******************************************************
    def __str__(self):

        outStr = ""
        outStr +=  "+======+=================+\n"
        outStr += f'| {self.__dado__:4} | {id(self.__prox__)} |\n'
        outStr +=  "+======+=================+\n"
        outStr +=  "                 |   \n"
        outStr +=  "                 |   \n"
        outStr +=  "           +-----+   \n"
        outStr +=  "           |            \n"
        if self.__prox__:
            outStr +=  "           V            \n"
        else:
            outStr +=  "           =            \n"
        return outStr

# *******************************************************
# *******************************************************
    def setDado(self, dado):

        # if type(dado) == int:
            self.__dado__ = dado

# *******************************************************
# *******************************************************
    def setProx(self, prox):

        # if type(prox) == cNo:
            self.__prox__ = prox

# *******************************************************
# *******************************************************
    def getDado(self):
        return self.__dado__

# *******************************************************
# *******************************************************
    def getProx(self):
        return self.__prox__ 
