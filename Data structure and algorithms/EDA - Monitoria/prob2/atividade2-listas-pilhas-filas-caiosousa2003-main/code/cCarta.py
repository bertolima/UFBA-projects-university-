# ##################################################
# Classe nó de uma Lista Duplamente Encadeada
# Utilizada para criar uma carta (objeto) de um deck (LSE)
# Ela pode ser utilizada em outras estruturas LSE como a mão, o monte, etc
# ##################################################

class cCarta:

# *******************************************************
# *******************************************************
    def __init__(self, valor=0, naipe=None):

        self.__valor__ = valor
        self.__naipe__ = naipe
        self.__prox__ = None
        self.__ante__ = None

# *******************************************************
# *******************************************************
    def __str__(self):

        outStr = ""

        if self:
            outStr +=  "+======+=================+\n"
            outStr += f'| {self.cartasEsp():4} de {self.__naipe__} | {hex(id(self.__prox__))} | {hex(id(self))} \n'
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
    def setProx(self, prox):
        if type(prox) == cCarta:
            self.__prox__ = prox
        else:
            self.__prox__ = None

# *******************************************************
# *******************************************************
    def setAnte(self, ante):
        if type(ante) == cCarta:
            self.__ante__ = ante
        else:
            self.__ante__ = None
            
# *******************************************************
# *******************************************************
    def getValor(self):
        return self.__valor__

# *******************************************************
# *******************************************************
    def getNaipe(self):
        return self.__naipe__

# *******************************************************
# *******************************************************
    def getDado(self):
        return f'{self.cartasEsp()} de {self.__naipe__}'

# *******************************************************
# *******************************************************
    def getProx(self):
        return self.__prox__ 
    
# *******************************************************
# *******************************************************
    def getAnte(self):
        return self.__ante__

# *******************************************************
# *******************************************************
    def cartasEsp(self):
        if self.__valor__ == 1:
            return 'Às'
        elif self.__valor__ == 11:
            return 'Valete'
        elif self.__valor__ == 12:
            return 'Dama'
        elif self.__valor__ == 13:
            return 'Rei'
        else:
            return str(self.__valor__)
# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    carta_vazia      = cCarta()   
    carta_1_paus = cCarta(1, 'Paus')

    print(str(carta_vazia))
    print(str(carta_1_paus))

    carta_vazia.__valor__ = 2
    carta_vazia.__naipe__ = 'Ouro'
    carta_vazia.setProx(carta_1_paus)
    
    print(carta_1_paus.getValor())
    print(carta_1_paus.getNaipe())
    print(carta_1_paus.getDado())
    print('')
    print(carta_vazia.getValor())
    print(carta_vazia.getNaipe())
    print(carta_vazia.getDado())
        
    print(str(carta_vazia))
    print(str(carta_1_paus))