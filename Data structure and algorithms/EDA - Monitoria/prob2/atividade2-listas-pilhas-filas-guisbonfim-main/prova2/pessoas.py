#Esse módulo será utilizado para separar os jogadores e como se comportam no jogo MICO;

#Cada jogador possui um nome, uma mão de cartas e um monte de cartas formado pelos pares que ele encontrou;

# ***********************************************************************************************************************
# *---------------------------------------------------------------------------------------------------------------------*
# ***********************************************************************************************************************

class Jogador: #Nessa classe, são atribuídos os jogadores e o baralho que terá em mãos;
    
# *********************************************************************************************************************** 
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.monte = []
# ***********************************************************************************************************************
    def adicionar_carta(self, carta): #Esse método adiciona cartas às mãos dos jogadores;
        self.mao.append(carta)
# ***********************************************************************************************************************
    def remover_carta(self, indice): #Esse método retira cartas às mãos dos jogadores de acordo com o  indice informado;
        return self.mao.pop(indice)
# ***********************************************************************************************************************
    def adicionar_par_ao_monte(self, carta1, carta2): #Aqui é adicionado uma tupla contendo as duas cartas ao final da lista self.monte, que representa o monte de cartas do jogador;
        self.monte.append((carta1, carta2))
# ***********************************************************************************************************************
    def mostrar_mao(self):
        print('-----------------------------------------------------------')
        print(f'Cartas na mão do(a) {self.nome}:')
        for carta in self.mao: #Esse loop é utilizado para percorrer todas as cartas que estão na lista indicada ('self.mao') e é exibida seu naipe e seu peso;
            print(f' => {carta.naipe}  {carta.peso}')
        print('')
# ***********************************************************************************************************************
    def mostrar_ultima_carta_do_monte(self): #Esse método verifica se o monte de cartas está vazio ou não;
        if self.monte: #Se o monte não estiver vazio, a última carta do monte é obtida desempacotando a tupla carta1, carta2 = self.monte[-1]. 
            carta1, carta2 = self.monte[-1]
            print('-----------------------------------------------------------\n')
            print(f'Último par no monte do(a) {self.nome}:')
            print(f'  {carta1.naipe} {carta1.peso}')
            print(f' => {carta2.naipe} {carta2.peso}')
            print('-----------------------------------------------------------\n')
# ***********************************************************************************************************************
        else: #Agora, se o monte estiver vazio, uma mensagem indicando que o monte está vazio é exibida.
            print('-----------------------------------------------------------')
            print(f'Monte vazio do jogador {self.nome}')
            print('-----------------------------------------------------------\n')
# ***********************************************************************************************************************
