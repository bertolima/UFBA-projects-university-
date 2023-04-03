#include "DoubleLinkedList.h"

DoubleLinkedList::DoubleLinkedList()
{
	this->head = nullptr;
	this->tail = nullptr;
}

DoubleLinkedList::~DoubleLinkedList()
{
}

void DoubleLinkedList::insert(int data)
{
	double_Node* new_node = new double_Node(data);
	if (!(this->head)) {
		this->head = new_node;
		this->tail = new_node;
	}
	else {
		this->tail->next = new_node;
		new_node->prev = this->tail;
		this->tail = new_node;	
	}
}

void DoubleLinkedList::remove(int data)
{
	double_Node* order = this->head;
	double_Node* reverse = this->tail;

	while (order) {
		if (order->data == data) {
			if (order->prev){
				double_Node* next = order->next;
				double_Node* prev = order->prev;
				delete order;
				order = prev;
				order->next = next;
				break;
			}
			else {
				double_Node* next = order->next;
				delete order;
				this->head = next;
				break;
			}
		}
		else if (reverse->data == data) {
			if (reverse->prev) {
				double_Node* next = reverse->next;
				double_Node* prev = reverse->prev;
				delete reverse;
				reverse = prev;
				reverse->next = next;
				break;
			}
			else {
				double_Node* next = reverse->next;
				delete reverse;
				this->head = next;
				break;
			}

		}
		order = order->next;
	}

}

bool DoubleLinkedList::search(int data)
{
	double_Node* order = this->head;
	double_Node* reverse = this->tail;

	while (order) {
		if (order->data == data || reverse->data == data) {
			return true;
		}
		order = order->next;
		reverse = reverse->prev;
	}
	return false;
}

void DoubleLinkedList::print_in_order()
{
	double_Node* current = this->head;
	while (current->next) {
		std::cout << current->data << ", ";
		current = current->next;
	}
	std::cout << current->data << "." << "\n";

}

void DoubleLinkedList::print_reverse()
{
	double_Node* current = this->tail;
	while (current->prev) {
		std::cout << current->data << ", ";
		current = current->prev;
	}
	std::cout << current->data << "." << "\n";
}
