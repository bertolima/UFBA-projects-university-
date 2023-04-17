#include "Swap.h"

template <class T>
void MAX_HEAPIFY(T arr[], int size, int i){
    int left = i * 2 + 1, right = i * 2 + 2, largest = i;

    if(left < size && arr[left] > arr[largest])
        largest = left;
    if (right < size && arr[right] > arr[largest])
        largest = right;

    if (largest != i){
        swap(arr[i], arr[largest]);
        MAX_HEAPIFY(arr, size, largest);

    }
}
template <class T>
void BUILD_MAX_HEAP(T arr[], int size){
    for (int i = size/2-1; i >= 0; i--){
        MAX_HEAPIFY(arr, size, i);
    }
}

template <class T>
void HeapSort(T arr[], int size){
    BUILD_MAX_HEAP(arr, size);
    for (int i=size-1; i> 0 ;i--){
        swap(arr[0], arr[i]);
        MAX_HEAPIFY(arr, i, 0);
    }
}

