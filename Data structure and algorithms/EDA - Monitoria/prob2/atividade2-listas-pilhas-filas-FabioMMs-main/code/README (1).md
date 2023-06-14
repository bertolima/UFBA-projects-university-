
# Atividade 2 - Simulando um Jogo de Baralho (Pilhas, Listas e Filas)
**Aluno:** Fábio Miguel Mascarenhas dos Santos
**Matrícula:** 222118639
**Professor:** Antônio Lopes Apolinário Junior
**Data:** 04/06/2023

---

## Objetivos
O objetivo geral desta atividade foi aplicar na prática os todos os conceitos aprendidos de **Tipos Abstratos de Dados (TAD) Lineares** , ou simplesmente, **Pilhas, Filas e Listas Encadeadas**. Também, esta tarefa servirá como 2º critério de avaliação da disciplina Estrutura de Dados (MATA40) da Universidade Federal da Bahia (UFBA).
Os objetivos específicos deste trabalho estão ligados a interpretação, codificação, em linguagem ***Python***, e testes do problema prosposto: Simular um jogo de Baralho, chamado **Mico**. Dessa forma, estes objetivos são:
1. **Justificar** as escolhas dos TAD's e **Analisar** brevemente a complexidade das operações; 
2. **Gerar** o baralho de cartas (*ACE*);
3. **Distribuir** as cartas para jogadores adequadamente; 
4. **Formar** e **Armazenar** os pares de cartas;
5. **Simular** jogadas essenciais; e,
6. **Simular** um jogo completo.
---

## Atividade
A atividade, como foi tratada brevemente no tópico acima, consistiu na construção de um jogo de cartas, chamado de Mico, utilizando como ferramenta a linguagem de programação *Python* e nossos conhecimentos sobre algumas estruturas de dados, em especial a Filas, Pilhas e Listas Encadeadas; também conhecidos como TAD's Lineares.
Para execução da tarefa, foi importante criar classes, são elas:
- **'Carta':** Criada para armazenar os valores individuais de uma carta de baralho, como seu Naipe e seu Valor;
- **'Jogador':** Criada para armazenar os valores individuais de um jogador deste jogo, como seu Nome e sua Mão de Cartas;
- **'Baralho':** Criada para gerar, armazenar, embaralhar e distribuir todas as cartas de um baralho, com exceção dos coringas (portanto, 52 cartas no total), que foram excluídas deste jogo;
- **'PilhaCartas':** Criada para receber os pares de cartas da mão dos jogadores;
- **'ListaJogadores':** Criada para organizar a posição dos jogadores na mesa e sua ordem de jogada; e,
- **'MaoJogador':** Criada para organizar a mão de cartas de um jogador. 


### Escolha das Estruturas
Para a realização desta atividade, foram utilizadas 6 classes baseadas em 4 tipos de estruturas:
- As classes **'Carta'** e **'Jogador'** foram baseados na classe **'cNó'**, ou seja, elas podem ser definidas como nós de uma lista encadeada. Esta característica foi escolhida para ambas as classes devido ao fato da necessidade de organizá-los em uma sequência linear sem saber, porém, da quantidade total de elementos que irão ser organizados. Desta forma, sempre que um novo elemento fora do planejamento surgir, ele poderá ser criado e posteriormente anexado a estrutura de lista sem grandes problemas;
- As classes **'Baralho'** e **'PilhaCartas'** foram baseados na classe **'cPilha'**, ou seja, elas podem ser definidas como Pilhas. Esta escolha de Pilha para ambas as classes se deve a importancia de seguir a característica *Last In First Out (LIFO)* presente no *ACE*, sempre é retirado o objeto do topo para distribuir, e no monte, que deve mostrar no topo o último par de cartas adicionado à ele;
- A classe **'ListaJogadores'** foi baseados na classe **'cLSEC'**, ou seja, ela pode ser definida como uma Lista Simplesmente Encadeada Circular. Esta estrutura foi escolhida para manter a sequência do jogo em uma única direção, em círculos (depois da vez do último jogador é novamente a vez do primeiro) até sobrar apenas um jogador, que então é definido como perdedor do jogo;
- As classe **'MaoJogadores'**  foi baseados na classe **'cLSE'**, ou seja, ela pode ser definida como uma Lista Simplesmente Encadeada. Esta estrutura foi escolhida com intuíto de organizar linearmente as cartas de um jogador em detrimento de uma estrutura como Vetor, pois não se sabe quantas cartas exatamente cada jogador irá receber até o momento da definição do número de jogadores. Dessa forma, se garante que mesmo com um número variado de jogadores, cada um deles irá receber adequadamente sua quantidade de cartas sem a necessidade de se alocar um espaço muito grande de memória, sem finalidade, a fim de tentar cobrir todas as possibilidades de distribuições.


### Análise de Complexidade
A maioria dos algoritmos utilizados nas classes baseadas em **TAD's de Listas Encadeadas** estão na ordem de n, ou seja, são ***O(n)***, pois eles dependem de percorer a lista elemento a elemento para localização e execução da instrução. Em instruções de busca e inserção, o desempenho pode ser um pouco melhor devido a escolha de organizá-los na lista ordenadamente.
Já os algoritmos utilizados nas classes baseadas em **TAD'S de Pilhas** estão na ordem de 1, ou seja, são ***O(1)***, porque cada instrução será apenas para o elemento do topo da pilha. No pior das hipóteses, cada instrução ***O(1)*** será executada n vezes, onde n é o tamanho da pilha; assim, o desempenho se tornaria semelhante ao caso médio das listas encadeadas.
Por fim, as classes baseadas em **TAD's de Nós** estão na ordem de ***O(1)***, por causa da existência de apenas algoritmos de coleta e atribuição de dados.

---
## Análise do Trabalho
A compreensão das regras do jogo e da formatação básica do trabalho, exemplificando: quais classes criar e que tipos de estrutura de dados são melhores para determinadas tarefas, não foram tarefas tão difíceis, mas também não foram tão fáceis de serem executadas. Entretanto, na parte da codificação já obtive algumas dificuldades, principalmente nas partes de simular o jogo Mico, a qual não obtive muito êxito.
No geral, o trabalho, em minha opinião, teve uma dificuldade moderada com bastante desafios interessantes a serem superados que com certeza agregaram bastante ao meu aprendizado como programador. 