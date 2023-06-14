# Ruan Cardoso dos Santos 220121212 04/06/2023

class Jogador:
    def __init__(self, nome, numero): # Classe Jogador gera um jogador com seu nome e um número, além de uma lista, a princípio vazia, das cartas do jogador.
        self.nome = nome
        self.numero = numero
        self.cartas = []
        return
    
    def receberCarta(self, carta): # Método que irá adicionar uma carta do baralho a lista de cartas do jogador.
        self.cartas.append(carta)

    def mostrarCartas(self): # Exibe todas as cartas que o jogador possui
        print(f'Cartas do jogador {self.numero}. {self.nome}:')
        for carta in self.cartas:
            print(carta)
    
    def removerCarta(self, posicao): # Método que remove a carta apartir de uma posição passada como parâmetro.
        if posicao >= 0 and posicao < len(self.cartas):
            return self.cartas.pop(posicao)
        else:
            return None

    def verificaPares(self): # Método que verifica se há pares de cartas na lista de cartas que o jogador possui, caso haja cartas na lista no momento em que o método é chamado.
        pares = []
        if len(self.cartas) < 2:
            return None
        for i in range(len(self.cartas)):
            primeiraCarta = self.cartas[i]
            for j in range(i+1, len(self.cartas)):
                segundaCarta = self.cartas[j]
                if primeiraCarta.valor == segundaCarta.valor: # Compara, através de um loop duplo, se o valor das cartas selecionadas são iguais.
                    pares.append(primeiraCarta)
                    pares.append(segundaCarta)
        return pares
    
    def temMico(self):
        valores = [carta.valor for carta in self.cartas]
        return len(set(valores) == len(valores))
