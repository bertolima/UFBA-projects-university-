# Criando o baralho
naipes = ['Paus', 'Copas', 'Espadas', 'Ouros']
valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

baralho = 2 * [valor + ' de ' + naipe for naipe in naipes for valor in valores]

# Embaralhando
import random

def embaralhar_lista(lista):
    tamanho = len(lista)
    for i in range(tamanho - 1, 0, -1):
        j = random.randint(0, i)
        lista[i], lista[j] = lista[j], lista[i]

lista = baralho
embaralhar_lista(lista)

# Escolhendo o MICO
def remover_item_aleatorio(lista):
    indice_aleatorio = random.randint(0, len(lista) - 1)
    item_aleatorio = lista[indice_aleatorio]
    nova_lista = lista[:indice_aleatorio] + lista[indice_aleatorio + 1:]
    return item_aleatorio, nova_lista

item, nova_lista = remover_item_aleatorio(lista)
print("MICO:", item)
print()

# Distribuindo
jogadores = int(input("Número de jogadores: "))

def distribuir_alternadamente(lista, num_listas):
    listas = [[] for _ in range(num_listas)]
    for i, item in enumerate(lista):
        lista_atual = i % num_listas
        listas[lista_atual].append(item)
    return listas

lista_original = baralho
num_listas = jogadores
listas_distribuidas = distribuir_alternadamente(lista_original, num_listas)

# Identificando os pares
for i, lista in enumerate(listas_distribuidas):
    print(f"Jogador {i + 1}: {lista}")
    print('')

    contador = {}
    pares = []

    for item in lista:
        if item in contador:
            contador[item] += 1
        else:
            contador[item] = 1

    for item, ocorrencias in contador.items():
        if ocorrencias > 1:
            pares.append(item)

    if pares:
        print("Pares encontrados:", pares)
        print('')
      
        # Remover os pares da lista do jogador
        lista_sem_pares = [item for item in lista if item not in pares]
        listas_distribuidas[i] = lista_sem_pares
        print("Lista sem os pares:", lista_sem_pares)
        print('')
      
    else:
        print("Nenhum par encontrado")
    print('')

# Rodadas

num_jogadores = jogadores

continuar_jogando = input("Continuar Jogando? (s/n): ")

while continuar_jogando not in 'n':
    for jogador1 in range(num_jogadores):
        jogador2 = (jogador1 + 1) % num_jogadores

        item_jogador2 = listas_distribuidas[jogador2].pop(0)
        listas_distribuidas[jogador1].append(item_jogador2)

        print(f"Jogador {jogador1 + 1} pegou {item_jogador2} do Jogador {jogador2 + 1}")
        print()
    continuar_jogando = input("Continuar Jogando? (s/n): ")
      
    # Identificando os pares após a rodada
    for i, lista in enumerate(listas_distribuidas):
        print(f"Jogador {i + 1}: {lista}")
        print()

        contador = {}
        pares = []

        for item in lista:
            if item in contador:
                contador[item] += 1
            else:
                contador[item] = 1

        for item, ocorrencias in contador.items():
            if ocorrencias > 1:
                pares.append(item)

        if pares:
            print("Pares:", pares)
        else:
            print("Nenhum par encontrado")
        print()
      
      # Remover os pares da lista do jogador
        lista_sem_pares = [item for item in lista if item not in pares]
        listas_distribuidas[i] = lista_sem_pares
        print("Lista sem os pares:", lista_sem_pares)
        print('')
      
    else:
        print("Nenhum par encontrado")
    print('')
