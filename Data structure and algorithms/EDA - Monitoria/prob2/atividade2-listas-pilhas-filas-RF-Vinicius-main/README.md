###### TAD Usados ######
Para realizar a tarefa foram usados os tipos Lista encadeada e Pilha.
1. A lista encadeada:  foi usada amplamente no decorrer da aplicação. Foi usada para representar a lista de baralho, ACE, a mão do jogador, lista de jogadores e para outras regras no decorrer do código. 
A escolha do TAD lista encadeada para esses fins deu-se por conta da flexibilidade de percorrer os valores intermediários, ademais, a possibilidade de retirar elementos intermediários. As demais aplicações não permitem isso.
2. Pilha: A pilha foi usada para representar o monte de cartas do jogador. Como a pilha tem a caracteristica de ser last in - first out, se encaixa bem no funcionamento da pilha. Uma vez que, só interessava o valor que está por último no monte. Além disso, a pilha é um TAD de fácil manipulação nesse caso.

###### ANÁLISE DE COMPLEXIDADE ######
* Abaixo será feito a análise de complexidade dos principais métodos da aplicação.
1. Baralho.embaralhar()
Complexidade: O(n²)
Explicação: n sendo o tamanho do baralho, o algorítmo percorre o tamanho do baralho e procura dentro do baralho novamente o valor do índice
2. Jogador.verificarPares()
Complexidade: O(n)
Explicação: Percorre no pior dos casos toda lista na busca do valor igual a entrada. 
3. Mico.iniciarJogadores()
Complexidade: O(n)
Explicação: Com base na quantiade de jogadores, instância cada jogador.
4. Mico.distribuirCartas()
Complexidade: O(n)
Explicação: Com base na quantidade de cartas, distribui indiviualmente para cada jogador na sequência.
5. Mico.checkWinner()
Complexidade: O(n)
Explicação: Com base na lista de jogadores com 0 cartas, verifica quem tem mais ou menos cartas no monte. Ganhando quem tem mais.


###### Como jogar e os resultados ######
* Como usar
1. Rodar o arquivo main.py
2. Selecionar a quantidade de jogadores.
3. Só será aceito jogadores maior ou igual a 2

* Como é exibido na tela:
1. Primeiro é exibido o baralho ordenado
2. Depois é exibido o ACE
3. Em seguida, é exibido no console como fica o resultado de cada jogador por jogada
2. Ao fim é exibido quem é o vencedor e quem é o mico.