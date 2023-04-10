#pragma once
#include <iostream>

class Node {
public:
	int data;
	Node* next;
	Node(int data);
};

class double_Node : public Node {
public:
	double_Node* next;
	double_Node* prev;
	double_Node(int data);
};

class treeNode {
public:
	int data;
	treeNode* left;
	treeNode* right;
	treeNode(int data);
	~treeNode();
};
