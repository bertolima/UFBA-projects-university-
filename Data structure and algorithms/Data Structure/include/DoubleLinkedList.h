#pragma once
#include <iostream>
#include "Node.h"


class DoubleLinkedList {
private:
	double_Node* head;
	double_Node* tail;
public:
	DoubleLinkedList();
	~DoubleLinkedList();
	void insert(int data);
	void remove(int data);
	bool search(int data);
	void print_in_order();
	void print_reverse();

};
