#include "Node.h"

Node::Node(int data)
{
	this->data = data;
	this->next = nullptr;
}

double_Node::double_Node(int data):Node(data) {
	this->prev = nullptr;
}