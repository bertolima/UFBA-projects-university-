# Atividade 2 - Simulando um Jogo de Baralho

## Introdução:

Esse repositório trata-se da resolução da atividade avaliativa 2 da disciplina *Estrutura de Dados e Algoritmos I*. Essa 
atividade propõe o desenvolvimento de um simulador do jogo de baralho mico. Para um melhor detalhamento da tarefa, 
visualizar o arquivo *ENUNCIADO.md.*

## Justificativa do uso das estruturas. Uso das estruturas e suas justificativas:

Inicialmente, o programa foi desenvolvido procurando utilizar adaptações dos **TADs** (tipos abstratos de dados) vistos 
em aula (vetores, listas, filas e pilhas) através de composição e/ou herança. Com isso, pode ser observado que o código 
de algumas classes podem apresentar padrões de implementação distintas. Classes, suas estruturas e justificativas:

-  **Carta:** classe para representação da carta;
-  **Jogador:** classe para representação do jogador, possuindo um nome para identificação, uma mão (lista de cartas - 
explicado mais a frente) e uma pilha de pares abaixados;
-  **Baralho:** uma classe que herda cPilha. Dessa forma, foi possível a utilização da classe pai e a implementação de 
métodos específicos, como o montarBaralho (iniciar o baralho com as 52 cartas) e embaralhar;
      1. Para embaralhar, foram utilizadas 2 listas auxiliares, de forma que: depois de esvaziar a pilha na primeira lista, 
  é retirado de forma aleatória cada nó da lista e passada para a segunda lista, que por sua vez, é esvaziada da mesma 
  forma de volta para a pilha, com uma alteração: a primeira carta retirada da segunda lista é separada e guardada 
  (**mico**). 
-  **Lista de cartas:** uma classe que herda cLista (lista simplemente encadeada). Classe que busca tratar os métodos 
envolvendo a manipulação das cartas nas mãos dos jogadores, utilizando assim alguns métodos específicos para inserção 
de cartas ordenadas, busca de pares de cartas iguais. 
      1. Com esse método de inserção, a forma para a busca implementada dos
  pares é voltada para uma busca sequencial ordenada, que visa parar e continuar para a próxima iteração toda vez que 
  encontrar duas cartas iguais em sequência e, em seguida, removê-las;  
-  **Lista de jogadores:** uma classe que herda cLista(lista encadeada circular). Criada com a intenção de tratar a 
ordenação de jogadas pelos usuários através da movimentação de um cursor, que é arbitrariamente postada em 
determinada posição. Com isso, é possivel continuar iterando e simulando a vez de cada jogador;


Para distribuição de cartas pelos jogadores, foi utilizada uma estrutura de repetição que, a cada iteração, retira uma 
carta do baralho e adiciona na mão do jogador da vez, até que o baralho esteja vazio.


## Resumo de complexidade dos principais métodos:

A inserção de cartas na mão do jogador é feita de forma que as cartas já se apresentem de forma ordenada. Com isso, 
é possível fazer uma busca pelos pares de cartas de forma distinta. Para esse código, foi implementado, basicamente, 
uma busca sequencial ordenada, em que é buscada uma sequência de 2 cartas iguais, seguindo assim, uma complexidade de 
***O(n)***. 


## Instruções para a utilização do programa:

Para fazer uma simulação do jogo, execute a seguinte instrução em um terminal a partir da pasta raiz desse projeto:

    python './src/main.py' 

Com a execução do programa, será indicado o que deverá ser escolhido e o que preencher. Em resumo, na ordem de 
instruções apresentadas no programa:

-  Insira a quantidade de jogadores que irão participar (2 ou 3 ou 4);
      1. (Obs.: o Mico é apresentado antes dessa etapa)
-  Insira o nome de cada jogador (um por vez);
-  Escolha entre organizar de forma aleatória a ordem dos jogadores ou manter a ordem apresentada na hora de nomeação
dos jogadores (sim - para reorganizar ou não - para manter ordenação).


Adaptações para o simulador:

- As cartas foram adaptadas para os valores númericos, de 1 a 13, seguindo a ordem das cartas reais, ou seja:

<div align="center">

| Versão original | Versão do simulador |
|:---------------:|:-------------------:|
|        A        |          1          |
|        2        |          2          | 
|        3        |          3          | 
|        4        |          4          |
|        5        |          5          |
|        6        |          6          |
|        7        |          7          |
|        8        |          8          |
|        9        |          9          |
|        J        |         10          |
|        Q        |         11          |
|        K        |         12          |
|        A        |         13          |

</div>
