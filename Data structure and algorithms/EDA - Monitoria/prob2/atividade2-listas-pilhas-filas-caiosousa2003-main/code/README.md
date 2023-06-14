# Atividade 2 - Simulando um Jogo de Baralho

## Justificativas

1 - Deck Ordenado - Foi escolhido a estrutura vetor para implementar tal elemento devido a quantidade de itens que esse possue e não haver necessidade de remoção dos itens. Além disso, para repassar as cartas para o ACE há um custo baixo já que é possível acessar diretamente o espaço em que o item está alocado, sem ter que percorrer a lista.

2 - ACE e Monte de Descarte - Foi escolhida a estrutura pilha para implementar tal elemento devido o formato que os dois requerem que a primeira carta a entrar seja a última a sair, o que é caracteristico da pilha.

3 - Ordem de jogadores - Foi utilizada a estrutura fila para implementar devido a característica de o primeiro jogador ser o primeiro a jogar e assim seguindo a ordem, podendo fazer algo ciclíco, onde o primeiro a entrar joga, e depois vai para o final da fila. Como a fila possui essas características, foi notória sua implementação.

4 - Mão - Foi utilizada a lista duplamente encadeada para implementação da mão do jogador já que ela possui como vantagem a fácil remoção das cartas, sendo de complexidade O(1). Como as mãos dos jogadores possuem menos cartas, é vantajoso a utilização da lista, menos que seja necessário percorrer todo o vetor para encontrar uma carta. Para compesar esse procura, a lista implementada possui inserção ordenada que faz com que reduza os custos e a complexidade.

5 - Carta e Jogador - Os dois foram implementados como nós, já que são peças fundamentais do jogo e estão inseridos dentro de outras estruturas já citadas anteriormente.

## Análise de Complexidade

1 - Criação do Baralho - O(1)

2 - Embaralhamento do Baralho - O(n)

3 - Criação do ACE - O(n)

4 - Verificação e Remoção dos Pares Iniciais - O(n)

5 - Escolha da carta a ser pegada - O(n), sendo aleatório

6 - Busca por um par - O(n)

7 - Remoção dos pares e remoção da carta escolhida - O(1)


## Instruções

Para utilizar o código, basta rodar e inserir a quantidade de jogadores que você deseja simular. Após isso, tudo será simulado com um delay entre 1 e 2 segundos. O terminal indica quando o código chega ao fim.
