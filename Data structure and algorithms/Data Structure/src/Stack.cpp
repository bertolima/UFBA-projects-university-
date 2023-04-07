#include "Stack.h"
#include <iostream>

Stack::Stack()
{
	this->current = nullptr;
	this->nElements = 0;
}

Stack::~Stack()
{
}

void Stack::push_back(int data)
{
	Node* new_node = new Node(data);
	if (!this->current) {
		this->current = new_node;
		this->nElements++;
		return;
	}
	new_node->next = this->current;
	this->current = new_node;
	this->nElements++;
}

void Stack::pop()
{
	if (!(nElements > 0))
		return;

	Node* tmp = this->current->next;
	delete this->current;
	this->current = tmp;
	this->nElements--;
}

bool Stack::search(int data)
{
	Node* tmp = this->current;
	while (tmp) {
		if (tmp->data == data)
			return true;
		tmp = tmp->next;
	}
	return false;
}

void Stack::print()
{
	Node* tmp = this->current;

	while (tmp->next) {
		std::cout << tmp->data << ", ";
		tmp = tmp->next;
	}
	std::cout << tmp->data << "." << "\n";
}

int Stack::size()
{
	return (this->nElements);
}

bool Stack::isEmpty()
{
	if (this->nElements > 0)
		return false;
	return true;
}

int Stack::top()
{
	return this->current->data;
}
