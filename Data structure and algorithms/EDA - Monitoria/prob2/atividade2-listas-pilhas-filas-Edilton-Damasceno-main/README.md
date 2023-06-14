[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/kLaYap_r)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11026504&assignment_repo_type=AssignmentRepo)
# Atividade 2 - Jogo do Mico. 

## Aluno: Edilton de Jesus Damasceno
## Matrícula: 221115977

### Instruções básicas do jogo:
O jogo é dividido em duas etapas. Primeiro, um baralho já embaralhado, com 52 cartas, é criado e o Mico é definido. Em seguida, as cartas são distribuídas alternadamente entre os jogadores. Cada jogador deverá separar as cartas que possuem pares em um monte, deixando visível o último par colocado.

A segunda etapa começa quando todos os jogadores já retiraram os pares de suas mãos. Nessa etapa, o primeiro jogador pegará uma carta do segundo jogador, que não tem par, e verificará se é possível fazer um par com a carta. Se for possível, ele colocará essa carta no monte. Em seguida, o segundo jogador pegará uma carta do terceiro jogador, e assim por diante, até que reste apenas um jogador com carta na mão. Se essa carta fizer par com o *Mico*, o jogador que a possui será considerado o perdedor.

#### Legenda.
*Mico = carta aleatoria tirada do baralho no inicio do Jogo.*

*Par = Duas cartas que começem com a mesma letra ou número.*

*Sentido: J1 pega de J2, J2 pega de J3, J3 pega de J4 e J4 pega de J1. e começa o ciclo novamente.*

*Fim do Jogo: O jogo termina quando apenas um jogador possui carta e está carta é o Mico.*


### Analise da complexidade dos principais métodos utilizados:

- ### _criaBaralho():

A complexidade da função _criaBaralho() é O(1), ou seja, é uma função de tempo constante. A função sempre cria um baralho com 52 cartas, independentemente do tamanho da entrada, o número de iterações dentro dos laços for é fixo e não depende de nenhum parâmetro de entrada.

- ### distribuiCartas():

A complexidade da função distribuiCartas() é O(n), onde "n" é o número de jogadores. Dentro da função, há um laço que itera até que a pilha de cartas esteja vazia. Portanto, o número máximo de iterações desse laço é igual ao número total de cartas no baralho, que é constante (52). Em cada iteração desse laço, ocorre um segundo laço que itera sobre os jogadores para distribuir as cartas alternadamente. Esse segundo laço é executado um número máximo de vezes igual ao número de jogadores (n). Portanto, a complexidade total da função é determinada pelo número de jogadores (n), resultando em uma complexidade de O(n).

- ### separaPar():

A complexidade da função separaPar() depende do número máximo de cartas que podem estar na mão do jogador. Analisando a complexidade de cada parte da função:

O laço while percorre a lista de cartas uma vez, até o final. No pior caso, o jogador possui o número máximo de cartas, então o número de iterações desse laço é proporcional ao número máximo de cartas (máximo possível).

Dentro do laço while, a operação de remoção de um nó (carta) da lista é executada. Essa operação tem uma complexidade de O(1), pois envolve a atualização de referências do nó anterior e posterior.

Além disso, há outras operações de incremento e decremento de variáveis, mas essas operações têm uma complexidade de O(1).

Portanto, a complexidade total da função separaPar() é determinada pelo número máximo de cartas que podem estar na mão do jogador. Se considerarmos que o número máximo de cartas é m, então a complexidade é O(m).

resumindo, a complexidade da função separaPar() é O(m), onde m é o número máximo de cartas que podem estar na mão do jogador.

- ### pegaCarta():

A complexidade da função pegaCarta() depende do número de jogadores (n) e do número máximo de cartas que um jogador pode ter (m). Analizando a complexidade de cada parte da função:

O primeiro laço while possui um número máximo de iterações igual ao número de jogadores (n). Portanto, a complexidade dessa parte é O(n).

Dentro desse primeiro laço, há um segundo laço for que itera sobre o número de jogadores (n). Portanto, a complexidade desse segundo laço é O(n).

Dentro do segundo laço, há operações que dependem do número máximo de cartas que um jogador pode ter (m). O método insereNoFim() possui complexidade O(1), mas o método removeCartaEscolhida() pode ter uma complexidade de até O(m) no pior caso, pois é necessário percorrer a lista de cartas até o índice escolhido. Além disso, o método separaPar() também pode ter uma complexidade de até O(m) no pior caso, pois precisa percorrer a lista de cartas para encontrar pares. Portanto, a complexidade dessas operações dentro do segundo laço é O(m).

No pior caso, todas as operações dentro do segundo laço são executadas n vezes. Portanto, a complexidade total da função pegaCarta() é O(n * m),  onde n é o número de jogadores e m é o número máximo de cartas que um jogador pode ter.

## Justificativa para o uso das estruturas de dados escolhidas.

### ***Escolha da Pilha:*** 
Uma pilha é uma estrutura de dados adequada para representar um baralho porque ela segue o conceito de LIFO (Last-In-First-Out), ou seja, a última carta que é inserida na pilha é a primeira a ser retirada. Quando simulamos um baralho, essa propriedade é importante, pois ao embaralhar as cartas, elas são empilhadas uma sobre a outra e, ao distribuí-las, as cartas são retiradas do topo da pilha, imitando um baralho real. Além disso, a pilha oferece eficiência em relação à inserção e remoção de elementos, pois ambas as operações são realizadas em tempo constante O(1), independentemente do tamanho da pilha. Isso torna a manipulação do baralho mais rápida e eficiente.

### ***Escolha da LSE:***
Uma lista simplesmente encadeada é uma estrutura de dados adequada para representar as cartas do jogador porque ela permite inserção e remoção eficientes de elementos em qualquer posição da lista, o que é essencial para lidar com as operações de manipulação das cartas durante o jogo.

A lista simplesmente encadeada oferece uma implementação flexível para lidar com essas operações, uma vez que os nós podem ser facilmente ligados e desligados para inserção e remoção de elementos. Além disso, a lista permite percorrer os elementos sequencialmente, o que é útil para exibir as cartas na mão do jogador.

Em termos de complexidade, a inserção e remoção em uma lista simplesmente encadeada têm um custo de tempo O(1) quando realizadas no início ou no fim da lista, e um custo de tempo O(n) quando realizadas no meio da lista, onde n é o número de elementos na lista. Portanto, a estrutura de lista simplesmente encadeada é eficiente para manipular as cartas do jogador ao longo do jogo.