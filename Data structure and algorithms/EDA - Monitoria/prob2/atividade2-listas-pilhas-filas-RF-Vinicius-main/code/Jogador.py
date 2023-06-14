from ListaEncadeada import LEncadeada
from Pilha import Pilha
import random

class Jogador:
    
    def __init__(self, mao = LEncadeada(), monteCartas = Pilha(52), nomeJogador = ''):
        self.__mao = mao
        self.__monteCartas = monteCartas
        self.__nome = nomeJogador
    
    @property
    def mao(self):
        return self.__mao
    @mao.setter
    def mao(self, value):
        self.__mao = value
        
    @property
    def monteCartas(self):
        return self.__monteCartas
    @monteCartas.setter
    def monteCartas(self, value):
        self.__monteCartas = value
        
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    def adicionarCartaMao(self, carta):
        if self.verificarPares(carta): #Antes de adicionar, percorre a mão e verifica se já existe o par dela. Existindo, armazena no monte
            return
        self.__mao.insereNo(carta) # Caso não exista a carta par na mão, insere a nova carta
    
    def escolherCarta(self, proxJogador):
        #Mao é uma Lista encadeada. O removePorindex seleciona uma carta da mão, com base no index e remove retornando o valor
        cartaEscolhida = proxJogador.mao.removePorindex(random.randint(0, proxJogador.mao.size() - 1)) #Seleciona aleatóriamente uma carta da mão do próximo jogador
        self.adicionarCartaMao(cartaEscolhida) #Adiciona carta na mão do jogador que está jogando
        return cartaEscolhida
        
    def verificarPares(self, carta):
        cartaMao = self.__mao.inicio
        while True:  
            try:
                #A cor foi definida pela regra de negócio da minha aplicação como sendo (V) ou (P), esse valor acompanha cada carta, logo após o numero
                if (carta[:4] == cartaMao.dado[:4]): #Verifica se é o mesmo número e mesma cor
                    self.adicionarCartaMonte(cartaMao, carta) #Se for, adiciona no monte
                    return True
                elif cartaMao.prox is None: #Se for a última carta da mão, finaliza a verificação
                    return False
                cartaMao = cartaMao.prox
            except AttributeError:
                return False
            
    def stateJogador(self):
        return f"""
                ##### Jogador {self.__nome} #####                      
                Mão: {self.__mao}
                Monte: {self.__monteCartas.getElemTopo()}
                Quantidade cartas monte: {self.__monteCartas.size()}
            """
            
    
    def adicionarCartaMonte(self, cartaMao, carta2):
        self.__monteCartas.push(cartaMao.dado) # Adiciona a carta no monte
        self.__mao.removeNo(cartaMao.dado) # Retira a carta adicionada da mão do jogador
        self.__monteCartas.push(carta2) # Adiciona nova carta no monte 
        