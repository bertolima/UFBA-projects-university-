# Atividade 2 - Simulando um Jogo de Baralho
# Aluno: Felipe S. Trebino
# Classe de cFilaTurno

from cJogadorNo import * 

class cFilaTurno:

# *******************************************************
    def __init__(self):
        self._inicio     = None
        self._fim        = None
        self._numElems   = 0

# *******************************************************
    def __len__(self):
        return self._numElems

# *******************************************************
    def queue(self, jogador):

        novoNo = cJogadorNo(jogador.getName())
        novoNo.setMao(jogador.getMao())

        if self._inicio == None:
            self._inicio = novoNo
            self._fim    = novoNo
        else:
            self._fim.setProx(novoNo)
            self._fim = novoNo
        self._numElems += 1

# *******************************************************
    def dequeue(self):

        if self._inicio == None:
            return None

        noCorrente = self._inicio

        self._inicio = noCorrente.getProx()

        self._fim.setProx(noCorrente)

        self._fim = noCorrente

        return noCorrente

# *******************************************************
    def empty(self):
        return self._inicio == None

