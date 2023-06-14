# Atividade 2 - Listas, Pilhas e Filas - "Simulando um Jogo de Baralho"

## Elaborado por Iúna Calasans

### Criação das Classes

Faz-se necessário implementar as classes para o baralho, o Agrupamento de Cartas Embaralhadas (ACE), a mão de cada jogador e o monte de cartas.

#### Classe "Baralho":

A classe Baralho possui um construtor que inicializa o baralho com todas as cartas, representadas como duplas contendo o naipe e o valor da carta. O método embaralhar utiliza a função shuffle do módulo random para embaralhar as cartas do baralho. O método retirar_carta retira a primeira carta do baralho, se houver, e retorna essa carta. O método quantidade_cartas retorna a quantidade de cartas restantes no baralho.

##### Estrutura da Classe "Baralho":

A estrutura de dados Baralho foi escolhida para representar o conjunto de cartas do jogo. Essa estrutura permite armazenar as cartas de forma ordenada por naipe e valor, facilitando a realização de operações como embaralhar o baralho e distribuir as cartas aos jogadores. Além disso, o Baralho permite a inclusão de novas cartas, caso seja necessário expandir o jogo. Para a classe baralho foi usada lista ordenada de cartas.

##### Complexidade na Classe "Baralho":

Embaralhar: O(n), onde n é o número de cartas no baralho. O método percorre todas as cartas do baralho e realiza operações de troca para embaralhar as cartas de forma aleatória.

#### Classe "ACE":

A classe ACE possui um construtor que recebe o objeto Baralho e inicializa o ACE vazio. O método gerar_ace retira as cartas do baralho e adiciona ao ACE até que o baralho esteja vazio. O método retirar_mico retira uma carta aleatória do ACE para ser o mico. O método quantidade_cartas retorna a quantidade de cartas restantes no ACE.

##### Estrutura da Classe "ACE":

O ACE foi escolhido como uma estrutura auxiliar para a distribuição das cartas aos jogadores. Ele armazena as cartas em ordem aleatória, simulando o embaralhamento do baralho. Essa estrutura permite que as cartas sejam retiradas em sequência para a distribuição, mantendo a ordem aleatória. O ACE também é responsável por retirar o mico do conjunto de cartas embaralhadas. Foi usada lista de cartas embaralhadas.

##### Complexidade na Classe "ACE":

Preencher: O(n), onde n é o número de cartas no baralho. O método preenche o ACE com as cartas do baralho, na ordem em que foram retiradas.
Retirar Mico: O(1). O método retira o mico do ACE, removendo-o da lista de cartas embaralhadas.

#### Classe "MaoJogador":

A classe MaoJogador representa a mão de um jogador e possui métodos para adicionar e remover cartas, verificar a quantidade de cartas na mão e obter uma carta pelo índice.

##### Estrutura da Classe "MaoJogador":

A estrutura de dados MaoJogador representa a mão de cada jogador, armazenando as cartas que estão em posse do jogador durante o jogo. Essa estrutura é essencial para que o jogador possa visualizar suas cartas, escolher uma carta para jogar e verificar se possui um par. A MaoJogador também permite adicionar e remover cartas de forma eficiente. Foi utilizada uma lista para as cartas na mão do jogador.

##### Complexidade na Classe "MaoJogador":

Adicionar Carta: O(1). O método adiciona uma carta à mão do jogador, realizando uma operação de inserção no final da lista.
Remover Carta: O(n), onde n é o número de cartas na mão do jogador. O método remove uma carta da mão do jogador, percorrendo a lista de cartas e realizando a remoção da carta desejada.

#### Classe "MonteCartas":

A classe MonteCartas representa o monte de cartas em frente a cada jogador, onde apenas o último par de cartas adicionado fica visível aos outros jogadores. A classe possui métodos para adicionar um par de cartas ao monte, verificar a quantidade de cartas no monte, obter o último par de cartas adicionado e obter a carta mais recente adicionada ao monte.

##### Estrutura da Classe "MonteCartas":

O MonteCartas é utilizado para armazenar os pares de cartas formados pelos jogadores. Essa estrutura é atualizada sempre que um jogador forma um par de cartas durante o jogo. Ela permite armazenar os pares de forma ordenada e possibilita a visualização do último par adicionado, que é o único visível para os outros jogadores. Foi utilizada lista para os pares de cartas formados pelo jogador.

##### Complexidade na Classe "MonteCartas":

Adicionar Par: O(1). O método adiciona um par de cartas ao monte de cartas do jogador, realizando uma operação de inserção no final da lista.

### Complexidade no Simulador do Jogo Mico

Distribuir Cartas: O(n), onde n é o número de jogadores. O método distribui as cartas entre os jogadores, percorrendo o ACE e realizando a adição de cartas nas mãos dos jogadores em ordem alternada.
Realizar Jogada: O(1). O método realiza uma jogada de um jogador, que envolve escolher um jogador alvo, jogar uma carta, verificar se formou um par e atualizar o estado do jogo.
Escolher Jogador Alvo: O(n), onde n é o número de jogadores. O método escolhe o jogador alvo para uma jogada, percorrendo a lista de jogadores e retornando o primeiro jogador disponível.
Verificar Fim do Jogo: O(n), onde n é o número de jogadores. O método verifica se o jogo chegou ao fim, percorrendo a lista de jogadores e verificando se algum jogador possui apenas uma carta na mão.
Exibir Estado do Jogo: O(n), onde n é o número de jogadores. O método exibe o estado atual do jogo, percorrendo a lista de jogadores e exibindo suas mãos e montes de cartas.