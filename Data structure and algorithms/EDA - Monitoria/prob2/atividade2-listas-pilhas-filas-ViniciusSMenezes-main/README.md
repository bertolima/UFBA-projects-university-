**UFBA - UNIVERSIDADE FEDERAL DA BAHIA**

**CURSO DE ENGENHARIA DE CONTROLE E AUTOMAÇÃO**

**MATA40 - ESTRUTUDA DE DADOS E ALGORÍTIMOS** 

**Data: 06/06/2023 - SEMESTRE 2023.1**
> Aluno: Vinícius dos Santos Menezes - Mat.: 201510931


# <br>Relatório Técnico: Atividade 2 -  Simulando um Jogo de Baralho<br><br>

# Atividade 2 - Simulando um Jogo de Baralho

## Objetivos da Atividade:

O objetivo principal da atividade é aplicar os conceitos de **Tipos Abstratos de Dados (TAD) Lineares**, ou seja, **Listas Encadeadas**, **Pilhas** e **Filas** [1] apresentados em sala de aula, no contexto de um problema real e prático.

Os alunos deverão analisar o problema proposto, e definir qual o melhor TAD a ser utilizado na resolução do problema. Mais de um TAD pode ser necessário para que se possa atingir a solução do problema. 

Escolhidos os TADs, sua implementação deverá ser integrada ao problema e uma solução computacional codificada em linguagem Python. Lembrando que os recursos da linguagem Python podem ser utilizados, desde que não entrem em conflito com o gerenciamento dos seus TADs. 

## Justificativa para o uso das estruturas de dados escolhidas:
1. O jogo começa com a criação de um baralho para o jogo. Para tanto foi criada uma classe `cBaralho` que é uma classe de baseada em lista duplamente
encadeada. Foi pensada como uma classe universal para vários tipos de jogos de carta. 

A classe cBaralho foi criada baseada em uma lista duplamente encadeada para facilitar seu manuseio na inserção e remoção de novas cartas, na busca por uma carta especifica, seja pelo índice ou pelos atributos da da classe cCarta sem limitação se acesso e remocçao. Por isso utilizada como lista encadeada.

2. A classe cBaralho tem como instâncias objetos do tipo classe cCartas, que é uma classe baseada em classe cNó, com os atributos de `Posição`, `Naipe`, além de ponteiros para `próxima carta` e `carta anterior` afim de facilitar a manuseio dentro das classes que a utilizam.

3. A "Mão" de cartas de cada jogador é uma classe do tipo `cMao`, que também é uma classe baseada em lista duplamente encadeada e que utiliza como instância objetos da classe `cCartas`. Foi feita como uma classe à parte da classe cBaralho pois, além de não utilizar algumas funções da classe cBaralho, que não são necessárias na classe cMao (como "gerar baralho" e "embaralhar cartas", foi pensada para oferecer um modo de impressão das suas instâncias para melhorar a visualização das cartas no jogo.

4. Para o monte de cartas embaralhados ou para o monte de cartas de depósito de pares de cartas retiradas da mão de jogo de cada jogador foi utilizada uma classe `cACE` (Agrupamento de Cartas Embaralhadas - ou não embaralhadas), que é uma classe baseada em uma classe `cPilha`. Esta classe utiliza a estrutura de pilha pois, nela só é possivel retirar a ultima carta da pilha, facilitando assim, por exemplo, a visualização das ultimas cartas depositadas no monte de depósito das cartas pares de cada jogador.

Além disso, o monte de cartas embaralhas, recebidas como uma pilha após o embaralhamento das cartas na classe "cBaralho", tem como premissa só ser possível fazer a retirada da última carta (para distribuição de cartas aos jogadores, por exemplo), como acontece num jogo na vida real. Por isso uma estrutura baseada em pilha.

5. Apesar de haver um arquivo com a classe `cFila` baseada em estrutura de fila, a mesma não chegou a ser utilizada neste jogo.


## O Problema:

Os principais métodos utilizados na produção deste jogo se baseiam na `busca`, `remoção`, `inserção` `impressão de cartas`. Além das operações de `Push` e `Pop` na `cACE` baseada em uma estrutura de pilha.

Apesar das operações de `inserção` e `remoção` serem críticas para evitar erros no manuseio das listas e pilhas, certamente as operações de `busca` necessitam maiores atenção quanto ao custo da eficiência do algorítimo (onde as operações de inserção e remoção prévias são críticas para o sucesso da busca, inclusive).

As classes `cMao` e `cBaralho` utilizam crítério de busca linear, partindo do `self.__início__` da lista (atributo destas listas que apontam para o primeiro elmento da lista), e percorrendo toda a lista até chagar no último elemento da lista (onde o atributo `próximo elemento` tem valor `None`).

Uma operação específica que o jogo necessita é a `remover_par`, que serve para buscar e remover cartas pares do jogo, conforme as regras do mesmo.

Nesta operação há um caso especial a se considerar: No início do jogo, onde as cartas são distribuídas e os jogadores recebem sua "Mão de jogo", é necessário realizar a busca de cartas pares e efetuar a remoção destas, empilhando em um monte (estrutura de pilha) do tipo `cACE`. Nesta operação, a busca parte do primeiro elemento, utilizando-o como pivot, e percorre toda a lista procurando cartas pares. Depois o elemento pivot passa a ser o próximo nó (carta) e o processo se repete até que se chegue no penúltimo elemento da lista, quando este é comparado ao último elemento.
Esta operação, como acontece de maneira iterativa tem uma complexidade de custo na ordem `O(n²)` de comparações.

Em outro momento do jogo, onde a carta escolhida na "Mão" do outro jogador é comparada à mão do jogador que faz a escolha, esta mesma operação é utilizada. Mas como foi definida uma opearção para inserir esta carta retirada na mão do outro jogador como primeiro elemento da lista "cMao" do jogador que neste momento atua, este mesmo algorítimo, como só precisa comparar a primeira carta com as outras, ao invés de buscá-la desntro da "Mao" do jogador, este mesmo algorítimo acaba tendo uma custo na ordem de `O(n)` comparações pois, assim ,só precisa percorrer a lista uma vêz para comparação.


## Referencias Bibliográficas:

[1] Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012.

[2]	Wikipedia. **Jogos de Cartas**. disponível em: https://pt.wikipedia.org/wiki/Jogos_de_cartas

[3]	WikiHow. **Como jogar mico em 12 passos**. disponível em: https://pt.wikihow.com/Jogar-Mico

[4] 	Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 

[5] 	**Markdown Guide**. Disponível em: https://www.markdownguide.org/basic-syntax/

[6]	**Boas Práticas de Programação**. Disponível em: https://liag.ft.unicamp.br/programacao2/boas-praticas-de-programacao/
