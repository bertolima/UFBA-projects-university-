#include <cstdlib>
#include "Swap.h"

template <class T>
int Partition(T &arr, int start, int end){
    auto pivot = arr[end];
    int i = start;
    for (int j=start;j<end;j++){
        if (arr[j] <= pivot){
            swap(arr[j], arr[i]);
            i++;
        }
    }
    swap(arr[i], arr[end]);
    return i;
}

template <class T>
void QuickSort(T &arr, int start, int end){
    if (start < end){
        int q = Partition(arr, start, end);
        QuickSort(arr, start, q-1);
        QuickSort(arr, q+1, end);
    }
}

int random(int start, int end){
    return (start + rand() % end);
}

template <class T>
int RandomizedPartition(T &arr, int start, int end){
    auto i = random(start, end);
    swap(arr[end], arr[i]);
    return Partition(arr, start, end);
}

template <class T>
void RandomizedQuickSort(T &arr, int start, int end){
    if (start < end){
    int q = RandomizedPartition(arr, start, end);
    RandomizedQuickSort(arr, start, q-1);
    RandomizedQuickSort(arr, q+1, end);
    }
}
