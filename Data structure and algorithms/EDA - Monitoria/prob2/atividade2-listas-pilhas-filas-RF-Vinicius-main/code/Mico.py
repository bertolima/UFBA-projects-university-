from Baralho import Baralho
import random
import numpy as np
from ListaEncadeada import LEncadeada
from Jogador import Jogador
from Pilha import Pilha


class Mico:
    
    def __init__(self, numeroJogadores = 2):
        self.__mico = None
        self.__numeroJogadores = numeroJogadores
        self.__baralhoJogo = Baralho() #Instancia o baralho criando um baralho ordenado. REGRA 01
        self.__listJogadores = LEncadeada()
        self.__listVencedores = LEncadeada()
        self.__contadorRodada = 0
        
    @property
    def mico(self):
        return self.__mico
    @mico.setter
    def mico(self, value):
        self.__mico = value
    
    @property
    def numeroJogadores(self):
        return self.__numeroJogadores
    @numeroJogadores.setter
    def numeroJogadores(self, value):
        self.__numeroJogadores = value
    
    @property
    def baralhoJogo(self):
        return self.__baralhoJogo
    @baralhoJogo.setter
    def baralhoJogo(self, value):
        self.__baralhoJogo = value
        
    @property
    def listJogadores(self):
        return self.__listJogadores
    @listJogadores.setter
    def listJogadores(self, value):
        self.__listJogadores = value
    
    
    def retirarCartaAleatoria(self, listCarta): # Seleciona uma carta aleatória do baralho, com base no index e retorna a carta retirada
        listIndex = list(np.linspace(0, listCarta.size() - 1, listCarta.size())) #Cria uma lista de index do tamanho do baralho para criar a ACE  
        return listCarta.removePorindex(int(random.choice(listIndex)))
    
    def iniciarJogo(self):
        self.__baralhoJogo.createBaralhoOrdenado() #Cria um baralho ordenado. REGRA 01
        print('Baralho ordenado: ')
        self.__baralhoJogo.printBaralho() # Exibe baralho ordenado para avaliação da ativiade
        
        self.__baralhoJogo = self.__baralhoJogo.embaralhar() # Cria um ACE a partir de um baralho ordenado.
        print(F"\n ## ACE: {self.__baralhoJogo}") # Exibe ACE para avaliação
       
        self.__mico = self.retirarCartaAleatoria(self.__baralhoJogo) #Define qual é o MICO
    
    def iniciarJogadores(self):#Instancia os jogadores dentro de uma Lista encadeada. Cada valor da lista corresponde a um jogador
        numeroCartasJogador = round(self.__baralhoJogo.size()/self.__numeroJogadores) #O valor máximo da pilha de cada jogador é a divisão do tamanho do baralho pela quantidade de jogadores
        for i in range(self.__numeroJogadores):
            self.__listJogadores.insereNo(Jogador(LEncadeada(), Pilha(numeroCartasJogador), str(i))) 

    def distribuirCartas(self):
        index = 0
        jogador = self.listJogadores.inicio # Iniciar a com o objeto referente ao primeiro jogador
        while(self.__baralhoJogo.size() > 0): # Enquanto existir carta, deve ir distribuindo na ordem do baralho
            jogador.dado.adicionarCartaMao(self.__baralhoJogo.removePorindex(0)) #Usando a função removePorIndex, que retorna o valor removido, adiciona na mão do jogador da vez a primeira carta do baralho
            if jogador.prox is None: #Caso seja o ultimo jogador, instancia novamente jogador como o primeiro e repete até acabar as cartas
                jogador = self.listJogadores.inicio
            else:
                jogador = jogador.prox #Seleciona o próximo jogador

            
    def jogar(self):
        listaJogador = self.__listJogadores
        #Escolhe aleatóriamente o jogador que vai começar para que não tenha um ciclo vicioso
        player = self.__listJogadores.buscaPorIndex(random.randint(0, self.__listJogadores.size() - 1), False)
        jogadorAtual = player # Será usado para exibir a parcial do jogo para avaliação
        while listaJogador.size() > 1:
            if player.prox is None: #Se o jogador for o último da lista, precisa pegar a carta do primeiro da lista. Reiniciando o ciclo
                cartaEscolhida  = player.dado.escolherCarta(listaJogador.inicio.dado)  #Escolhe a carta do primeiro da lista
                if listaJogador.inicio.dado.mao.size() == 0: # Verificar se o próximo jogador ficou sem nenhum carta e remove ele do jogo.
                    self.__listVencedores.insereNo(listaJogador.inicio.dado) # Adiciona jogador com zero cartas na lista de prováveis campeão
                    listaJogador.removeNo(listaJogador.inicio.dado) # Remove jogador da partida
                elif player.dado.mao.size() == 0: # Verifica se o jogador zerou a mão, pois achou o último par
                    self.__listVencedores.insereNo(player.dado) # Insere ele na lista de provável campeao
                    listaJogador.removeNo(player.dado) # Remove jogador da partida
                jogadorAtual = player
                player = listaJogador.inicio # Seleciona o próximo jogador que irá jogar
            
            else:
                # O trecho abaixo repete o if acima, considerando que o próximo jogador não é None
                cartaEscolhida  = player.dado.escolherCarta(player.prox.dado) 
                if player.prox.dado.mao.size() == 0:
                    self.__listVencedores.insereNo(player.prox.dado)
                    listaJogador.removeNo(player.prox.dado)
                elif player.dado.mao.size() == 0:
                    self.__listVencedores.insereNo(player.dado)
                    listaJogador.removeNo(player.dado)
                jogadorAtual = player
                player = player.prox if player.prox is not None else listaJogador.inicio # Se o jogador atual já for o último seleciona o primeiro jogador da lista novamente.
            self.showParcial(cartaEscolhida, player, jogadorAtual)
            
      
    def showParcial(self, cartaEscolhida, proxJogador, jogadorAtual):
        self.__contadorRodada += 1
        emJogo = self.__listJogadores.inicio
        zerouMao = self.__listVencedores.inicio
        
        parcial = f"""
        ############## Rodada: {self.__contadorRodada} ##############
        Carta escolhida na rodada: {cartaEscolhida}
        Jogador Atual: {jogadorAtual.dado.nome}
        Próximo Jogador: Jogador {proxJogador.dado.nome}
        """
        while emJogo: # Adiciona na parcial os jogadores que ainda estão disputando
            parcial += emJogo.dado.stateJogador()
            emJogo = emJogo.prox
        while zerouMao: # Adiciona na parcial os jogadores que já zerou a mão.
            parcial += zerouMao.dado.stateJogador()
            zerouMao = zerouMao.prox
        return print(parcial)
            
    def checkWinner(self): # Verifica quem é o campeam 
        campeao = self.__listVencedores.inicio
        
        #Veifica quem tem o maior monte, caso seja o próximo jogador, atualiza o campeão. Caso contrário, remove o de menor tamanho da lista     
        while campeao.prox:
            
            if campeao.prox.dado.monteCartas.size() >= campeao.dado.monteCartas.size():
                campeao = campeao.prox
            else:
                self.__listVencedores.removeNo(campeao.prox.dado)
                    
        vitoria = f"""
                    ############ VENCEDOR ############
                    Nome: Jogador {campeao.dado.nome}
                    Monte de cartas: {campeao.dado.monteCartas.getElemTopo()}
                    Tamanho monte: {campeao.dado.monteCartas.size()}
                    
                    ############ MICO ################
                    Carta Mico: {self.__mico} 
                     
                    Nome: Jogador {self.__listJogadores.inicio.dado.nome}
                    Cartas: {self.__listJogadores.inicio.dado.mao}
                    Monte: {self.__listJogadores.inicio.dado.monteCartas.getElemTopo()}
                    Tamanho monte: {self.__listJogadores.inicio.dado.monteCartas.size()}
                """
        return vitoria
