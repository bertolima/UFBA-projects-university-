#pragma once
#include <iostream>
#include "Node.h"

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
	bool erase(int data);
};

class frontLinkedList : public LinkedList {
public:
	frontLinkedList();
	void insert(int data);
};

class circularLinkedList : public LinkedList {
public:
	circularLinkedList();
	void insert(int data);
	bool search(int data);
	void remove(int data);
	void print();
	
};
