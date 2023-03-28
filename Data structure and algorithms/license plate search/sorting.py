def countingSort(lista, n=None, r=None):
    if n is None:  # get size of list
        n = len(lista)
    if r is None:  # get value of max item on the list
        r = max(lista)+1
    ocorrencias = [0] * r  # create a auxliar list to count how numbers appears
    # create a auxiliar list to count how many times a number appears
    ocorrencias_pred = [0] * r
    aux = [0] * n  # create a auxiliar list to get the sorted elements of the list

    for i in range(n):
        # add +1 to position ocorrencias[i] when we have lista[i] = number and ocorrencias[number]
        ocorrencias[lista[i]] += 1

    ocorrencias_pred[0] = 0
    for valor in range(1, r):
        ocorrencias_pred[valor] = ocorrencias_pred[valor-1] + \
            ocorrencias[valor-1]

    for i in range(n):
        valor = lista[i]
        aux[ocorrencias_pred[valor]] = lista[i]
        ocorrencias_pred[valor] += 1

    for i in range(n):
        lista[i] = aux[i]


# lista = lista das placas, n=qtd de placas, w=qtd de digitos nas placas, r=conjunto de inteiros que os digitos das placas podem assumir em unicode.
def radixSort(lista, n=None, w=None, r=90, nComp=0):
    if n is None:  # pega a quantidade de placas na lista
        n = len(lista)
    if w is None:  # pega a qtd de digitos em cada placa
        w = len(lista[0])

    # lista auxiliar que vai armazenar os valores das placas de forma ordenada pra depois passar pra lista original
    aux = [0] * (n)
    # como vamos usar o radixSort LSD devemos comparar digito a digito de cada placa e ordenar as placas com base nisso, do digito menos significante pro mais significante.
    for digito in range(w-1, -1, -1):

        # lista auxiliar que vai guardar quantas vezes um digito aparece, essa informação vai ser guardada pelo unicode do digito e, também vai ser responsavel por armazenar a qtd de vezes que o digito é repetido e sua respectiva posição
        ocorre_total = [0] * (r+1)

        for i in range(0, n):  # vai percorer x digito de todas as placas e guarda os valores dos digitos na lista auxiliar ocorre_total
            valor = ord(lista[i][digito])
            ocorre_total[valor+1] += 1
            nComp += 1

        # o valor total de ocorrencias de um digito é igual o valor total de ocorrencias do atual mais o valor total dos anteriores.
        for valor in range(1, r):
            ocorre_total[valor] += ocorre_total[valor-1]
            nComp += 1

        for i in range(0, n):  # esse for vai pegar a ordem e a qtd de repetição dos valores unicode armazenados em ocorre_total e a partir disso vai atribuir uma posição da lista aux, em que a placa da lista original vai ser copiada pra aux de forma ordenada
            valor = ord(lista[i][digito])
            aux[ocorre_total[valor]] = lista[i]
            # é necessario somar +1 pra que o indice do proximo elemento adicionado seja diferente do atual.
            ocorre_total[valor] += 1
            nComp += 1

        for i in range(n):  # esse for serve simplesmente pra copiar os elementos ordenados em aux para a lista original
            nComp += 1
            lista[i] = aux[i]
    # retorna o numero total de iterações entre todas as listas.
    return print('O número total de iterações do algortimo de ordenação foi de:', nComp)