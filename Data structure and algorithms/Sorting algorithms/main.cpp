#include "include/QuickSort.h"
#include <iostream>
#include <ctime>

int main(){
    srand(static_cast<unsigned>(time(NULL)));

    int arr[11] = {30, 5, 10, 3, 4, 90, 150, 2, 67, 30, 7};
    int size = sizeof(arr)/sizeof(int);

    for (int i=0;i<size;i++){
        std::cout << arr[i] << " ";
    }
    std::cout << "\n";

    tailQuickSort(arr, 0, size-1);

    for (int i=0;i<size;i++){
        std::cout << arr[i] << " ";
    }

    return 0;
}

