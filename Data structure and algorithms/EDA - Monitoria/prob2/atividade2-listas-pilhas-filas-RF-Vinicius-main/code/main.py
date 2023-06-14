from Baralho import Baralho
import random
import numpy as np
from ListaEncadeada import LEncadeada
from Jogador import Jogador
from Pilha import Pilha
from Mico import Mico


if __name__ == "__main__":
    while True:
        try:
            qtdJogadores = int(input('Defina4 a quantidade de jogadores: '))
            if 2 <= qtdJogadores <= 4:
                partida = Mico(qtdJogadores)
                partida.iniciarJogo()
                partida.iniciarJogadores()
                partida.distribuirCartas()
                partida.jogar()
                print(partida.checkWinner())
                break
            else:
                print('Precisa definir um valor maior que 2 e menor que 4')
        except ValueError:
            print('Precisa definir um valor inteiro')
        except AttributeError:
            print('Tente novamente') # Ao executar muitas vezes seguidas, as vezes a IDE confunde umas referências. Em caso de erro é só repetir