# Esse módulo será utilizado para definir como será jogado o jogo MICO;

#Aqui utilizamos as funcionalidades já explicadas anteriormente nos outros módulos;

# ***********************************************************************************************************************
# *---------------------------------------------------------------------------------------------------------------------*
# ***********************************************************************************************************************

from objetos import Baralho
# ***********************************************************************************************************************
class Jogo:

# ***********************************************************************************************************************

    def __init__(self, jogadores): #Aqui foi feito um constructor que inicia a cada vez que um objeto da class é criado, no caso quando novos jogadores são adicionados ao jogo;
        self.baralho = Baralho() #Aqui foi feita uma instanciação da class Baralho e um novo baralho aleatório é criado a cada novo jogador adicionado;
        self.jogadores = jogadores #Cria novos jogadores e suas listas;
# ***********************************************************************************************************************
    def iniciar_partida(self): #O método 'iniciar_partida()' executa duas ações principais: embaralhar o baralho e distribuir as cartas para os jogadores;
        self.baralho.embaralhar() #Esse método embaralha as cartas que vieram do objeto baralho de forma aleatória, dessa forma, toda partida comecará de cartas diferentes;
        self.distribuir_cartas() # Esse método é responsável por distribuir as cartas do baralho para os jogadores, seguindo as regras do jogo;
# ***********************************************************************************************************************
    def distribuir_cartas(self): #Esse método foi montado basicamente para garantir que todos os jogadores terão a mesma quantidade de cartas;
        num_jogadores = len(self.jogadores) #Aqui é utiizado para contar a quantidade de jogadores presentes no jogo;
        for _ in range(num_jogadores):
            for jogador in self.jogadores: #Esse loop funciona para garantir que todos os jagadores tenham o mesmo número de cartas;
                carta = self.baralho.retirar_carta() #Aqui é retirada uma carta da pilha do baralho;
                jogador.adicionar_carta(carta) #Aqui a carta retirada da pilha do baralho é adicionada à mão do jogador;
# ***********************************************************************************************************************
    def jogar_rodada(self): #Foi pensado para exibir a cartas dos jogadores e verificar se há pares nas mãos, caso tenha, há a remoção;
        for jogador in self.jogadores:
            jogador.mostrar_mao() #Aqui basicamente funciona para exibir as cartas de cada jogar após a distruibuição do método anterior;
            jogador.mostrar_ultima_carta_do_monte()
# ***********************************************************************************************************************
            if self.verificar_mao(jogador): #Nessa parte, serve para verificar se há pares de cartas na mão do jogador;
                self.remover_par(jogador) #Caso tenha par de cartas, é chamado o método de remoção e o par de cartas desaparece;
# ***********************************************************************************************************************
    def verificar_mao(self, jogador):
        for i in range(len(jogador.mao)): 
            for j in range(i+1, len(jogador.mao)): #Aqui, cada carta é verificada se há alguma paridade;
                if jogador.mao[i].peso == jogador.mao[j].peso: #Nesse caso, se o valores em "jogador.mao[i].peso" e "jogador.mao[j].peso", caso sejam iguais, as cartas são pares;
                    jogador.adicionar_par_ao_monte(jogador.mao[i], jogador.mao[j]) #Já aqui, havendo a paridade, o par é adicionado ao monte de cartas do jogador;
                    return True #Se um par for encontrado;
        return False #Se um par não for encontrado;
# ***********************************************************************************************************************
    def remover_par(self, jogador): #Ao encontrar um par pelo método anterior, aparece essa mensagem em tela;
        print('-----------------------------------------------------------')
        print(f"Jogador {jogador.nome} encontrou um par e removeu as cartas da mão:")
        print('-----------------------------------------------------------\n')    
# ***********************************************************************************************************************
        #O método "remover_par()" encontra e remove um par de cartas da mão do jogador. 
        # Ele registra os índices das cartas que formam o par, adiciona o par ao monte do jogador e, em seguida, remove as cartas da mão pelo índice.
# ***********************************************************************************************************************  
        indices_pares = []
        for i in range(len(jogador.mao)):
            for j in range(i+1, len(jogador.mao)):
                if jogador.mao[i].peso == jogador.mao[j].peso:
                    indices_pares.extend([i, j])
                    jogador.adicionar_par_ao_monte(jogador.mao[i], jogador.mao[j])
                    break
# ***********************************************************************************************************************       
        # Remover as cartas da mão do jogador pelos índices em ordem reversa
        for indice in sorted(indices_pares, reverse=True):
            jogador.mao.pop(indice)
# ***********************************************************************************************************************
