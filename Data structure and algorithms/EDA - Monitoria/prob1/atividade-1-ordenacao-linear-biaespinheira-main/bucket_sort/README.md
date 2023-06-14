# Bucket Sort 

O algoritmo escolhido foi o **bucket sort**. Esse algoritmo é ideal para entradas que seguem uma distribuição uniforme e possui tempo de execução de O(n) em seu caso médio. O bucketsort é considerado um algoritmo rápido, pois assume que a entrada é gerada por um processo aleatório que distribui elementos de forma uniforme e independente no intervalo [0, 1).

## Explicação e Justificativa

O algoritmo escolhido foi adaptado no presente trabalho para ordenar valores reais aleatórios em qualquer intervalo de números (incluindo negativos). As seguintes adaptações foram essenciais para alcançar esse objetivo:

1. Para normalizar os elementos no intervalo [0,1), todos os valores foram divididos por uma constante 'k' igual ao sucessor do maior elemento do vetor. 

2.  As partes negativas e positivas do vetor foram ordenadas separadamente e concatenadas no final, o que diminuiu quase pela metade o número de comparações entre vetores com distribuições parecidas de elementos positivos e negativos.

A escolha se mostrou adequada ao problema proposto, pois foi capaz de ordenar valores com significativamente menos comparações e menos tempo do que outros algoritmos de ordenação convencionais, como o selection sort e o insertion sort, principalmente para vetores com grande quantidade de elementos. Essas conclusões foram obtidas após a realização de inúmeros testes e podem ser verificadas no programa de teste "teste.py".

