#pragma once
#include <iostream>

class Node {
public:
	int data;
	Node* next;
	Node(int data) {
		this->data = data;
		this->next = nullptr;
	}
};


class LinkedList {
protected:
	Node* head;
	Node* tail;
public:
	LinkedList();
	~LinkedList();
	void insert(int data);
	bool search(int data);
	void remove();
	void print();



};
