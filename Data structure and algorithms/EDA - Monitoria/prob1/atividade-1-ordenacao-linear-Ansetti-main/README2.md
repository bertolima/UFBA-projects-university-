# Escolha do Algoritmo 

 - Para fazer a escolha do algoritmo, a busca foi feita a partir  dos requisitos propostos para a atividade 1
   Dessa forma, o algoritmo de Complexidade linear escolhido foi o Radix sort
   
 ## Sobre o algoritmo
 
   A seguir, estarão expostos caracteristicas do Radix sort, dispostas em 4 critérios, são eles:
   - Complexidade
   - Uso da memória
   - Velocidade
   - Implementação

 ### Complexidade
 
  O tempo de execução do Radix Sort dependerá do número de elementos a serem ordenados e do número de dígitos usados para ordenação. Sua complexidade assintótica O(n + k), sendo n é o número de elementos e k é o número de possíveis valores de um dígito. Isso significa que o tempo de execução crescerá linearmente com o número de elementos e o número de valores possíveis de um dígito. No entanto, o número de dígitos pode ser grande e isso pode levar a um tempo de execução maior.
  
### Uso da memória

 O Radix Sort requer espaço adicional para armazenar os dados a serem ordenados e os dígitos durante a ordenação. O uso de memória dependerá da implementação do algoritmo e da quantidade de dígitos usados para ordenação. Em geral, o uso de memória é menor que outros algoritmos de ordenação, como por exemplo, o Merge Sort.
 
 
### Velocidade

 É claro que velocidade é um critério que dependerá também da maquina em que estará rodando o algoritmo. No entanto, O desempenho do Radix Sort depende do número de dígitos do maior número e do número de bits necessários para armazenar cada dígito. Em geral, o Radix Sort tem uma complexidade assintótica menor que outros algoritmos de ordenação, como o Quick Sort e o Merge Sort, quando o número de dígitos é relativamente pequeno. Em contra partida, quando o número de dígitos é grande, o tempo de execução do Radix Sort pode ser significativamente maior.
 
### Implementação
 
  O Radix sort pode ser implementado de algumas  maneiras, incluindo o uso de vetores, listas encadeadas e árvores. A implementação mais simples usa vetores e é conhecida como Radix Sort com contagem. Outra implementação comum é o Radix Sort com buckets, que usa listas encadeadas ou árvores para armazenar os elementos com o mesmo valor de dígito. A escolha da implementação depende do número de dígitos e da quantidade de memória disponível.
  
  
 ## Conclusão
 
  Esses fatores me levaram a utilizar o radix sort para o desenvolvimento da atividade, além do critério de conhecimento própio já que durante as pesquisas, o interesse por esse novo algoritmo foi aumentando, principalmente por suas características em ordenar digitos.
