import random
import carta
import pilha


def gerarBaralho():
    naipes = ["Paus", "Ouros", "Copas", "Espadas"]
    posicoes = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Rainha", "Rei"]
    tamanho = 52
    baralho = pilha.cPilha(tamanho)

    contador = 0
    for naipe in naipes:
        for posicao in posicoes:
            baralho.push(carta.Carta(naipe, posicao))
            contador += 1

    return baralho


def embaralhar(baralho):
    cartas = []
    while not baralho.empty():
        carta = baralho.pop()
        cartas.append(carta)
    random.shuffle(cartas)
    for i in range(len(cartas) - 1):
        baralho.push(cartas[i])
    mico = cartas[-1]
    return mico

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':
    
    baralho = gerarBaralho()
    mico = embaralhar(baralho)
    
    while not baralho.empty():
        cartaTopo = baralho.pop()
        print(cartaTopo)
        
        
    print("mico: ", mico)