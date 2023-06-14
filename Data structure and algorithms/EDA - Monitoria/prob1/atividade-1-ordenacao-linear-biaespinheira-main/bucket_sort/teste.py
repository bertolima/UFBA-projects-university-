import random
from time import time
from datetime import datetime
from bucket_sort import cVetor

# Garante a geração aleátoria dos números
random.seed(datetime.now().timestamp()) 


n=int(input("\nDigite a quantidade de elementos do vetor que deseja ordenar:\n"))

i,f=map(float,input("\nDigite o início e o fim do intervalo separados por espaço (Exemplo: '-9 3' para o intervalo [-9,3])\n").split())

#Cria um objeto do tipo cVetor
vetor=cVetor(n)

# Gera valores aleatórios no intervalo que vai de 'i' até 'f'
for j in range (n):
    vetor.insere(random.uniform(i,f)) # Armazena os valores no vetor 

# Guarda o vetor gerado para realização da análise
vetor_analise=vetor

print("\nVetor gerado aleatoriamente:", vetor,"\n")

start_time = time( ) # Armazena o tempo inicial
vet,num_comp = vetor.bucket_sort_reais() # Realiza a ordenação por meio do bucket_sort_reais
end_time = time ( ) # Armazena o tempo final
time_bucket= end_time-start_time # Caucula o tempo de execução

print("Vetor ordenado pelo bucket sort:",vet)

print(f"\n---------------- Bucket sort ----------------")
print("Complexidade caso médio: O(n)")
print(f"Número de comparações:",num_comp)
print(f"Tempo de execução:", time_bucket)



def analisys(vetor_analise, time_bucket, num_comp):

    vetor_analise2 = vetor_analise # Armazena o vetor 

    # Comparação com o Insertion Sort

    start=time() # Guarda o tempo inicial
    comp_insertion = vetor_analise.insertionSort()
    end=time() # Guarda o tempo final
    time_insertion = end-start # Calcula o tempo de execução

    print(f"\n--------------- Insertion sort --------------")
    print("Complexidade caso médio: O(n²)")
    print(f"Número de comparações:",comp_insertion)
    print(f"Tempo de execução:", time_insertion)

    dif_comp=0     # Inicializa a diferença de comparações com 0
    dif_tempo=0 # Inicializa a diferença do tempo de execução com 0

    # Calcula as diferenças (em porcentagem) se os denominadores forem !=0
    if time_insertion!=0:
        dif_tempo = 100 - round((time_bucket*100/time_insertion),2)
    if comp_insertion!=0:
        dif_comp = 100 - round((num_comp*100/comp_insertion),2)


    # Comparação Selection Sort 

    start=time() # Guarda o tempo inicial
    comp_selection=vetor_analise2.selection_sort()
    end=time() # Guarda o tempo final
    time_selection = end-start # Calcula o tempo de execução

    print(f"\n--------------- Selection sort --------------")
    print("Complexidade caso médio: O(n²)")
    print(f"Número de comparações:", comp_selection)
    print(f"Tempo de execução:", time_selection)

    dif_comp2=0 # Inicializa a diferença de comparações com 0
    dif_tempo2=0 # Inicializa a diferença do tempo de execução com 0

    # Calcula as diferenças (em porcentagem) se os denominadores forem !=0
    if time_selection!=0:
        dif_tempo2 = 100 - round((time_bucket*100/time_selection),2)
    if comp_selection!=0:
        dif_comp2 = 100 - round((num_comp*100/comp_selection),2)
        
    print("\n----------------- Relatório -----------------")
    print(f"\nO bucket sort em comparação a um insertion sort: ")
    print(f"  - Realiza aproximadamente {dif_comp}% menos comparações")
    print(f"  - É executado aproximadamente {dif_tempo}% mais rápido ")

    print(f"\nO bucket sort em comparação a um selection sort: ")
    print(f"  - Realiza aproximadamente {dif_comp2}% menos comparações")
    print(f"  - É executado aproximadamente {dif_tempo2}% mais rápido\n")


option=int(input("\nDeseja gerar um relatório comparando o algoritmo escolhido com outros? (Digite '1' para sim e '0' para não)\n"))
if option==1:
    # Retorna o relatório
    analisys(vetor_analise, time_bucket, num_comp)