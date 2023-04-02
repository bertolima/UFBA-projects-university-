#include "LinkedList.h"

LinkedList::LinkedList()
{
	this->head = nullptr;
	this->tail = nullptr;
}

LinkedList::~LinkedList()
{
}

void LinkedList::insert(int data)
{
	Node* new_node = new Node(data);
	if (this->head == nullptr) {
		this->head = new_node;
		this->tail = new_node;
		return;
	}
	else {

		this->tail->next = new_node;
		this->tail = new_node;
	}
}

bool LinkedList::search(int data)
{
	Node* current = this->head;
	while (current->next != nullptr) {
		if (current->data == data)
			return true;
		current = current->next;
	}
	return false;
}

void LinkedList::remove()
{
	Node* current = this->head;
	while (current->next->next != nullptr) {
		current = current->next;
	}
	
	delete current->next;
	current->next = nullptr;
	this->tail = current;
}

void LinkedList::print()
{
	Node* current = this->head;
	while (current->next != nullptr) {
		std::cout << current->data << ", ";
		current = current->next;
	}
	std::cout << current->data << "." << std::endl;
}
