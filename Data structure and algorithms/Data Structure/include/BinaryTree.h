#pragma once
#include "Node.h"

class BinaryTree {
private:
	treeNode* root;
public:
	BinaryTree();
	treeNode* getRoot();
	void insert(int data);
	void remove(treeNode* root, int data);
	bool search(int data);
	void print_post_order(treeNode* root);
	void print_in_order(treeNode* root);
	void print_pre_order(treeNode* root);
};
