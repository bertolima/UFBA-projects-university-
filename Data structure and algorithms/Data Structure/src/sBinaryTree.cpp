#include "sBinaryTree.h"
#include <stack>


sBinaryTree::sBinaryTree()
{
	this->root = nullptr;
}

treeNode* sBinaryTree::getRoot()
{
	return this->root;
}

//void sBinaryTree::insert(int data)
//{
//	treeNode* new_node = new treeNode(data);
//	if (!this->root) {
//		this->root = new_node;
//		return;
//	}
//
//	treeNode* tmp = this->root;
//	while (tmp) {
//		if (data >= tmp->data) {
//			if (tmp->right == nullptr) {
//				tmp->right = new_node;
//				return;
//			}
//			tmp = tmp->right;
//		}
//		else {
//			if (tmp->left == nullptr) {
//				tmp->left = new_node;
//				return;
//			}
//			tmp = tmp->left;
//		}
//	}
//}

void sBinaryTree::insert(int data) {
	treeNode* new_node = new treeNode(data);
	treeNode* current = this->root;
	treeNode* parent = nullptr;

	while (current) {
		parent = current;
		if (data < current->data)
			current = current->left;
		else
			current = current->right;
	}
	if (!parent)
		this->root = new_node;
	else if (data < parent->data)
		parent->left = new_node;
	else
		parent->right = new_node;

}

void sBinaryTree::remove(int data)
{
	/*need parent node to turn parent->left and parent->right to nullpointers, without this, when delete current,
	current->right and current->left point to invalid address of memory.*/
	treeNode* current = this->root;
	treeNode* parent = this->root;

	//loop to find node that node->data == data gived, if don`t found current == nullptr
	while (current) {
		parent = current;
		if (data < current->data)
			current = current->left;
		else if (data > current->data)
			current = current->right;
		if (current->data == data) {
			break;
		}
	}

	//if current == nullptr, return without deletions
	if (!current)
		return;

	//this case is for nodes without children
	if (!(current->left) && !(current->right)) {
		//if the node is the root, we make root point to null to delete the space occuped by root in memory
		if (current == this->root)
			this->root = nullptr;
		//as said earleir, parent pointer is necessary to don't get memory erros
		//we turn parent->left or parent->right to nullpointer, to properly delete what occuped that memory position
		else if (current == parent->left)
			parent->left = nullptr;
		else if (current->right == nullptr)
			parent->right = nullptr;
		delete current;
	}
	//in this case de node has only right child
	else if (!(current->left)) {
		//if the node is the root, the new root is equal the old root->right, then delete memory occuped by old root first node
		if (current == this->root)
			this->root = current->right;
		//again, use parent pointer to properly delete your right or left child
		else if (current == parent->left)
			parent->left = current->right;
		else if (current == parent->right)
			parent->right = current->right;
		delete current;
	}
	//same as above, but node has only left child
	else if (!(current->right)) {
		if (current == this->root)
			this->root = current->left;
		else if (current == parent->left)
			parent->left = current->left;
		else if (current == parent->left)
			parent->right = current->right;
		delete current;
	}
	//in this case the node has left and right child
	else {
		//we need to create a temporary node pointer to find the node that will replace the deleted node
		treeNode* new_node = current->right;
		//need the parent node of node that will replace, cause after replaced we need to delete it
		treeNode* new_node_parent = current;
		//loop to find the node
		while (new_node->left) {
			new_node_parent = new_node;
			new_node = new_node->left;
		}
		//replace node datas
		current->data = new_node->data;
		//operations that will delete node used to replace data
		new_node_parent->right = nullptr;
		delete new_node;;
	}
}

void sBinaryTree::transplant(treeNode* u, treeNode* v)
{
	if (!u)
		this->root = v;
	else if(u == u->left)
		

}

void sBinaryTree::delet(int data)
{
	treeNode* current = this->root;
	if(!current->left)
		

}

bool sBinaryTree::search(int data)
{
	treeNode* current = this->root;

	while (current) {
		if (current->data == data)
			return true;
		if (data < current->data)
			current = current->left;
		else
			current = current->right;
	}
	return false;
}

treeNode* sBinaryTree::recursiveSearch(treeNode* root ,int data) {
	if (!root || data == root->data)
		return root;
	if (data < root->data)
		return recursiveSearch(root->left, data);
	else
		return recursiveSearch(root->right, data);
}

treeNode* sBinaryTree::iterativeSearch(treeNode* root, int data)
{
	while (root && data != root->data) {
		if (data < root->data)
			root = root->left;
		else
			root = root->right;
	}
	return root;
}

treeNode* sBinaryTree::maximum(treeNode* root)
{
	while (root->right) {
		root = root->right;
	}
	return root;
}

treeNode* sBinaryTree::minimum(treeNode* root)
{
	while (root->left) {
		root = root->left;
	}
	return root;
}

treeNode* sBinaryTree::recursiveMaximum(treeNode* root)
{
	if (!root)
		return root;
	return recursiveMaximum(root->right);
}

treeNode* sBinaryTree::recursiveMinimum(treeNode* root)
{
	if (!root)
		return root;
	return recursiveMinimum(root->left);
}

void sBinaryTree::print_post_order(treeNode* root)
{
	if (!root)
		return;
	print_post_order(root->left);
	print_post_order(root->right);
	std::cout << root->data << " ";
}


void sBinaryTree::print_in_order(treeNode* root)
{
	if (root) {
		print_in_order(root->left);
		std::cout << root->data << " ";
		print_in_order(root->right);
	}
}

void sBinaryTree::print_pre_order(treeNode* root)
{
	if (!root)
		return;
	std::cout << root->data << " ";
	print_pre_order(root->left);
	print_pre_order(root->right);
}
