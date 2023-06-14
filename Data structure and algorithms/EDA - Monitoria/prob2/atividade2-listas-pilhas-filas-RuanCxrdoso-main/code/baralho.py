# Ruan Cardoso dos Santos 220121212 04/06/2023

import random

class Carta:
    def __init__(self, valor, naipe) -> None: # Quando chamada, a classe gera uma carta com um valor e um naipe.
        self.valor = valor
        self.naipe = naipe

    def __repr__(self) -> str:
        return f"{self.valor} / {self.naipe}"

class Baralho:
    def __init__(self) -> None: # Constrói um baralho e armazena um baralho e o seu topo.
        self._cartas = []
        self._top = 0
        self.iniciar()

    def iniciar(self): # Método que gera o baralho em si, com seus naipes e valores.
        self._cartas = []
        naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']
        valores = ['Ás', '2', '3', '4', '4', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
        for naipe in naipes:
            for valor in valores:
                self._cartas.append(Carta(valor, naipe)) # Adiciona a carta, gerada pela classe Carta, no baralho.
                self._top += 1 # Adiciona um à indicação do topo da pilha sempre que é adicionada uma carta no baralho.
      
    def embaralhar(self): # Método que embaralha o baralho através de um algoritmo chamado Fisher-yates.
        for i in range (len(self._cartas) - 1, 0, -1):
            j = random.randint(0, i)
            self._cartas[i], self._cartas[j] = self._cartas[j], self._cartas[i]
        return self._cartas

    def ACE(self): # Método ACE, que embaralha o baralho chamando o método embaralhar() e retorna a lista contendo as cartas do baralho.
        return self.embaralhar()
    
    def distCartas(self): # Método para distribuição das cartas
        if self.vazio() is False: # Caso o baralho não esteja vazio ele retornará a carta do topo da pilha e irá subtrair 1 do atributo _top.
            self._top -= 1
            return self._cartas.pop()
        else:
            return None
    
    def sorteiaMico(self): # Sorteia o mico, gerando um índice aleatório dentro do intervalo que vai de 0 ao tamanho do baralho menos um, e remove do baralho a carta que está alocada neste índice sorteado.
        indexMico = random.randint(0, len(self._cartas))
        return self._cartas.pop(indexMico)

    def vazio(self): # Verifica se o baralho está vazio
        return len(self._cartas) == 0
