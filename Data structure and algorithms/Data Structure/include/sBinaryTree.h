#pragma once
#include "Node.h"

class sBinaryTree {
private:
	treeNode* root;


public:
	sBinaryTree();
	treeNode* getRoot();
	void insert(int data);
	void remove(int data);
	void transplant(treeNode* u, treeNode* v);
	void delet(int data);
	bool search(int data);
	treeNode* recursiveSearch(treeNode* root, int data);
	treeNode* iterativeSearch(treeNode* root, int data);
	treeNode* maximum(treeNode* root);
	treeNode* minimum(treeNode* root);
	treeNode* recursiveMaximum(treeNode* root);
	treeNode* recursiveMinimum(treeNode* root);

	void print_post_order(treeNode* root);
	void print_in_order(treeNode* root);
	void print_pre_order(treeNode* root);
};
