#include <vector>

template <class T>
void Merge(T &arr, int  start, int  mid, int end){
    auto n1 = mid - start + 1;
    auto n2 = end - mid;

    int* leftArray= new int[n1];     
    int* rightArray= new int[n2];

    for (int i=0;i<n1;i++){
        leftArray[i] = arr[start + i];
    }
    for (int j=0;j<n2;j++){
        rightArray[j] = arr[mid + j + 1];
    }

    int i = 0, j = 0;
    

     for (int k = start;k<=end;k++){
        if (i >= n1){
            arr[k] = rightArray[j];
            j++;
        }
        else if(j >= n2){
            arr[k] = leftArray[i];
            i++;
        }
        else if (leftArray[i] < rightArray[j]){
            arr[k] = leftArray[i];
            i++;
        }
        else{
            arr[k] = rightArray[j];
            j++;
        }
     }
     delete rightArray;
     rightArray = nullptr;
     delete leftArray;
     leftArray = nullptr;
}

template <class T>
void MergeSort(T &arr, int const start, int const end){
    if (start < end){
        int mid = (start + end) / 2;
        MergeSort(arr, start, mid);
        MergeSort(arr, mid+1, end);
        Merge(arr, start, mid, end);
    }
}