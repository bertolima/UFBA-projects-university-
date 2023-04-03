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

bool LinkedList::erase(int data) {
	Node* current = this->head;
	while (current->next != nullptr) 
	{
		if (current->data == data) {
			Node* temp = current->next;
			delete current;
			current = nullptr;
			current = temp;
			return true;
		}
		current = current->next;
	}
	return false;
}

frontLinkedList::frontLinkedList():LinkedList() {

}

void frontLinkedList::insert(int data)
{
	Node* new_node = new Node(data);
	new_node->next = this->head;
	this->head = new_node;
}


circularLinkedList::circularLinkedList() :LinkedList()
{
}

void circularLinkedList::insert(int data)
{
	Node* new_node = new Node(data);
	if (!(this->head)) {
		new_node->next = new_node;
		this->head = new_node;
		this->tail = new_node;
		return;
	}
	new_node->next = this->head;
	this->tail->next = new_node;
	this->tail = new_node;

}

bool circularLinkedList::search(int data)
{
	return false;
}

void circularLinkedList::remove(int data)
{
	Node* current = this->head;

	while (current) {
		if (current->next->data == data) {
			Node* prev = current;
			Node* next = current->next->next;
			delete current->next;
			if (current->next == this->tail) {
				this->tail = prev;
				this->tail->next = next;
			}
			else if (current->next == this->head) {
				this->head = next;
				this->tail->next = this->head;
		
			}
			else {
				current = prev;
				current->next = next;
			}
			return;
		}
		current = current->next;
	}

}

void circularLinkedList::print()
{
	Node* current = this->head;

	while (current != this->tail) {
		std::cout << current->data << ", ";
		current = current->next;
	}
	std::cout << current->data << "." << "\n";

}
