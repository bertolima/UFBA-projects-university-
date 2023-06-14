class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # Inicializa o primeiro nó da lista encadeada como vazio
        self.ultimo = None  # Inicializa o último nó da lista encadeada como vazio
        self.tamanho = 0  # Inicializa o tamanho da lista como 0

    def esta_vazia(self):
        return self.cabeca is None  # Verifica se a lista está vazia

    def inserir_no_fim(self, dado):
        novo_no = No(dado)  # Cria um novo nó com o dado fornecido

        if self.esta_vazia():
            self.cabeca = novo_no
            self.ultimo = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
            self.ultimo = novo_no

        self.tamanho += 1  # Incrementa o tamanho da lista

    def adicionar_carta(self, carta):
        self.inserir_no_fim(carta)  # Insere uma nova carta no final da lista

    def remover(self, dado):
        if self.esta_vazia():
            return  # Retorna se a lista está vazia

        if self.cabeca.dado == dado:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return

        anterior = self.cabeca
        atual = self.cabeca.proximo
        while atual:
            if atual.dado == dado:
                anterior.proximo = atual.proximo
                if atual == self.ultimo:
                    self.ultimo = anterior
                self.tamanho -= 1
                return
            anterior = atual
            atual = atual.proximo

    def _tamanho_(self):
        return self.tamanho  # Retorna o tamanho da lista

    def __repr__(self):
        if self.esta_vazia():
            return "ListaEncadeada: []"

        atual = self.cabeca
        nos = []
        while atual:
            nos += [str(atual.dado)]
            atual = atual.proximo
        return "ListaEncadeada: [" + ", ".join(nos) + "]"

    def adicionar_elemento(self, elemento):
        if isinstance(self, list):
            self[size(self):] = [elemento]  # Adiciona um elemento à lista

    def converter_em_lista(self):
        lista = []
        no_atual = self.cabeca
        while no_atual is not None:
            add(lista, no_atual.dado)
            no_atual = no_atual.proximo
        return lista  # Retorna a lista encadeada como uma lista simples


class Pilha:
    def __init__(self):
        self.itens = []  # Inicializa a lista de itens vazia
        self.tamanho = 0  # Inicializa o tamanho da pilha como 0

    def esta_vazia(self):
        return self.tamanho == 0  # Verifica se a pilha está vazia

    def empilhar(self, item):
        self.itens = [item] + self.itens  # Adiciona o item no topo da pilha
        self.tamanho += 1  # Incrementa o tamanho da pilha

    def desempilhar(self):
        if self.esta_vazia():
            return None  # Retorna None se a pilha estiver vazia
        self.tamanho -= 1  # Decrementa o tamanho da pilha
        topo = self.itens[0]  # Obtém o item do topo da pilha
        self.itens = self.itens[1:]  # Remove o item do topo
        return topo  # Retorna o item removido

    def topo(self):
        if self.esta_vazia():
            return None  # Retorna None se a pilha estiver vazia
        return self.itens[0]  # Retorna o item do topo da pilha

    def get_tamanho(self):
        return self.tamanho  # Retorna o tamanho da pilha

    def __repr__(self):
        return f"Pilha: {self.itens}"  # Retorna uma representação em string da pilha


class Fila:
    def __init__(self):
        self.itens = []  # Inicializa a lista de itens vazia
        self.tamanho = 0  # Inicializa o tamanho da fila como 0

    def esta_vazia(self):
        return self.tamanho == 0  # Verifica se a fila está vazia

    def enfileirar(self, item):
        self.itens += [item]  # Adiciona o item no final da fila
        self.tamanho += 1  # Incrementa o tamanho da fila

    def desenfileirar(self):
        if self.esta_vazia():
            return None  # Retorna None se a fila estiver vazia
        self.tamanho -= 1  # Decrementa o tamanho da fila
        primeiro = self.itens[0]  # Obtém o primeiro item da fila
        self.itens = self.itens[1:]  # Remove o primeiro item da fila
        return primeiro  # Retorna o item removido

    def get_tamanho(self):
        return self.tamanho  # Retorna o tamanho da fila

    def __repr__(self):
        return f"Fila: {self.itens}"  # Retorna uma representação em string da fila


def add(lista, valor):
    contador = 0
    for _ in lista:
        contador += 1
    lista[contador:contador] = [valor]
def size(arr):
    count = 0
    for _ in arr:
        count += 1
    return count  # Retorna o tamanho da lista
