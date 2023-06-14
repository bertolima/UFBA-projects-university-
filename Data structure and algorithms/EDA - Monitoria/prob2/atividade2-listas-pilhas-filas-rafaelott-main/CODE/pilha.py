class cPilha:

    def __init__(self, n):
        self.vPilha     = [0] * n 
        self.maxElem    = n 
        self.topo       = 0
        return

    # Empilha
    def push(self, k): 
        if self.full():
            return
        self.vPilha[self.topo] = k
        self.topo += 1
        return

    def pop(self):
        if self.empty():
            return
        self.topo -= 1
        return self.vPilha[self.topo]

    def empty(self):
        return self.topo == 0

    def full(self):
        return self.topo == self.maxElem

    def size(self):
        return self.topo


# *******************************************************
# ***                                                 ***
# *******************************************************

if __name__ == '__main__':
    numElementos = 5
    pilha = cPilha(numElementos)
    i=100
    while(not pilha.full()):
        pilha.push(i)
        print(f'++ {i}')
        i += 3
    while(not pilha.empty()):
        i = pilha.pop()
        print(f'-- {i}')