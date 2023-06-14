#include <cstdlib>

template <class T>
void CountingSort(T arr[], int size, int max){
    int valor, i;
    T* ocorre_pred, *aux;
    ocorre_pred = (T*)malloc((max+1) * sizeof(T));
    aux = (T*)malloc(size * sizeof(T));

    for (valor = 0; valor <= max;valor++){
        ocorre_pred[valor] = 0;
    }

    for (i=0; i < size;i++){
        valor = arr[i];
        ocorre_pred[valor+1] += 1; 
    }

    for (valor = 1; valor <= max; valor++){
        ocorre_pred[valor] +=  ocorre_pred[valor-1];
    }

    for (i=0;i<size;i++){
        valor = arr[i];
        aux[ocorre_pred[valor]] = arr[i];
        ocorre_pred[valor]++;
    }

    for (i = 0;i<size;++i){
        arr[i] = aux[i];
    }
    free(ocorre_pred);
    free(aux);
}
