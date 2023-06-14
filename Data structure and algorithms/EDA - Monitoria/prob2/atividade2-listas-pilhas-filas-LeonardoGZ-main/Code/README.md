# Jogo de Mico

Este é um programa Python que implementa o jogo de cartas chamado Mico. O jogo de Mico é um jogo de cartas popular, onde o objetivo é se livrar de todas as cartas da mão e evitar ser o último jogador com cartas. O jogo é jogado com um baralho padrão de 52 cartas.

## Funcionalidades do programa

O programa possui as seguintes funcionalidades:

- Permite que o usuário informe o número de jogadores (de 2 a 4) e seus nomes.
- Cria um baralho com todas as cartas necessárias para o jogo.
- Embaralha o baralho de forma aleatória.
- Distribui as cartas para os jogadores, de forma equilibrada.
- Inicia o jogo, onde os jogadores vão jogando suas cartas e tentando se livrar delas.
- Verifica se algum jogador possui um par de cartas e move essas cartas para o monte do jogador. (O par é formado por cartas de mesmo valor e cor)
- Em cada rodada, os jogadores trocam uma carta aleatória entre si.
- O jogo continua até que apenas um jogador fique com cartas na mão, sendo declarado como o perdedor.


## Arquivos do programa

O programa é dividido em três arquivos:

- `main.py`: Contém a função principal `main()`, que é responsável por interagir com o usuário, criar os jogadores e iniciar o jogo.
- `MICO.py`: Contém as classes `Carta`, `Jogador` e `JogoMico`, que representam as entidades do jogo e implementam suas respectivas funcionalidades.
- `TADs.py`: Contém as classes `No`, `ListaEncadeada`, `Pilha` e `Fila`, que são estruturas de dados utilizadas no programa para manipular as cartas, as mãos dos jogadores e o baralho.

## Como executar o programa

1. Certifique-se de ter o Python instalado em seu sistema.
2. Baixe todos os arquivos do programa em um diretório local.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos estão localizados.
4. Execute o comando `python main.py` para iniciar o programa.
5. Siga as instruções fornecidas pelo programa para jogar o jogo de Mico.

### Divirta-se jogando o Mico! ###

**Observação:** Certifique-se de ter todos os arquivos mencionados (`main.py`, `MICO.py` e `TADs.py`) no mesmo diretório para que o programa funcione corretamente.

### TADs 

1. TAD No: A classe No é utilizada para representar um nó em uma estrutura de dados encadeada. Ela contém um atributo para armazenar o valor do nó e um atributo para apontar para o próximo nó na sequência. Essa estrutura é utilizada nas implementações das TADs ListaEncadeada, Pilha e Fila.

2. TAD ListaEncadeada: A classe ListaEncadeada representa uma lista encadeada, onde cada elemento é armazenado em um nó encadeado. Ela contém métodos para inserção, remoção, busca e outras operações em uma lista encadeada. No contexto do jogo de Mico, a ListaEncadeada é utilizada para representar o baralho e as mãos dos jogadores.

3. TAD Pilha: A classe Pilha representa uma pilha, onde os elementos são inseridos e removidos seguindo a política Last-In-First-Out (LIFO). A classe Pilha é implementada utilizando a estrutura de dados ListaEncadeada, com as operações de inserção e remoção realizadas no topo da pilha. No jogo de Mico, a Pilha é utilizada para representar a pilha de cartas descartadas.

4. TAD Fila: A classe Fila representa uma fila, onde os elementos são inseridos no final e removidos do início, seguindo a política First-In-First-Out (FIFO). Assim como a Pilha, a Fila também é implementada utilizando a estrutura de dados ListaEncadeada, com as operações de inserção realizadas no final da fila e as operações de remoção realizadas no início. No jogo de Mico, a Fila é utilizada para representar a fila de cartas a serem distribuídas aos jogadores.

### Complexidade 

1. Criar Jogadores:

- Complexidade: O(n)
- Justificativa: A função cria uma lista de jogadores com base no número fornecido. A complexidade é linear em relação ao número de jogadores, pois a função percorre um loop para criar cada jogador.

2. Iniciar Jogo:

- Complexidade: O(N * M)
- Justificativa: A função inicia o jogo, realizando várias etapas:
    Criar Baralho: O(N * M), onde N é o número de naipes (4) e M é o número de valores (13).
    Embaralhar Baralho: O(K), onde K é o tamanho do baralho.
    Distribuir Cartas: O(N * M), onde N é o número de jogadores e M é o número médio de cartas distribuídas para cada jogador.
    Pares Início: O(N * M), onde N é o número de jogadores e M é o número médio de cartas na mão de cada jogador.
    Jogar Rodada: O(N * M), onde N é o número de jogadores e M é o número médio de cartas na mão de cada jogador.

3. Distribuir Cartas:

- Complexidade: O(N * M)
- Justificativa: A função distribui as cartas do baralho para os jogadores. Ela percorre cada jogador e insere as cartas na mão de cada jogador. A complexidade é proporcional ao número de jogadores e ao número médio de cartas distribuídas para cada jogador.

4. Pares Início:

- Complexidade: O(N * M^2)
- Justificativa: A função verifica se há pares na mão de cada jogador. Para cada jogador, ela percorre todas as cartas na mão (O(M)) e verifica se há algum par (O(M)). A complexidade total é proporcional ao número de jogadores e ao número médio de cartas na mão de cada jogador.

5. Jogar Rodada:

- Complexidade: O(N * M)
- Justificativa: A função simula uma rodada do jogo. Para cada jogador, ela realiza uma jogada, que envolve a remoção de uma carta da mão de um jogador e a adição dessa carta na mão do próximo jogador. A complexidade total é proporcional ao número de jogadores e ao número médio de cartas na mão de cada jogador.

6. Verificação de Condição de Vitória:

- Complexidade: O(N * M)
- Justificativa: A função verifica se algum jogador possui todas as cartas do mesmo valor na mão. Ela percorre cada jogador e verifica se há pares de cartas com o mesmo valor e mesma cor. A complexidade é proporcional ao número de jogadores e ao número médio de cartas na mão de cada jogador.

7. TADs (Lista Encadeada, Pilha, Fila):

- Inserção de elemento: O(1)
- Remoção de elemento: O(1)
- Acesso a elemento: O(n), onde n é o tamanho da estrutura de dados
- Justificativa: As operações básicas de inserção, remoção e acesso aos elementos das TADs utilizadas no código têm complexidade constante ou linear em relação ao tamanho da estrutura de dados.