#pragma once
#include "Node.h"

class Queue {
private:
	//pointers to end and start of queue
	Node* head;
	Node* tail;

	//a counter to get how many elements the queue has
	unsigned int nElements;
public:
	Queue();
	~Queue();
	void push_back(int data);
	void pop();
	bool search(int data);
	void print();
	bool isEmpty();
	int front();
	int back();
	int size();
};