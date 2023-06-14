from CLSE import CLSE
class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    def Par(C1,C2):
        if isinstance(C1, Carta) and isinstance(C2, Carta):
            if C1.valor==C2.valor:
                return True
        else:
            return False
