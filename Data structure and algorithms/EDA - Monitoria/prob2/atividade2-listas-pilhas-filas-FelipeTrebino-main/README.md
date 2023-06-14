# Atividade 2- Simulando um Jogo de Baralho

Aluno: Felipe S. Trebino

## Objetivo:

O objetivo desta atividade é desenvolver uma simulação do jogo de cartas conhecido como *mico* através da aplicação dos conceitos de **Tipos Abstratos de Dados (TAD) Lineares**.

## Descrição do jogo:

O *mico*, é um jogo casual de baralho, jogado normalmente entre 2 à 4 pessoas. A partir de um baralho completo embaralhado, é retirado uma carta, o par da carta *mico*, o restante das 51 cartas são distribuidas igualmente entre os jogadores.

O objetivo do jogo é formar pares com os números das cartas da mão, sendo um total de 2 pares para cada número **- 1**, resultado da retirada da carta, de forma que o jogador que sobrar com uma carta na mão, o *mico*, perde.

No início do jogo, todos os jogadores retiram os pares da mão e colocam num monte a frente, deixando visível o ultimo par formado.

O jogo funciona em turnos em forma de ciclo, o jogador que iniciar vai retirar uma carta aleatóriamente da carta da mão de outro jogador, o próximo a jogar, repete o processo com jogador seguinte, assim, até alguém perder.

## Estruturas de dados escolhidas

A partir da análise do funcionamento do jogo podemos observar algumas classes de objetos:
- `Baralho` 
- `Carta`
- `Jogador`
- `Mão do jogador`
- `Fila de jogadores`

Analisando a lógica de funcionamento de cada classe, podemos atribuir uma certa estrutura de dados para algumas delas:

1. Baralho: O baralho basicamente é um arranjo de cartas em forma de pilha, a primeira carta a ser inserida no baralho é a ultima a ser retirada, além de que, pela lógica do jogo, temos acesso sempre a carta do topo do baralho a retirando. Deixando claro, que a estrutura ideal a ser implementada para o baralho é uma pilha.
2. Carta: A carta é uma unidade, sozinha armazena apenas valor e naipe, porém, dentro de algumas estruturas informações como a próxima carta são importantes de serem armazenadas. Por isso, para a carta, foi implementado uma classe comum, que só armazena naipe e valor, e outra classe filha de carta chamada de cartaNo, que armazena a informação da próxima carta.
3. Jogador: O jogador, como a carta, sozinho apenas armazena as cartas, que estão na sua mão, e o seu nome. Porém, o jogador pode fazer partes de estruturas de dados como uma fila, que torna necessário armazenar a informação do próximo jogador. Por isso, como em carta, foi implementado a classe jogador, que armazena sua mão e o nome, e uma classe filha jogadorNo que armazena a informação do próximo jogador.
4. Mão do jogador: Para armazenar as cartas do jogador é necessário implementar uma estrutura que facilite operações como a identificação de pares. Uma opção seria o vetor, porém, como é sábido, o vetor que possui espaço de armazenamento em memória limitado, e a mão de um jogador não possui um limite de cartas a serem armazenadas, por isto, foi optado por utilizar uma lista encadeada, cada carta que é inserida na mão do jogador é armazenada como um nó, com a carta anterior apontando para ela.
5. Fila de jogadores: O jogo funciona através de turnos, com um jogador jogando por vez num formato ciclico, ou seja, é necessário uma estrutura de dados que induz uma ordem e é ciclica, ou seja, uma fila circular, onde o último elemento da fila é ligado ao primeiro. Basicamente a ordem de jogares pode ser implementada através de uma simples rotação de ponteiros.

**Extra**: Além destas estruturas foi implementado um vetor como uma estrutura auxiliadora. Não condiz com a lógica da estrutura de dados de pilha realizar algumas operações como o embaralhamento. Para isto foi utilizado um vetor que recebe todas as cartas desempilhadas da pilha, realiza o embaralhamento através da mudança das posições das cartas, e depois empilha de volta em uma nova pilha formando o ACE.

## Detalhamento da complexidade dos principais métodos:
Segue uma análise dos principais algorirmos utilizados nos métodos das classes utilizadas na simulação:

### **generateDeck** (Algoritmo que gera as cartas 56 cartas do baralho):
Este método se encontra na classe cBaralho.
# 
    def generateDeck(self):
        for i in range(4):
            match(i):
                case 0:
                    naipe = 'Copas'
                case 1:
                    naipe = 'Ouros'
                case 2:
                    naipe = 'Espadas'
                case _:
                    naipe = 'Paus'

            for j in range(1,14):
                match j:
                    case 1:
                        valor = 'Ás'
                    case 11:
                        valor = 'Valete'
                    case 12:
                        valor = 'Dama'
                    case 13:
                        valor = 'Rei'
                    case _:
                        valor = j
                self.push(cCarta(valor, naipe))
        return

A complexidade deste algoritmo é `O(1)`, ou seja, constante. Isso ocorre porque o algoritmo tem um número fixo de iterações.

O loop externo é executado 4 vezes, pois a variável i varia de 0 a 3. Dentro desse loop externo, há outro loop que é executado 13 vezes, pois a variável j varia de 1 a 13.

### **shuffle** (Algoritmo que embaralha as cartas): 
Este método se encontra na classe cBaralho e utiliza a classe cVetor como auxiliadora.

1. Método da classe cBaralho:
#
    def shuffle(self):
        vetor = cVetor(len(self))
        for i in range(len(self)):
           vetor.insert(self.pop())
        vetor.shuffle()
        for i in range(len(vetor)):
            self.push(vetor[i])
        return

2. Método da classe cVetor:
#
    def shuffle(self):
        random.seed(int(datetime.now().strftime('%H%M%S')))
        for i in range(len(self) - 1, 0, -1):
            j = random.randint(0, i)
            self[i], self[j] = self[j], self[i]

Primeiramente, sobre o *shuffle* da classe baralho, ele percorre duas vezes o tamanho do baralho, ou seja, O(2n), onde n é a quantidade de cartas, já o método *shuffle* do vetor chamado dentro do algoritmo possui complexidade O(n), pois ele percorre o vetor uma vez. Como na de complexidade assintótica, constantes multiplicativas são ignoradas, a complexidade total do algoritmo é `O(n)`.  

### **removePares** (Algoritmo que busca pares na mão do jogador e os remove)
Este método se encontra na classe cMao
#
    def removePares(self):
            remove = False
            if len(self) == 0:
                return None, None
            noCompara = self.__inicio
            while noCompara is not None:
                if not self.busca(noCompara)[0]:
                    noCompara = noCompara.getProx()
                    continue
                noCorrente = noCompara.getProx()
                while noCorrente is not None:
                    if noCompara.compareValue(noCorrente):
                        self.removeCarta(noCompara)
                        self.removeCarta(noCorrente)
                        self.getPilhaCartas().push(noCompara)
                        self.getPilhaCartas().push(noCorrente)
                        remove = True
                        break
                    else:
                        noCorrente = noCorrente.getProx()
                noCompara = noCompara.getProx()
            return remove

Para analisar este algoritmo precisamos analisar primeiramente a complexidade dos algoritmos presentes nos método *busca()* e *removeCarta()*, e, nesses métodos a lista encadeada é percorrida no máximo uma vez, em busca de uma carta compatível, ou seja, possuem a complexidade `O(n)`, onde n é quantidade de cartas na mão.

Já no algoritmo do *removePares* em si, há dois loops aninhados. O loop externo itera sobre todos os nós da lista e o loop interno itera sobre os nós subsequentes ao nó atual. Como ambos os loops percorrem todos os nós da lista, a complexidade total do método removePares é `O(n^2)`, onde n é a quantidade de cartas na mão. 



## Utilização do programa de testes.

Para utilizar o programa de teste, basta executar o arquivo python, podendo passar três parâmetros opcionais.

➡️ **`nJogadores`** número de jogadores

➡️ **`nomesGenericos`** Utilização de nomes genéricos

➡️ **`intervalo`** Intervalo entre turnos em segundos

    py code/main.py nJogadores nomesGenericos intervalo

O parâmetro `nJogadores` deve ser passado como inteiro e aceita valores entre 2 e 4. seu valor padrão é 4.

O parâmetro `nomesGenericos` deve ser passado como 's' (**sim**) ou 'n' (**não**), caso não, o programa perguntará o nome de cada jogador. Seu valor padrão é 'n'.

O parâmentro `intervalo` deve ser passado como inteiro em segundos e determina o intervalo da simulação entre o turno de cada jogador. Seu valor padrão é 2.

O programa irá simular um jogo de *mico*, mostrará inicialmente a mão dos jogadores, fruto da distribuição de cartas do ACE, já no primeiro turno, todos so jogadores irão retirar os pares de suas respectivas mãos e após isto, se inica o jogo, em turnos, cada jogador irá escolher uma carta de outro jogador e, após isso, verificar se algum par foi formado. O último par formado pelo jogador sempre irá estar disponível para visualização. Caso o jogador não tenha mais cartas, ele é pulado na sequencia da fila. O ultimo jogador que sobrar perde, e carta par do mico é revelada.

## Referencias:

[1] 	Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 
