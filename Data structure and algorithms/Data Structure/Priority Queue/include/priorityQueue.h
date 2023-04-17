#include <iostream>

template <class T>
void swap(T &v1, T &v2){
    T tmp = v1;
    v1 = v2;
    v2 = tmp;
}



template <class T>
class maxPriotiryQueue{
    private:
        T arr[100000];
        int size;
    
    public:
        maxPriotiryQueue(){
            this->size = -1;
        }
        int getParent(int i){
            return (i-1)/2;
        }
        int getLeft(int i){
            return i*2+1;
        }
        int getRight(int i){
            return i*2+2;
        }
        void shiftUp(int i){
            while (i > 0 && arr[getParent(i)] < arr[i]){
                swap(arr[getParent(i)], arr[i]);
                i = getParent(i);
            }
        }
        void max_heapify(int i){
            int max = i;
            int left = getLeft(i);

            if (left <= this->size && arr[left] > arr[max])
                max = left;

            int right = getRight(i);
            if (right <= this->size && arr[right] > arr[max])
                max = right;

            if (i != max){
                swap(arr[i], arr[max]);
                max_heapify(max);
            }
        }      
        void insert(T data){
            this->size++;
            this->arr[size] = data;
            
            shiftUp(this->size);
        }
        T extract_max(){
            T value = arr[0];

            arr[0] = arr[size];
            this->size--;

            max_heapify(0);
            return value;

        }
        T maximum(){
            return this->arr[0];
        }
        void getArray(){
            for (int i=0;i<this->size+1;i++){
                std::cout << this->arr[i] << " ";
            }
            std::cout << "\n";
        }
};


template <class T>
class minPriotiryQueue{
    private:
        T arr[100000];
        int size;
    public:
    minPriotiryQueue(){
        this->size = -1;
    }
    int getParent(int i){
        return (i-1)/2;
    }
    int getLeft(int i){
        return i*2+1;
    }
    int getRight(int i){
        return i*2+2;
    }
    void shiftUp(int i){
        while(i>0 && this->arr[getParent(i)] > arr[i]){
            swap(arr[getParent(i)], arr[i]);
            i = getParent(i);
        }
    }
    void min_heapify(int i){
        int min = i;
        int left = getLeft(i);
        int right = getRight(i);

        if(left <= this->size && arr[left] < arr[min])
            min = left;
        if(right <= this->size && arr[right] < arr[min])
            min = right;

        if(i != min){
            swap(arr[i], arr[min]);
            min_heapify(min);
        }
    }
    void insert(T data){
        this->size++;
        this->arr[size] = data;
        this->shiftUp(this->size);
    }
    T extract_min(){
        T value = arr[0];

        arr[0] = arr[size];
        this->size--;
        
        min_heapify(0);
        return value;
    }
    T minimum(){
        return arr[0];
    }
    void getArray(){
        for (int i=0;i<this->size+1;i++){
            std::cout << this->arr[i] << " ";
        }
        std::cout << "\n";
    }
};