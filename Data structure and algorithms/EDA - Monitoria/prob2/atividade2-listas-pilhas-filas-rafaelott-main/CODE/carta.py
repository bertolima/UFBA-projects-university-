class Carta:
    def __init__(self, naipe, posicao):
        self.naipe = naipe
        self.posicao = posicao

    def __str__(self):
        return f'{self.posicao} de {self.naipe}'
    
    
    
# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':
    carta = Carta("copas", "2")
    print(carta)