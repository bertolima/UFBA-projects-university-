import random

class Carta:
    def __init__(self, naipe, value):
        self.naipe = naipe
        self.value = value
        self.next = None
        
class Baralho:
    def __init__(self):
        self.head = None

    def add_carta(self, naipe, value):
        carta = Carta(naipe, value)
        if self.head is None:
            self.head = carta
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = carta
            

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.hand = Baralho()
        self.pares = Baralho()
        
class Mico:
    def __init__(self, num_jog):
        self.baralho = Baralho()
        self.jogadores = []
        self.jogador_atual = None

        # Cria o baralho
        for naipe in ['Copas', 'Ouros', 'Paus', 'Espadas']:
            for value in range(1, 14):
                self.baralho.add_carta(naipe, value)

        # Embaralha as cartas
        self.embaralhar()

        # Cria os jogadores
        for i in range(num_jog):
            jogador = Jogador(f'Jogador {i+1}')
            self.jogadores.append(jogador)
            
    #método para embaralhar o baralho
            
    def embaralhar(self):
        cartas = []
        atual = self.baralho.head
        while atual:
            cartas.append((atual.naipe, atual.value))
            atual = atual.next

        random.shuffle(cartas) #embaralha as cartas dentro da lista "cartas"

        self.baralho = Baralho()
        for naipe, value in cartas:
            self.baralho.add_carta(naipe, value)

    def distribuir(self):
        atual = self.baralho.head
        jogador_index = 0
        while atual:
            jogador = self.jogadores[jogador_index]
            jogador.hand.add_carta(atual.naipe, atual.value)
            atual = atual.next
            jogador_index = (jogador_index + 1) % len(self.jogadores)
            #distribui as cartas pra cada jogador
            
    def inicio(self):
        self.jogador_atual = random.choice(self.jogadores)

        while not self.is_game_over():
            print(f"\nJogador Atual: {self.jogador_atual.nome}")
            self.display_game_state()
            self.jogada()
            self.jogador_atual = self.get_prox_jogador()

        print("\nFim de jogo!")
        self.display_game_state()
        self.vencedor()
        
    def jogada(self):
        
        jogador_alvo = random.choice(self.jogadores)
        if jogador_alvo == self.jogador_atual:
            return

        carta = self.jogador_atual.hand.head
        prev_carta = None

        while carta:
            if carta.naipe == jogador_alvo.hand.head.naipe or carta.value == self.jogador_atual.hand.head.value:
                print(f"{self.jogador_atual.nome} pegou a carta de {jogador_alvo.nome}")
                self.jogador_atual.hand.add_carta(jogador_alvo.hand.head.naipe, jogador_alvo.hand.head.value)
                jogador_alvo.hand.head = jogador_alvo.hand.head.next
                if prev_carta:
                    prev_carta.next = carta.next
                else:
                    self.jogador_atual.hand.head = carta.next
                carta.next = None
                self.verifica_par(self.jogador_atual)
                return
            prev_carta = carta
            carta = carta.next

        self.jogador_atual.hand.add_carta(self.baralho.head.naipe, self.baralho.head.value)
        self.baralho.head = self.baralho.head.next
        self.verifica_par(self.jogador_atual)
        
    def verifica_par(self, jogador):
        carta = jogador.hand.head
        while carta and carta.next:
            if carta.naipe == carta.next.naipe and carta.value == carta.next.value:
                print(f"{jogador.nome} achou o par: {carta.value} de {carta.naipe}")
                jogador.pares.add_carta(carta.naipe, carta.value)
                jogador.pares.add_carta(carta.next.naipe, carta.next.value)
                jogador.hand.head = carta.next.next
                carta = jogador.hand.head
            else:
                carta = carta.next
                
    def is_game_over(self):
        return all([jogador.hand.head is None for jogador in self.jogadores])  
    
    def get_prox_jogador(self):
        index = self.jogadores.index(self.jogador_atual)
        return self.jogadores[(index + 1) % len(self.jogadores)]
    
    def display_game_state(self):
        for jogador in self.jogadores:
            print(f"\n Mão {jogador.nome}:")
            self.display_cartas(jogador.hand)
            print(f"\n  Par do {jogador.nome}:")
            self.display_cartas(jogador.pares)

    def display_cartas(self, baralho):
        carta = baralho.head
        while carta:
            print(f"{carta.value} of {carta.naipe}")
            carta = carta.next

    def vencedor(self):
        max_par = 0
        vencedores = []
        for jogador in self.jogadores:
            num_par = self.conta_par(jogador)
            if num_par > max_par:
                max_par = num_par
                vencedores = [jogador]
            elif num_par == max_par:
                vencedores.append(jogador)

        if len(vencedores) == 1:
            print(f"\n{vencedores[0].nome} ganhou com {max_par} pares!")
        else:
            nomes = ', '.join([jogador.nome for jogador in vencedores])
            print(f"\nempate entre  {nomes} com {max_par} pares!")
            
    def conta_par(self, jogador):
        count = 0
        carta = jogador.pares.head
        while carta:
            count += 1
            carta = carta.next
        return count

game = Mico(3)  # Cria o jogo com 3 jogadores
game.inicio()    # Inicia o jogo