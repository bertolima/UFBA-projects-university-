#pragma once
#include <iostream>

class Node {
public:
	int data;
	Node* left;
	Node* right;
	Node(int data);
	~Node();
};

class Tree {
public:
	Node* root;
	Tree();
	~Tree();
	void insert(Node*& current, int data);
	Node* search(Node* current, int data);
	void remove(Node* &current, int data);
	Node* maximum(Node* root);
	Node* minimum(Node* root);
	void print_inorder(Node* root);
	void print_preorder(Node* root);
	void print_posorder(Node* root);
	Node* sucessor(Node* root, int data);
	Node* predecessor(Node* root, int data);
	
};

