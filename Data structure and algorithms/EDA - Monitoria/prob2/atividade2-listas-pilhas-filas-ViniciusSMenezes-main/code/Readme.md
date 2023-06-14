Atividade 2 - Simulando um Jogo de Baralho
Objetivos da Atividade:
O objetivo principal da atividade é aplicar os conceitos de Tipos Abstratos de Dados (TAD) Lineares, ou seja, Listas Encadeadas, Pilhas e Filas [1] apresentados em sala de aula, no contexto de um problema real e prático.

Os alunos deverão analisar o problema proposto, e definir qual o melhor TAD a ser utilizado na resolução do problema. Mais de um TAD pode ser necessário para que se possa atingir a solução do problema.

Escolhidos os TADs, sua implementação deverá ser integrada ao problema e uma solução computacional codificada em linguagem Python. Lembrando que os recursos da linguagem Python podem ser utilizados, desde que não entrem em conflito com o gerenciamento dos seus TADs.

Motivação:
Jogos eletrônicos costumam demandar por estruturas de dados eficientes e robustas em várias de suas etapas. Mesmo jogos simples podem requerer estruturas de dados apropriadas para que o roteiro do jogo possa ser implementado de forma eficiente.

Jogos tradicionais ainda são bastante comuns como passatempos. Nessa categoria, os jogos baseados em baralhos de cartas apresentam uma vasta gama de opções [2]. Um dos mais simples e divertido é o Mico [3]. Nesse jogo o objetivo é formar pares de cartas, a partir das cartas na mão do jogador. No inicio do jogo, uma carta é retirada do baralho (o mico). Dessa forma, um par deixará de ser formado. O "perdedor" é aquele jogador que ficar com a carta "par" do "mico".

O jogo é jogado com 1 baralho de cartas completo. Após ser embaralhado, uma carta é retirada e as demais distribuidas entre os jogadores. Na primeira etapa os jogadores avaliam suas mãos e retiram os pares de cartas iguais, separando-as em um monte a sua frente. Com o restante das cartas que não possuem par, cada jogador na sua vez retira uma carta aleatóriamente da mão de outro jogador (mantendo uma regra de ciclagem, horária ou anti-horária). Caso a nova carta faça um par com alguma carta de sua mão, o jogador coloca o par no monte de cartas a sua frente. Esse passo é realizado até que reste apenas uma carta na mão de um jogador: o mico. Esse jogador é o perdedor.

O Problema:
Uma empresa de desenvolvimento de jogos quer contratar um novo membro para a sua equipe de desenvolvimento de jogos infantis educativos. Sabendo que os alunos da disciplina de Estrutura de Dados na UFBA são muito bons, decidiu fazer a primeira etapa de sua seleção durante a disciplina propondo um desafio simples mas instigante: desenvolver um simulador de jogo de Mico para crianças, para ser jogado em sua plataforma on-line de jogos educativos.

Como o desafio é parte do processo seletivo, o interesse é avaliar o conhecimento dos concorrentes para projetar e desenvolver o núcleo jogo, ou seja, os TADs que darão suporte às suas regras básicas. Para demonstrar que seus TADs funcionam de forma adequada, solicitaram que você produza um simulador de uma partida do jogo.

Nesse simulador as cartas são distribuídas aleatoriamente entre de 2 a 4 jogadores virtuais. O simulador organiza de forma randômica os jogadores e indica um deles para iniciar a partida. Na sequencia todos os jogadores jogam uma vez, e o processo recomeça até que todas as cartas acabem. O controle das rodadas é feito pelo simulador.

O simulador deve permitir que as jogadas sejam acompanhadas na tela. Deve ser possível ver as cartas de cada jogador, e a carta de cima do monte de cada jogador.

As seguintes regras devem ser seguidas:

O baralho, um conjunto de cartas ordenado por naipe e por valor, deve ser gerado no início do jogo. Sua criação deve envolver um processo algoritmico e não uma inicialização por enumeração;
Um Agrupamento de Cartas Embaralhadas (ACE) deve ser definido no início de cada partida. O ACE deve ser gerado pelo sorteio aleatório de cartas do baralho;
O mico deve ser retirado do ACE, por sorteio, antes da distribuição para os jogadores ;
Tal como em um jogo real, a ordem das cartas do ACE deve mantida na distribuição das cartas aos jogadores;
A distribuição das cartas entre os jogadores deve ser feita a partir da retirada de cartas do ACE e de forma alternada, ou seja, primeira retirada para o primeiro jogador, segunda para o segundo, terceira para o primeiro, quarta para o segundo, quinta para o primeiro, e assim sucessivamente, para o caso de apenas 2 jogadores;
O processo de retirada de uma carta da mão do outro jogador deve ser feita simulando a escolha da posição da carta pelo jogador da vez;
As cartas de cada jogador devem ser armazenadas de tal forma que a busca por um par em uma jogada seja a mais rápida possível;
O monte de cartas do jogador permite que apenas o ultimo par inserido fique visível aos outros jogadores.
Os Requisitos de implementação:
Seu simulador deverá ser codificado na linguagem Python [4], utilizando os conceitos de Classes, Objetos e modularização.

Seu repositório deve conter um arquivo README com a documentação da solução adotada, que deve conter:

Justificativa para o uso das estruturas de dados escolhidas;
Uma breve analise da complexidade dos principais métodos utilizados;
Instruções de como utilizar o programa, caso necessário.
A submissão do código do seu projeto será feita exclusivamente pelo repositório individual disponibilizado no GitHub Classroom.

Procure fazer commits e pushs regularmente, de modo a que seja possível acompanhar a evolução do seu código.

Não serão aceitas submissões no Google Classroom, por e-mail ou qualquer outro meio eletrônico de envio.