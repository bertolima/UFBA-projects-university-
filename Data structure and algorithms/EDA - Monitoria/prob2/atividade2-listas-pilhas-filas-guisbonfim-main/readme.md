# **Aqui um breve resumo das TADs utilizadas nesse trabalho:**


## Class Carta: 

Essa CLASS funciona para separar as cartas em *peso* e o *naipe*, ela cria objetos de cartas que vem do *Baralho*;
Ela será direcionada aos *jogadores*.

## Class Baralho: 

Essa classe é utilizada para simular o baralho do jogo, em seguida temos as representações das cartas do *baralho*;
A escolha da *lista* como estrutura de dados se deve à sua capacidade de armazenar elementos ordenados e permitir operações como **adicionar**, **remover** e **embaralhar**;

### Class Jogador: 

Nessa classe, são atribuídos os *jogadores* e o *baralho* que terá em mãos;
Foi feito listas para cartas nas *mãos dos jogadores* e no *monte*, pois foi analisado que era mais **simples** de percorrer todos os **dados**;

### Class Jogo:

A classe *Jogo* é responsável por gerenciar as regras do jogo. Ela utiliza o objeto Baralho para criar o *baralho*, distribuir as cartas e verificar pares. Além disso, utiliza a classe *Jogador* para representar os jogadores do jogo. As estruturas de dados utilizadas (**lista de jogadores**, **lista de cartas na mão** e **lista de pares no monte**) permitem armazenar e manipular as informações necessárias para o funcionamento do jogo.

# **Agora analisando a complexidade de cada método:**

## Baralho.embaralhar(): 

O método embaralhar utiliza a função *random.shuffle()*, que possui uma **complexidade de tempo O(n)**;

## Baralho.retirar_carta(): 

O método *pop()* possui uma **complexidade de tempo O(1)**.


## Jogador.mostrar_mao():

A complexidade desse método é **linear** em relação ao número de cartas na mão do jogador.

## Jogador.mostrar_ultima_carta_do_monte(): 

O método *mostrar_ultima_carta_do_monte* tem complexidade desse método é **constante**, já que apenas acessa o último elemento da *lista do monte*.

## Jogo.verificar_mao(): 

A complexidade desse método depende do número de cartas na mão do jogador e é **quadraticamente proporcional** ao número de cartas. No pior caso, em que não há pares, a **complexidade seria O(n^2)**, onde *n* é o número de cartas na mão.
