#include "MergeSort.h"
#include <iostream>
#include <ctime>

int main(){
    srand(static_cast<unsigned>(time(NULL)));

    int arr[5] = {30, 5, 10, 3, 4};
    int size = sizeof(arr)/sizeof(int);

    for (int i=0;i<5;i++){
        std::cout << arr[i] << " ";
    }
    std::cout << "\n";

    MergeSort(arr, 0, size-1);

    for (int i=0;i<5;i++){
        std::cout << arr[i] << " ";
    }

    return 0;
}

