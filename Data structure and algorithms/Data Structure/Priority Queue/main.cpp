#include "include/priorityQueue.h"
#include <iostream>

int main(){
    maxPriotiryQueue<int> queue1;
    minPriotiryQueue<int> queue2;

    queue1.insert(5);
    queue1.insert(10);
    queue1.insert(2);
    queue1.insert(1);
    queue1.insert(28);
    queue1.insert(40);
    queue1.insert(23);
    queue1.insert(100);

    std::cout << queue1.maximum() << "\n";

    queue2.insert(5);
    queue2.insert(10);
    queue2.insert(2);
    queue2.insert(1);
    queue2.insert(28);
    queue2.insert(40);
    queue2.insert(23);
    queue2.insert(100);

    std::cout << queue2.minimum() << "\n";

    for (int i=0;i<8;i++){
        std::cout << queue1.extract_max() << " ";
    }
    std::cout << "\n";

    for (int i=0;i<8;i++){
        std::cout << queue2.extract_min() << " ";
    }
    std::cout << "\n";



}