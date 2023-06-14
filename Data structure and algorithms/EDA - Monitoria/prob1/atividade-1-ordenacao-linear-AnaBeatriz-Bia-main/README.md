[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/kLaYap_r)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11030048&assignment_repo_type=AssignmentRepo)
# Atividade 1 - Algoritmo de Ordenação *Linear*

### Relatório técnico

Nessa atividade, foram implementados três algoritmos de ordenação: Heap Sort, Counting Sort e Extended Counting Sort. O Heap Sort tem complexidade O(n.log(n)) e utiliza uma estrutura de dados chamada heap para organizar os elementos durante a ordenação. O HeapSort trabalha com valores inteiros ou floats. Esse algoritmo foi utilizado para a análise comparativa do desempenho entre algoritmos lineares e não lineares O(n.log(n)). 

Já o Counting Sort é um algoritmo de ordenação em tempo linear, eficiente para ordenar uma grande quantidade de números inteiros dentro de um intervalo específico. Sua complexidade é O(n+k), tornando-o mais rápido em certas situações em comparação a outros algoritmos de ordenação.

Para tornar o Counting Sort capaz de ordenar vetores de números float, foi realizada uma modificação na implementação original. Foi necessário realizar adaptações no código, já que a implementação original só trabalhava com números inteiros. Posteriormente, para abranger valores reais, como números naturais, inteiros, racionais e irracionais, foi feita a normalização dos valores entre [0,1]. No final foi adicionada ao usuário a opção de fornecer o intervalo em que os valores se encontram e quantos valores devem ser gerados. 

O Extended Counting Sort - versão aprimorada do Counting Sort - foi mais eficiente porque abrangeu valores reais, incluindo números naturais, inteiros, racionais e irracionais, enquanto o Counting Sort trabalhava apenas com números inteiros em um intervalo específico. O Extended Counting Sort teve que converter os valores reais em inteiros, multiplicando-os por um fator e arredondando, o que aumentou a complexidade do algoritmo. Devido a essas modificações, o algoritmo Extended Counting Sort foi capaz de ordenar corretamente um vetor de números reais, mantendo a sua complexidade linear.

A metodologia utilizada na análise comparativa desses algoritmos de ordenação envolveu os seguintes passos:

1. Implementação dos algoritmos: os três algoritmos foram implementados em uma mesma linguagem de programação para garantir uma comparação justa e precisa.

2. Seleção de um conjunto de dados: um conjunto de dados adequado de valores reais foi selecionado para testar os algoritmos.

3. Medição no número de comparações: foi medido o número de comparações de cada algoritmo para o conjunto de dados selecionado. 

4. Análise da complexidade: a complexidade de cada algoritmo foi avaliada teoricamente e comparada com os resultados da medição anterior. Isso permite verificar se a complexidade teórica corresponde ao desempenho na prática.

5. Comparação de desempenho: com base nos resultados da medição e na análise da complexidade, foi possível comparar o desempenho dos algoritmos e identificar qual deles é o mais eficiente para o conjunto de dados selecionado.

6. Análise de resultados: por fim, os resultados foram analisados e interpretados para extrair conclusões relevantes sobre os algoritmos de ordenação.

A partir disso, o Extended Counting Sort foi mais eficiente que o Heap Sort e o Counting Sort, já que teve um número menor de comparações realizadas durante o processo de ordenação. Por isso, esse algoritmo foi escolhido por apresentar um desempenho melhor em relação aos outros dois algoritmos, o que o torna mais rápido para ordenar grandes conjuntos de dados, pois satisfez os requisitos propostos no problema.

### Objetivo: 
- Aprofundar o estudo dos algoritmos de ordenação e sua análise de complexidade;
- Pesquisar algoritmos de ordenação não tradicionais.

### O Problema:

Diversas aplicações utilizam algoritmos de ordenação para organizar dados que provem de amostragens do mundo real. Tais dados são  representados no domínio dos números reais. Mais recentemente, com o aumento do poder computacional das CPUs e GPUs, modelos de simulação complexos são capazes de descrever o comportamento dos fenomenos naturais com um grau de precisão satisfatório. Em muitos casos é mais barato a simulação de um fenomeno que a captura de dados reais. 

O volume de dados produzido por uma simulção complexa pode ser muito grande. Porém, em geral, os dados possuem uma característica importante: sua ditribuição é uniforme e independente dentro do intervalo `[0.0, 1.0)`[^1]. Tal distribuição pode ser alcançada por métodos como o de Monte Carlo de amostragem. 

O processamento de grandes volumes de dados torna-se mais eficientes quando os dados estão ordenados. Algoritmos de ordenação com complexidade  `O(n.log(n))` podem ser utilizados, porém nesses casos algoritmos "quase lineares" se mostram soluções mais interessantes. Algoritmos de ordenação "quase lineares" possuem complexidade `O(n + k)` onde `k << n`. O valor `k` pode estar relacionado com a composição da chave de ordenação ou com algum processo de divisão dos dados [1]. 

### A Atividade: 

1. Pesquise algoritmos de ordenação que sejam capazes de ordenar valores reais. 
2. Analise os algoritmos que voce encontrar e escolha um que satisfaça os requisitos propostos no problema. 
3. Construa um programa de teste que permita gerar um conjunto de valores reais dentro de um intervalo fixo e que produza como saída o conjunto ordenado. 
4. Seu programa deve ser parametrizado, permitindo ao usuário fornecer qual o intervalo em que os valores se encontram e quantos valores devem ser gerados. Outros parametros podem ser incluidos em função do algoritmo escolhido.
5. Ao final da ordenação, algumas estatísticas devem ser geradas, como o numero de comparações no processo de ordenação.  

### A Implementação:

A implementação deve ser desenvolvida em linguagem *Python* [2].

Utilize os conceitos de **modularização** e **TAD** utilizados nas aulas.

O código fonte gerado deve ser comentado e legível, seguindo as boas práticas de programação [4]. 

Procure fazer `commits` e `pushs` regularmente, de modo a que seja possível acompanhar a evolução do seu código (isso será pontuado!!). 

Utilize o arquivo README do seu repostório para elaborar um pequeno relatório técnico justificando a escolha do algoritmo e discutindo sua adequação ao problema e sua complexidade teórica. Use a linguagem *Markdown* [3] para formatar o seu texto de forma adequada. 

# A Avaliação

Como voce não foi o único profissional contactado, haverá uma avaliação comparativa de todas as soluções apresentadas, guiada pelos seguintes critérios:

| Critério | Pontuação |
| :--- | :---: |
| 1. Documentação (README) [3] | 0,5 |
| 2. Modularização e uso de TAD/Classe | 1,0 | 
| 3. Código comentado e seguindo boas práticas [4] | 0,5 | 
| 4. Uso adequado dos recursos do GitHub | 0,5 |
| 5. Escolha justificada do algoritmo de ordenação | 1,0 | 
| 6. Implementação correta do TAD/Classe |  |
| - Construtor | 0,5 |
| - Algoritmo de ordenação | 2,0 |
| - Operações de entrada e saida da Classe | 0,5 |
| 7. Implementação correta do programa de teste |  |
| - Parametrização da entrada | 0,5 |
| - Controle dos testes | 2,0 |
| - Geração das estatísticas | 1,0 |

## O Prazo e as Penalidades

Sua atividade deverá ser submetida até o dia 04/05 (5a. feira).  

> Será aplicada a penalização de -1,0 pto por dia de atraso (verificado via data da ultima submissão no repositório)
> 
>> **Em casos de plágio (total ou parcial) todos os envolvidos serão desclassificados ficando com zero na avaliação**. 

# Referencias Bibliográficas:

[1] 	Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012..

[2] 	Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 

[3] 	**Markdown Guide**. Disponível em: https://www.markdownguide.org/basic-syntax/

[4]		**Boas Práticas de Programação**. Disponível em: https://liag.ft.unicamp.br/programacao2/boas-praticas-de-programacao/

[^1]: Lembrando que qualquer intervalo real pode ser normalizado para o intervalo [0.0, 1.0(.
