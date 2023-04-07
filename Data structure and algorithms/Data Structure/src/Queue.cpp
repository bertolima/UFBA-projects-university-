#include "Queue.h"

Queue::Queue()
{
	this->head = nullptr;
	this->tail = nullptr;
	this->nElements = 0;
}

Queue::~Queue()
{
}

void Queue::push_back(int data)
{
	Node* new_node = new Node(data);
	if (!this->head) {
		this->head = new_node;
		this->tail = new_node;
		this->nElements++;
		return;
	}
	this->tail->next = new_node;
	this->tail = new_node;
	this->nElements++;
}

void Queue::pop()
{
	if (!(this->nElements > 0))
		return;
	Node* tmp = this->head->next;
	delete this->head;
	this->head = tmp;
	this->nElements--;
}

bool Queue::search(int data)
{
	Node* tmp = this->head;

	while (tmp) {
		if (tmp->data == data)
			return true;
		tmp = tmp->next;
	}
	return false;
}

void Queue::print()
{
	Node* tmp = this->head;
	while (tmp->next) {
		std::cout << tmp->data << ", ";
		tmp = tmp->next;
	}
	std::cout << tmp->data << "." << "\n";
}

bool Queue::isEmpty()
{
	if (this->nElements > 0)
		return false;
	return true;
}

int Queue::front()
{
	return (this->head->data);
}

int Queue::back()
{
	return (this->tail->data);
}

int Queue::size()
{
	return this->nElements;
}
