#  Simulador Jogo de Baralho
O simulador foi implementado em Python e possui uma estrutura organizada em classes, cada uma com sua responsabilidade específica.

## Estruturas de Dados Utilizadas


**Carta**
A classe Carta representa uma carta do jogo, contendo informações sobre seu naipe e valor. Ela é utilizada para criar as cartas do baralho, armazenar as cartas nas mãos dos jogadores e exibir informações sobre as cartas durante o jogo.

**Baralho**
A classe Baralho representa o baralho do jogo, que é um conjunto de cartas ordenadas por naipe e valor. A estrutura utilizada para armazenar as cartas é uma lista. O baralho é gerado no início do jogo de forma algorítmica, garantindo a ordem correta das cartas. O método gerar_baralho utiliza dois loops aninhados para criar todas as combinações possíveis de naipes e valores. A função random.shuffle() é usada para embaralhar o baralho aleatoriamente. O método comprar_carta remove a carta do topo do baralho.

**Mao**
A classe Mao representa a mão de um jogador, que contém as cartas que ele possui. As cartas são armazenadas em uma lista. A estrutura permite adicionar, remover e verificar cartas na mão. O método tem_par percorre a lista de cartas para verificar se há um par de cartas com o mesmo valor. O método adicionar_par adiciona um par de cartas à lista de pares.

**Jogador**
A classe Jogador representa um jogador do jogo. Cada jogador possui um nome e uma mão de cartas. A estrutura utilizada para armazenar a mão é um objeto da classe Mao. O método jogar permite que o jogador escolha uma carta aleatória da sua mão para jogar e verifica se algum outro jogador possui a mesma carta em sua mão.

**Jogo**
A classe Jogo representa o jogo de Mico. Ela controla as interações entre os jogadores e a distribuição de cartas. O jogo possui um baralho e uma lista de jogadores. O método distribuir_cartas distribui as cartas do baralho entre os jogadores de forma alternada. O método jogar_rodada permite que cada jogador jogue uma carta e verifique se algum outro jogador possui a mesma carta em sua mão. O método jogar_jogo controla o fluxo do jogo até que não haja mais cartas na mão de nenhum jogador. O método imprimir_estado_jogo exibe as cartas e os pares de cada jogador.
 
# Complexidade dos Principais Métodos

A seguir, apresento uma breve análise da complexidade dos principais métodos utilizados no simulador:

**gerar_baralho():** A complexidade desse método é `O(n)`, onde n é o número total de cartas no baralho. Ele utiliza dois loops aninhados para criar todas as combinações possíveis de naipes e valores, resultando em `n` iterações.

**comprar_carta():** A complexidade desse método é `O(1)`, pois envolve apenas a remoção da carta do topo do baralho.

**tem_par()**: A complexidade desse método é `O(n^2)`, onde n é o número de cartas na mão do jogador. Ele utiliza dois loops aninhados para comparar todas as combinações de cartas e verificar se há um par com o mesmo valor.

**adicionar_par()**: A complexidade desse método é `O(1)`, pois envolve apenas a adição de um par de cartas à lista de pares do jogador.

**jogar()**: A complexidade desse método é `O(1)`, pois envolve apenas a escolha aleatória de uma carta da mão do jogador e a verificação em outros jogadores.

**distribuir_cartas()**: A complexidade desse método é `O(n)`, onde n é o número total de cartas no baralho. Ele distribui as cartas de forma alternada entre os jogadores, com uma iteração para cada carta.

**jogar_rodada()**: A complexidade desse método é `O(m)`, onde m é o número de jogadores. Cada jogador joga uma carta, resultando em m iterações.

**jogar_jogo()**: A complexidade desse método depende do número total de cartas no baralho e do número de jogadores. Em média, a complexidade é `O(n + m)`, onde n é o número total de cartas e m é o número de jogadores.

**imprimir_estado_jogo()**: A complexidade desse método é `O(m * k)`, onde m é o número de jogadores e k é o número de cartas na mão de cada jogador. Ele percorre todas as cartas e pares de cada jogador.

## Executando o Simulador
Para executar o simulador, basta executar o arquivo `main.py` dentro do diretório `code`. Todos os arquivos Python devem estar no mesmo diretório para que as importações funcionem corretamente. Durante a execução, o jogo será simulado e o estado atual do jogo será exibido na tela.
