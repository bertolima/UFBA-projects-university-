import random
import cCartas
import cNo

class cBaralho:

# *******************************************************
    def __init__(self, n):
        self.vPilha = [''] * 52
        self.maxElem = 52
        self.topo = 0
        self._criaBaralho()
        self.mico = self.pop()
        self.numJogadores = n
        self.perdedor = ''
        self.rodada = 0
        self.jogadores = []

        for c in range(n):
            self.jogadores += [jogador()]

# *******************************************************

    def _criaBaralho(self):
        """Cria um baralho já embaralhado. """

        """ Escolhi fazer assim, mas poderia criar um baralho ordenado e depois 
        inserir na pilha as cartas de forma aleatoria. 
        Ex do código: 
            laço:
                indiceAleatorio = random.randint(0, self.numMax -2) #-1 do mico e -1 pq é um indice. 
                cartaEscolhida = listaDeCartas[indiceAleatorio] 
                self.push(cartaEscolhida)
            """

        naipe = ['Copas', 'Paus', 'Ouros', 'Espadas']
        especiais = ['A', 'K', 'Q', 'J']
        baralho = []
        vazio = True

        # Forma as cartas de 1 - 10 e adciona elas a lista.
        for i in naipe:
            for c in range(2, 11):
                carta = str(c) + ' - ' + i
                while vazio:

                    # Precisei tratar a pilha como uma lista nesse momento para inserir a carta no indice sorteado.
                    indice = random.randint(0, 51)
                    if self.vPilha[indice] == '':
                        self.vPilha[indice] = carta
                        vazio = False
                vazio = True

            # Forma as cartas de A - J e adciona elas a lista.
            for c in especiais:
                carta = str(c) + ' - ' + i
                while vazio:
                    indice = random.randint(0, 51)
                    if self.vPilha[indice] == '':
                        self.vPilha[indice] = carta
                        vazio = False
                vazio = True
        self.topo = 51

# *******************************************************
    def top(self):
        """Retorna o ultimo elemento da pilha."""

        return self.vPilha[self.topo]

# *******************************************************
    def pop(self):
        """Remove e retorna o ultimo elemento da pilha."""

        if self.empty():
            return
        else:
            topo = self.top()
            del(self.vPilha[self.topo])
            self.topo -= 1
        return topo

# *******************************************************

    def empty(self):
        """Diz se ta vazia."""

        if self.topo == -1:
            return True
        return False

    def distribuiCartas(self):
        """Distribui as cartas de forma alternada para os jogadores."""

        c = 1
        while not self.empty():
            for jogador in self.jogadores:
                jogador.cartas.insereNoFim(self.pop())
                if self.empty():
                    break
                if c <= self.numJogadores:
                    jogador.nome = f'J{c}'
                    c+=1

    def mostraCartas(self):
        """Printa as cartas dos jogadores da Lista e a ultima carta do monte."""

        for jogador in self.jogadores:
            f = f'Cartas na mão do {jogador.nome}: {jogador.cartas}'
            print('{:.<135}'.format(f), f'Ultimas Cartas do monte do {jogador.nome}: ', '\033[31m', f'[{jogador.cartas.monte[jogador.cartas.numMonte-1]}], [{jogador.cartas.monte[jogador.cartas.numMonte-2]}]', '\033[m',)


    def pegaCarta(self):
        """Pega a carta do proximo jogador e da para o primeiro no indice escolhido"""

        # Controle para sair do loop quando so restar o perdedor.
        controle = self.numJogadores
        if self.numJogadores == 1:
            controle = 0

        while controle == self.numJogadores:
            c = 0
            for z in range(self.numJogadores):

                # Printa a rodada
                self.rodada += 1
                print('\033[1;34m', f'\nRodada {self.rodada}', '\033[m')

                # Controla os indices dos jogadores que irão dar e receber.
                i = c+1
                if c == self.numJogadores -1:
                    i = 0

                # Enquanto o jogador tiver cartas na mão.
                if self.jogadores[i].cartas.__inicio__.__prox__ is not None:

                    # Indice que simula a escolha da carta que será tirada da mão de outro jogador.
                    escolha = random.randint(0, self.jogadores[i].cartas.numCartas)

                    # tira uma carta de um jogador e da para o proximo.
                    self.jogadores[c].cartas.insereNoFim(self.jogadores[i].cartas.removeCartaEscolhida(escolha))

                    # Informações da rodada.
                    print(f'Jogador {self.jogadores[c]} pegou do {self.jogadores[i]}\n')
                    self.mostraCartas()

                    # Se o jogador[c] não tiver mais cartas, remove ele da lista.
                    if self.jogadores[c].cartas.separaPar():
                        del (self.jogadores[c])
                        self.numJogadores -= 1
                        c -=1

                        # Se o jogador[c] estiver antes do jogador[i] precisa atualizar o i.
                        if c < i:
                            i -= 1

                    # Se o jogador[i] não tiver mais cartas, remove ele da lista.
                    if self.jogadores[i].cartas.separaPar():
                            del (self.jogadores[i])
                            self.numJogadores -= 1
                            c-=1
                c += 1

    def iniciaRodada(self):
        """Inicia a etapa de pegar as cartas."""

        for c in range(self.numJogadores):
            self.pegaCarta()
        if self.perdedorMico():
            print(f'\nPerdedor: ', '\033[31m', f'{self.perdedor}.', '\033[m', f'\nSua Carta: ', '\033[31m', f'{self.jogadores[0].cartas}', '\033[m', '\nMico: ', '\033[31m',f'{self.mico}', '\033[m')


    def perdedorMico(self):
        """Se sobrar apenas um jogador define ele como o perdedor"""

        if self.numJogadores == 1:
            self.perdedor = self.jogadores[0].nome
            return True
        return False


#*********************************************************

class jogador:

    def __init__(self):
        self.cartas = cCartas.cCartas()
        self.nome = ''
        self.monte = self.cartas.monte
        self.numCartasJogador = self.cartas.numCartas

    def __str__(self):
        return self.nome

