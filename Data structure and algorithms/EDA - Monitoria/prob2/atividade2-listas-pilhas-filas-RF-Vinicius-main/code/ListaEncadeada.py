from No import No
class LEncadeada:

    def __init__(self):
        self.__inicio = None
        self.__numElems = 0

    @property
    def inicio(self):
        return self.__inicio
    @inicio.setter
    def inicio(self, value):
        self.__inicio = value
        
    @property
    def numElems(self):
        return self.__inicio
    @numElems.setter
    def numElems(self, value):
        self.__numElems = value

    
    def __str__(self):

        outStr = ""

        if self.__inicio == None:        
            outStr += "### VAZIO ###"
        else:
            # aqui voce deve implementar a saida de todos os nós da lista
            node_atual = self.inicio
            outStr += f'{node_atual.dado}'
            while node_atual.prox:
                outStr += f", {node_atual.prox.dado}"
                node_atual = node_atual.prox
                

        return outStr
    
    def size(self):
        return self.__numElems
    
    def insereNo(self, n):
        new_node = No(n)
        
        if self.inicio is None: # Se for o promiro no, inicia a lista com o valor
            self.inicio = new_node
            self.__numElems += 1
        else:
            node_atual = self.inicio
            while node_atual.prox:
                node_atual = node_atual.prox
            node_atual.prox = new_node
            self.__numElems += 1
        
    def buscaDado(self, n): #Busca o dado por um valor.
        if self.inicio == n:
            return hex(id(self.inicio))
        else:
            node_atual = self.inicio.prox
            while True:
                if node_atual.dado == n:
                    return hex(id(node_atual))
                elif node_atual.prox is None:
                    return "Elemento não encontrado"
                else:
                    node_atual = node_atual.prox
                
    def buscaPorIndex(self, index, tipoDado=True): #Busca o valor por indice e retorna o valor encontrado.
        countPosicao = 0
        node_atual = self.__inicio
        while True:
            if countPosicao == index:
                #return node_atual.getDado()
                return node_atual.getDado() if tipoDado else node_atual #Por padrão o tipo retornado é o dado da lista, caso passe False no tipo, retorna o No
            elif node_atual.getProx() is None:
                return False # Caso o valor não seja encontrado, retorna False
            node_atual = node_atual.prox # Atualiza o novo valor, com o próximo do ponteiro
            countPosicao += 1
                
            
    def removeNo(self, n): # Remove o no com base em um valor
        
        if self.inicio.dado == n:
            self.inicio = self.inicio.prox
            self.__numElems -= 1
            return True
        else:
            node_atual = self.__inicio.prox
            node_anterior = self.__inicio
            while True:
                if node_atual.dado == n:
                    node_anterior.prox = node_atual.prox
                    self.__numElems -= 1
                    return True
                elif node_atual.prox is None:
                    return False
                else:
                    node_anterior = node_atual
                    node_atual = node_atual.prox
              
                    
    def removePorindex(self, index):
        countPosicao = 0
        node_atual = self.__inicio
        while True:
            
            if index == 0: # Se o index == 0, já retorna o valor removido, sendo ele o primeiro
                removido = self.__inicio.dado
                self.__inicio = self.__inicio.prox # Define como valor incial o próximo valor que o ponteiro estava indicando
                self.__numElems -= 1 # Reduz 1un no número de elementos
                return removido
            elif countPosicao == index: #Se a contagem for igual o index, remove o valor e define ponteiro do dado anteiror por o próximo
                removido = node_atual.dado
                node_anterior.prox = node_atual.prox
                self.__numElems -= 1
                return removido
            elif node_atual.getProx() is None: # Caso não encontre nas condições anteriores, e o dado sendo o último, entende-se que não existe o valor.
                return False 
            node_anterior = node_atual
            node_atual = node_atual.prox
            countPosicao += 1
            