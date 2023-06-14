class MonteCartas:
    def __init__(self):
        self.cartas = []
    
    def adicionar_par(self, carta1, carta2):
        # Adiciona um par de cartas ao monte de cartas
        self.cartas.extend([carta1, carta2])
    
    def quantidade_cartas(self):
        # Retorna a quantidade de cartas no monte de cartas
        return len(self.cartas)
    
    def obter_ultimo_par(self):
        # Retorna o último par de cartas adicionado ao monte
        if len(self.cartas) >= 2:
            return self.cartas[-2], self.cartas[-1]
        else:
            return None
    
    def obter_carta_superior(self):
        # Retorna a carta mais recente adicionada ao monte
        if self.cartas:
            return self.cartas[-1]
        else:
            return None
