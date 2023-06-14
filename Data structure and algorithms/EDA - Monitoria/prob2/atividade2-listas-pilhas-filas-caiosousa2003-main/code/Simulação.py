# ##################################################
# Código para realização da simulação do jogo mico
# ##################################################

# Importação das classes e bibliotecas necessárias para a simulação
import cDeckOrd
import cCarta
import cMonte
import cOrdem
import cJogador
import random as rd
from datetime import datetime
import time

# Inicialização do random
rd.seed(int(datetime.now().strftime('%H%M%S')))

# Estética do terminal
linha = '--------------------------------------------------------------------------------------------------'
print(linha)
print('|                                        JOGO DO MICO                                            |')
print(linha)
print('')

# Definição da quantidade de jogadores
print('DEFINIÇÕES INICIAIS')
Qjogadores = input('Com quantos jogadores você quer simular? (Insira de 2 a 4) ')
print('')

# Criação dos jogadores e da ordem aleatória do jogo
ordem = cOrdem.cOrdem()
ordem_dist = cOrdem.cOrdem()

Qjogadores = int(Qjogadores)
sorteio = rd.sample(range(1, Qjogadores+1), Qjogadores) # Geração da aleatoriedade

# Algoritmo para criar a fila de ordem do jogo
for i in sorteio: 
    nome = f'Jogador {i}'
    JogadorX = cJogador.cJogador(nome)
    ordem.enfileirar(JogadorX)
    ordem_dist.enfileirar(JogadorX)

print(f'A ORDEM DO JOGO SERÁ: {ordem} \n')

# Geração de um baralho de cartas ordenado
time.sleep(1)
print('----------------------------------------VAMOS INICIAR-------------------------------------------')
deckOrd = cDeckOrd.cDeckOrd(52) # Criação de um vetor para armazenar o deck ordenado de 52 cartas

naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Algoritmo para criação de um baralho ordenado
for valor in valores:
    for naipe in naipes:
        deckOrd.setCarta(cCarta.cCarta(valor, naipe))

# Embaralhar o deck ordenado e transformá-lo em uma pilha de cartas (ACE)
time.sleep(1)
print('\nEmbaralhando as cartas....')
deckOrd.embaralhar()

baralho = cMonte.cMonte(52) # Criação de um vetor para armazenar o ACE de 52 cartas 

# Armazenamento do baralho (embaralhado) na pilha (ACE)
for i in range(len(deckOrd)):
    baralho.push(deckOrd.getCarta(i))

# Definição do mico
time.sleep(1)
print('Retirando o mico....')
mico = baralho.pop()

# Distribuição das cartas seguindo a ordem de jogo
time.sleep(1)
print('Distribuindo as cartas...\n')

while(not baralho.empty()):
    jogador = ordem_dist.proxTurno() # Percorrer a ordem de distribuição de maneira ordenada
    carta = baralho.pop()
    jogador.getMao().setCarta(carta)

# Apresentação das mãos iniciais de cada jogador (com todas cartas que foram distribuídas)
time.sleep(1)
print(f'{linha}\n')
print('MÃOS INICIAIS')
for i in range(Qjogadores):
    jogador = ordem.proxTurno() 
    time.sleep(2)
    print(f'\n{jogador.setStatus()}\n')
print(linha)

# Apresentação das mãos de cada jogador após a retirada dos pares já formados
time.sleep(1)
print('\nFORMAÇÃO DE PARES INICIAIS\n')
for i in range(Qjogadores):
    jogador = ordem.proxTurno()
    jogador.descartarPares()
    time.sleep(2)
    print(f'{jogador.setStatus()}')
    print(f'Monte de Pares: {jogador.getDesc().getUltPar()}\n')
print(linha)

# Início dos turnos onde cada jogador pegará uma carta do seu sucessor para tentar formar um par
print('\nINÍCIO DOS TURNOS\n')
fim = False
turno = 1

# Criação de uma fila de saída para armazenar os jogadores assim que descartarem todas as cartas
saida = cOrdem.cOrdem()

# Looping do jogo
while not fim:
    time.sleep(1)
    print(f'TURNO {turno}\n')
    for i in range(ordem.size()):
        jogador = ordem.desenfileirar()
    # Caso que o jogador descartou todas as cartas e saiu do jogo 
        if jogador.getMao().isempty():
            time.sleep(2)
            print(f'{linha}\n')
            print(f'{jogador.setStatus()}\n')
            print(f'{linha}\n')
            saida.enfileirar(jogador)
        else:
    # Caso que o jogador é o último e está com o Mico
            if jogador.getProx() == jogador:
                jogador.setMico()
                time.sleep(2)
                print(f'{linha}\n')
                print(f'{jogador.getStatus()}\n')
                print(f'MÃO DO JOGADOR: {jogador.getMao()}')
                print(f'{linha}\n')
                saida.enfileirar(jogador)
                fim = True
    # Caso geral que irá fazer com que o jogo continue (sentido seguindo a fila)    
            else:
                prox = jogador.getProx()
                pos = rd.randint(0, prox.getMao().getTamanho()-1)
                cartaEsc = prox.getMao().buscaPos(pos) # Jogador escolhe uma carta aleatória de acordo com a posição
                prox.getMao().removeNo(cartaEsc)
                time.sleep(2)
                print(f'{linha}\n')
                print(f'{jogador.getName()} pegou a carta {cartaEsc.getDado()} do {prox.getName()}\n')
                chave, cartaEnc = jogador.getMao().buscaPar(cartaEsc) # Jogador busca a carta escolhida dentro da sua mão
                # Caso ele tenha a carta, ela será descartada junto com a escolhida
                if chave: 
                    jogador.getDesc().push(cartaEsc)
                    jogador.getDesc().push(cartaEnc)
                # Caso ele não tenha a carta, ela será inserida na mão dele
                else:
                    jogador.getMao().setCarta(cartaEsc)
                time.sleep(2)
                print('MÃO DO JOGADOR\n')
                print(f'{jogador.setStatus()}')
                print(f'Monte de Pares: {jogador.getDesc().getUltPar()}\n')
                print(f'{linha}\n')
                if jogador.getMao().isempty():
                    saida.enfileirar(jogador)
                else:
                    ordem.enfileirar(jogador)
    turno += 1
    
print('\nRESULTADOS FINAIS DO JOGO\n')
for i in range(Qjogadores):
    jogador = saida.proxTurno() 
    time.sleep(2)
    print(f'\n{jogador.getStatus()}\n')
    
print(f'REVELAÇÃO DO MICO - {mico.getDado()}\n')
print(linha)

print('\nVERIFICAÇÃO DOS MONTES\n')
for i in range(Qjogadores):
    jogador = saida.proxTurno() 
    time.sleep(2)
    print(f'\n{jogador.getName()}: {jogador.getMao()}')
    print(f'Monte de Descarte: {jogador.getDesc()}\n')

print('\n\n|                                             FIM                                               |')