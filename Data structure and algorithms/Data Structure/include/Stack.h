#pragma once
#include "Node.h"

class Stack {
private:
	//main node thats real represent the stack
	Node* current;

	//counter to get how many elements the stack has
	unsigned int nElements;
public:
	Stack();
	~Stack();
	void push_back(int data);
	void pop();
	bool search(int data);
	void print();
	int size();
	bool isEmpty();
	int top();

};

