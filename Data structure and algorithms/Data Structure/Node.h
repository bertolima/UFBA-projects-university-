#pragma once

class Node {
public:
	int data;
	Node* next;
	Node(int data);
};

class double_Node : public Node {
public:
	double_Node* prev;
	double_Node(int data);
};
