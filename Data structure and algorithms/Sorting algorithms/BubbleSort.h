#pragma once

template <class T>
void BubbleSort(T* v, int size){
    for (int i=0;i<size;i++){
        for(int j=0;j<size-1;j++){
            if(v[j] > v[j+1]){
                T tmp = v[j];
                v[j] = v[j+1];
                v[j+1] = tmp;
            }
        }
    }
}