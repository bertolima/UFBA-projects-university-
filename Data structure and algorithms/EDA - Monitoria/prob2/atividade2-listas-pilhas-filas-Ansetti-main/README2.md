# Estrutura de dados escolhida

## Lista encadeada
  
  - No simulador de jogos de cartas Mico, listas encadeadas são usadas para representar os baralhos de cartas de cada jogador 
  (baralhos de mão e pares). Aqui estão alguns motivos do porquê escolher listas encadeadas neste caso:
  
    ### Alocação Dinâmica 
    -  As listas encadeadas são cruciais em jogos de cartas devido à sua capacidade de alocar o tamanho dinamicamente. Isso permite que o número de cartas na mão de um jogador e os pares possam ser alterados ao longo do jogo,
     oferecendo flexibilidade para adicionar e remover cartas sem a necessidade de redimensionamento ou realocação. Em resumo, as listas encadeadas permitem ajustes contínuos no tamanho da estrutura de dados, tornando-as ideais para manipulação eficiente de cartas em um jogo.

    ### Eficiência na inserção e remoção 
    - As listas encadeadas têm operações eficientes de inserção e remoção no início e no final da lista.
    No jogo Mico, os jogadores pegam cartas de outros jogadores ou do baralho, e adicionam cartas aos seus pares quando encontram um par correspondente. As listas encadeadas permitem a inserção e a remoção eficientes de cartões nesses cenários.

    ### Fácil transição 
    - As listas encadeadas fornecem uma travessia fácil de um nó para outro, permitindo-nos iterar sobre as cartas na mão de um jogador ou no baralho de pares.
    Isso é importante para exibir o estado do jogo e verificar se há pares.
    
    ### Sem capacidade fixa 
    - As listas encadeadas não têm uma capacidade fixa, ao contrário das arrays ou listas com um tamanho predefinido.
    No jogo Mico, o número de jogadores e o número de cartas na mão de cada jogador podem variar. O uso de listas encadeadas permite um número flexível de jogadores e cartas sem impor quaisquer restrições.

    ### Sobrecarga mínima de memória 
    - As listas encadeadas têm uma pequena sobrecarga de memória por elemento em comparação com outras estruturas de dados, como arrays.
    No jogo Mico, onde o número de cartas pode ser grande, a implementação com de listas encadeadas ajuda a otimizar o uso da memória.
    
    ## Sobre alguns métodos
      - O método add_carta() adiciona uma nova carta ao fim da lista encadeada.
      - O método Embaralhar() embaralha as cartas no baralho convertendo-as em uma lista, embaralhando a lista usando o random.shuffle e, em seguida, recriando o baralho a partir da lista embaralhada.
      - Distribuir() dá as cartas para os jogadores um a um, alternando entre os jogadores.
      - O método jogada() lida com um único turno para o jogador atual, simulando o jogador pegando uma carta de outro jogador ou do baralho
      - O verifica_par() verifica se o jogador formou algum par após cada jogada.
      - O método is_game_over() verifica se todos os jogadores não tem nenhuma carta nas mãos.
      - O get_prox_jogador() determina o próximo jogador da rodada.
      - display_game_state() Exibe o estado atual do jogo, mostrando a mão e os pares de cada jogador.
      - display_cartas() ajuda na exibição das cartas em um determinado baralho.
      - O método vencedor()  determina o vencedor ,baseado no número de pares na mão de cada jogador.
      - O conta_par  conta o número de pares no baralho de pares de um jogador.

   
## Conclusão
      
    - Embora as listas encadeadas tenham essas vantagens em termos de flexibilidade e eficiência para o simulador de jogo Mico,
      é importante ressaltar que a escolha da estrutura de dados depende dos requisitos específicos do jogo ou aplicação e das compensações entre diferentes estruturas de dados. 
      Outras estruturas de dados, como matrizes ou dicionários, também podem ser consideradas com base em diferentes fatores, como uso de memória, operações de pesquisa ou dinâmicas de jogo específicas.
    - É importante analisar os requisitos do jogo e escolher as estruturas de dados apropriadas de acordo. A escolha das listas encadeadas, neste caso, baseia-se na necessidade de 
      tamanho dinâmico, inserção/remoção eficiente, fácil transição entre nos e flexibilidade no número de jogadores e cartas.
