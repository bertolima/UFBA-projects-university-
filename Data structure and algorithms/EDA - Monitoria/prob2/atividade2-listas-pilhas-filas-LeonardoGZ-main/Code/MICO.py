import random
from TADs import ListaEncadeada, Pilha, Fila
import TADs


class Carta: #Define a classe carta e seus parametros
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        self.cor = self.definir_cor()

    def __repr__(self):
        return f"{self.valor} de {self.naipe}"
    
    def definir_cor(self):
        if self.naipe == "Paus" or self.naipe == "Espadas":
            return "\033[30m"  # Preto
        else:
            return "\033[31m"  # Vermelho

    def __str__(self):
        return f"{self.valor} de {self.cor}{self.naipe}\033[0m"

class Jogador: #Define a classe jogador e seus parametros 
    def __init__(self, nome):
        self.nome = nome
        self.mao = ListaEncadeada()
        self.monte = Pilha()

    def obter_mao(self):
        return self.mao
    
    def escolher_carta_aleatoria(self):
        mao_jogador = ListaEncadeada.converter_em_lista(self.mao)
        carta_aleatoria = random.choice(mao_jogador)
        return  carta_aleatoria


class JogoMico: #Define o jogo, os parametros, e ações necessárias para o funcionamento
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.baralho = ListaEncadeada()
        self.ace = Pilha()
        self.mico = None

    def criar_baralho(self): 
        naipes = ["Paus", "Ouros", "Copas", "Espadas"]
        valores = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Rainha", "Rei"]
        for naipe in naipes:
            for valor in valores:
                carta = Carta(valor, naipe)
                self.baralho.inserir_no_fim(carta)

    def embaralhar_baralho(self): 
        cartas = []
        while not self.baralho.esta_vazia():
            carta = self.baralho.cabeca.dado
            self.baralho.remover(carta)
            TADs.add(cartas, carta)
        random.shuffle(cartas)
        for carta in cartas:
            self.baralho.inserir_no_fim(carta)

    def distribuir_cartas(self):

        carta_mico = self.baralho.cabeca.dado
        self.baralho.remover(carta_mico)
        jogadores =list(self.jogadores)
        num_cartas = (self.baralho.tamanho) 
        num_jogadores = TADs.size(jogadores)
        cartas_por_jogador = num_cartas // num_jogadores
        for jogador in self.jogadores:
            prox_jogador = self.jogadores[((self.jogadores.index(jogador))+1) % TADs.size(self.jogadores)]
            for _ in range(cartas_por_jogador):
                carta = self.baralho.cabeca.dado
                self.baralho.remover(carta)
                jogador.mao.adicionar_carta(carta)

                if (num_jogadores % 2) == 0:
                    if jogador.mao.tamanho == prox_jogador.mao.tamanho:
                        carta = self.baralho.cabeca.dado
                        self.baralho.remover(carta)
                        jogador.mao.adicionar_carta(carta)
                    else:
                        continue

    def pares_inicio(self): # Compara os pares nas mão dos jogadores
        for jogador in self.jogadores:
            cartas_na_mao = []  # Lista para armazenar as cartas na mão do jogador
            pares = []  # Lista para armazenar os pares encontrados

            no_atual = jogador.mao.cabeca

            while no_atual is not None:
                carta = no_atual.dado

                if carta is not None:
                    TADs.add(cartas_na_mao, carta)

                no_atual = no_atual.proximo

            for i in range(TADs.size(cartas_na_mao)):
                for j in range(i + 1, TADs.size(cartas_na_mao)):
                    if cartas_na_mao[i].valor == cartas_na_mao[j].valor and cartas_na_mao[i].cor == cartas_na_mao[j].cor:
                        TADs.add(pares, cartas_na_mao[i])
                        TADs.add(pares, cartas_na_mao[j])

            for carta in pares:
                jogador.mao.remover(carta)
                jogador.monte.empilhar(carta)

        
     
    def jogar_rodada(self): # Realiza a jogada de cada jogador em uma rodada          
        for jogador in self.jogadores:    
           # Cada jogador retira uma carta aleatória da mão de outro jogador
            prox_jogador = self.jogadores[((self.jogadores.index(jogador))+1) % TADs.size(self.jogadores)] 
            if prox_jogador.mao.esta_vazia() is False:
                nova_carta = Jogador.escolher_carta_aleatoria(prox_jogador)
                jogador.mao.adicionar_carta(nova_carta)
                prox_jogador.mao.remover(nova_carta)
            else:
                break
            
          
            print(f"\nVez de {jogador.nome}:\n")
            print(f"{jogador.nome} pegou a carta {nova_carta} de {prox_jogador.nome}")
            print(f"{jogador.nome}: {jogador.mao}\n")
            
            self.pares_inicio()
            print(f"Monte de {jogador.nome}: {jogador.monte}\n\n")
            
            
    def iniciar_jogo(self): 
        self.criar_baralho()
        self.embaralhar_baralho()
        self.mico = self.baralho.cabeca.dado
        self.distribuir_cartas()
        
        self.baralho.remover(self.mico)
        print("Começando o jogo do Mico!")
        print("Mico:", self.mico)
        print("Distribuindo cartas para os jogadores...\n")
        for jogador in self.jogadores:
            print(f"{jogador.nome}: {jogador.mao}\n")

            print(f"Verificando pares de {jogador.nome} antes da primeira rodada\n")  
           
            self.pares_inicio()

            print(f"Monte de {jogador.nome}: {jogador.monte}\n")

            print(f"Cartas de {jogador.nome} sem pares: {jogador.mao}\n")
           

        print("Iniciando as rodadas...\n")
        while True:
            for jogador in self.jogadores:
                if jogador.mao.esta_vazia() is True:
                    self.jogadores.remove(jogador)
                   
                self.jogar_rodada()
                prox_jogador = self.jogadores[((self.jogadores.index(jogador))+1) % TADs.size(self.jogadores)]
                
                if jogador.mao.esta_vazia() is not True  and prox_jogador.mao.esta_vazia() is True:
                    print(f"{jogador.nome} é o perdedor!")
                    acabou = True
                    return acabou


    