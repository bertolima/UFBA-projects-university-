# ##################################################
#           Classe ACE                             #
# ##################################################
from cCarta import cCarta
class cACE:

    # *******************************************************
    def __init__(self, n=52):
        self.vPilha = [None]*n
        self.maxElem = n
        self.topo = 0

    # *******************************************************
    def __str__(self):
        outStr = ""
        if self.topo == 0:
            outStr += "     ................................ \n"
            outStr += "    |         Monte Vazio            |\n"
            outStr += "     ................................ \n"
            return outStr
        else:
            outStr += self.imprime_topo()
            outStr += f'{"":->5}\n'
            outStr += "   | Monte:  [ "
            j = 0
            carta_cor = cCarta()
            for m in range(self.topo):
                carta_cor = self.vPilha[m]
                outStr += f' {carta_cor.lista_de_posicoes[carta_cor.getPosicao()]}{carta_cor.lista_de_naipes[carta_cor.getNaipe()]} '
                j += 1
            outStr += " ]  |\n"
            outStr += f'   {"":->35}\n'
            outStr += f'   Total de cartas: {self.topo}\n'
        return outStr

    # *******************************************************
    # *******************************************************
    def imprime_topo(self):
        carta_topo = cCarta()
        n = "\033[;1m"
        c = "\033[1;31m"
        r = "\033[0;0m"
        if self.empty():
            outStr = ""
            outStr += f'   {"":_>25}\n'
            outStr += f'   | Monte:  -> {"Vazio":^4} <-  |\n'
            outStr += f'   {"":¨>25}\n'
            return outStr
        else:
            outStr = ""
            outStr += f'   {"":_>18}\n'
            outStr += f'   | Topo: '
            carta_topo = self.pop()
            outStr += f'  {n}{carta_topo.lista_de_posicoes[carta_topo.getPosicao()]}{carta_topo.lista_de_naipes[carta_topo.getNaipe()]:^3} {r}  |\n'
            self.push(carta_topo)
            outStr += f'   {"":->30}'
            return outStr

    # *******************************************************
    # *******************************************************
    def imprime_ultimo_par(self):
        n = "\033[;1m"
        c = "\033[1;31m"
        r = "\033[0;0m"
        if self.empty():
            outStr = ""
            outStr += f'  {"":_>25}\n'
            outStr += f'  | Monte:  -> {"Vazio":^4} <-  |\n'
            outStr += f'  {"":¨>25}\n'
            return outStr
        else:
            outStr = ""
            outStr += f'  {"":_^35}\n'
            outStr += f'  | Monte: Último par: '
            carta_topo = self.pop()
            carta_ant = self.pop()
            outStr += f' {carta_ant.lista_de_posicoes[carta_ant.getPosicao()]}{carta_ant.lista_de_naipes[carta_ant.getNaipe()]:^3} '
            outStr += f' {n}{carta_topo.lista_de_posicoes[carta_topo.getPosicao()]}{carta_topo.lista_de_naipes[carta_topo.getNaipe()]:^3} {r} |\n'
            self.push(carta_ant)
            self.push(carta_topo)
            outStr += f'  {"":->35}\n'
            outStr += f'  Total de cartas do monte: {self.size()}\n'
            return outStr

    # *******************************************************
    # *******************************************************
    def imprime_carta_topo(self):
        carta_cor = self.pop()
        if carta_cor.getPosicao() == 0:
            outStr = ""
            outStr += f'{"":.<10}\n'
            outStr += f'| {carta_cor.lista_de_posicoes[self.vPilha[self.topo - 1].getPosicao()]:4} |\n'
            outStr += f'| {carta_cor.lista_de_naipes[self.vPilha[self.topo - 1].getNaipe()]:^4}  |\n'
            outStr += f'| {carta_cor.lista_de_posicoes[self.vPilha[self.topo - 1].getPosicao()]:4} |\n'
            outStr += f'{"":¨>9}'
            return outStr
        outStr = ""
        outStr += f'{"":.>9}\n'
        if self.topo == 0:
            outStr += f'| {"":<5} |\n'
            outStr += f'{" Monte vazio!":""<10}\n'
            return outStr
        outStr += f'| {carta_cor.lista_de_posicoes[self.vPilha[self.topo - 1].getPosicao()]:<5} |\n'
        outStr += f'| {carta_cor.lista_de_naipes[self.vPilha[self.topo - 1].getNaipe()]:^5} |\n'
        outStr += f'| {carta_cor.lista_de_posicoes[self.vPilha[self.topo - 1].getPosicao()]:>5} |\n'
        outStr += f'{"":¨>9}'
        return outStr

    # *******************************************************
    def push(self, k):
        if self.full():
            return False
        self.vPilha[self.topo] = k
        self.topo += 1
        return True

    # *******************************************************
    def pop(self):
        if self.empty():
            return False
        self.topo -= 1
        return self.vPilha[self.topo]

    # *******************************************************
    def empty(self):
        return self.topo == 0

    # *******************************************************
    def full(self):
        return self.topo == self.maxElem

    # *******************************************************
    def size(self):
        return self.topo


# *******************************************************
# ***     Programa de teste da classe cACE            ***
# *******************************************************
if __name__ == '__main__':
    numElementos = 20
    pilha = cACE(numElementos)
    i = 10
    while not pilha.full():
        pilha.push(i)
        print(f'++ {i}')
        i += 3
    while not pilha.empty():
        i = pilha.pop()
        print(f'-- {i}')
