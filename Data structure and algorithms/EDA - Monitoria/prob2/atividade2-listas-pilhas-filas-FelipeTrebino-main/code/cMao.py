# Atividade 2 - Simulando um Jogo de Baralho
# Aluno: Felipe S. Trebino
# Classe de cMao

from cCartaNo import *
from cBaralho import *

# *******************************************************
class cMao:

# *******************************************************
    def __init__(self):
        self.__inicio     = None
        self.__numElems   = 0
        self.__pilhaCartas = cBaralho(28)

# *******************************************************
    def __len__(self):
        return self.__numElems

# *******************************************************
    def __str__(self):

        outStr = ""

        if self.__inicio == None:        
            outStr += "=====================\n"
            outStr += "|   MÃO   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            noCorrente = self.__inicio
            while(noCorrente.getProx() != None):
                outStr += str(noCorrente)
                noCorrente = noCorrente.getProx()
            outStr += str(noCorrente)
        return outStr

# *******************************************************
    # Retorna a pilha de cartas que sairam da mão 
    def getPilhaCartas(self):
        return self.__pilhaCartas

# *******************************************************
    # Retorna as duas últimas cartas que sairam da mão
    def getUltimoPar(self):
        pilha = self.getPilhaCartas().clone()
        return f"{pilha.pop()}, {pilha.pop()}"

# *******************************************************
    # Método para inserir novas cartas no baralho
    def insereCarta(self, cartaNo):
        # Transforma uma carta comum em cartaNo
        if type(cartaNo) == cCarta:
            cartaNo = cCartaNo(cartaNo.getValor(), cartaNo.getNaipe())

        if self.__inicio is None:
            self.__inicio = cartaNo
            self.__numElems += 1
            return

        noCorrente = self.__inicio
        while(noCorrente.getProx() is not None):
            noCorrente = noCorrente.getProx()            
        
        noCorrente.setProx(cartaNo)
        self.__numElems += 1

# *******************************************************
    # Método que busca se há uma carta no baralho e retorna sua posição
    def busca(self, cartaNo):
        p = 0
        if self.__inicio is None:
            return False, -1
        noCorrente = self.__inicio
        while(noCorrente is not None):
            if noCorrente == cartaNo:
                return True, p
            noCorrente = noCorrente.getProx()
            p+=1
        return False, -1
    
# *******************************************************
    # Método para remover cartas
    def removeCarta(self, cartaNo):
        if self.__inicio is None:
            return False
        noCorrente = self.__inicio
        noAnterior = None
        while(noCorrente is not None):
            if noCorrente == cartaNo:
                if noAnterior is None:
                    if noCorrente.getProx() is not None:
                        self.__inicio = noCorrente.getProx()
                    else:
                        self.__inicio = None
                    self.__numElems -= 1
                    return True
                noAnterior.setProx(noCorrente.getProx())
                self.__numElems -= 1
                return True
            noAnterior = noCorrente
            noCorrente = noCorrente.getProx()
        return False
            
# *******************************************************
    # Método para remover pares do baralho, retorna o último par que foi removido
    def removePares(self):
        remove = False
        if len(self) == 0:
            return None, None
        noCompara = self.__inicio
        while noCompara is not None:
            if not self.busca(noCompara)[0]:
                noCompara = noCompara.getProx()
                continue
            noCorrente = noCompara.getProx()
            while noCorrente is not None:
                if noCompara.compareValue(noCorrente):
                    self.removeCarta(noCompara)
                    self.removeCarta(noCorrente)
                    self.getPilhaCartas().push(noCompara)
                    self.getPilhaCartas().push(noCorrente)
                    remove = True
                    break
                else:
                    noCorrente = noCorrente.getProx()
            noCompara = noCompara.getProx()
        return remove

# *******************************************************
    # Método que remove e retorna uma carta no baralho baseado na sua posição
    def removeCartaEscolhida(self, n):
        if n > len(self) - 1 or n < 0:
            return None
        carta = self.__inicio
        for _ in range(n):
            carta = carta.getProx()
        self.removeCarta(carta)
        carta.setProx(None)
        return carta

if __name__ == '__main__':
    #Criar Cartas e Mão
    carta1 = cCarta(1,'Copas')
    carta2 = cCarta(1,'Espadas')
    carta3 = cCarta(1,'Paus')

    carta4 = cCarta(2, 'Copas')
    carta5 = cCarta(2, 'Paus')

    mao = cMao()

    #Inserir Cartas
    mao.insereCarta(carta1)
    mao.insereCarta(carta2)
    mao.insereCarta(carta3)
    
    print(f"Mão inicial: {mao}\n")

    mao.removePares()

    # Teste de remoção de pares
    print(f"Remove pares: {mao}\n")

    mao.insereCarta(carta4)
    mao.insereCarta(carta5)

    # Teste para acessar duas últimas cartas
    print(f"Mão intermediaria: {mao}\n")

    mao.removePares()

    print(f"Mão final: {mao}\n")

    print(mao.getUltimoPar())