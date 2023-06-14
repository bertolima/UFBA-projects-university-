class MaoJogador:
    def __init__(self):
        self.cartas = []
    
    def adicionar_carta(self, carta):
        # Adiciona uma carta à mão do jogador
        self.cartas.append(carta)
    
    def remover_carta(self, indice):
        # Remove uma carta da mão do jogador pelo índice
        if 0 <= indice < len(self.cartas):
            return self.cartas.pop(indice)
        else:
            return None
    
    def quantidade_cartas(self):
        # Retorna a quantidade de cartas na mão do jogador
        return len(self.cartas)
    
    def obter_carta(self, indice):
        # Retorna a carta da mão do jogador pelo índice
        if 0 <= indice < len(self.cartas):
            return self.cartas[indice]
        else:
            return None
