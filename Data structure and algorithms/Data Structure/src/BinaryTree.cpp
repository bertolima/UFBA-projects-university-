#include "BinaryTree.h"
#include <stack>

BinaryTree::BinaryTree()
{
	this->root = nullptr;
}

treeNode* BinaryTree::getRoot()
{
	return this->root;
}

void BinaryTree::insert(int data)
{
	treeNode* new_node = new treeNode(data);
	if (!this->root) {
		this->root = new_node;
		return;
	}

	treeNode* tmp = this->root;
	while (tmp) {
		if (data >= tmp->data) {
			if (tmp->right == nullptr) {
				tmp->right = new_node;
				return;
			}
			tmp = tmp->right;
		}
		else {
			if (tmp->left == nullptr) {
				tmp->left = new_node;
				return;
			}
			tmp = tmp->left;
		}
	}
}

void BinaryTree::remove(treeNode* root, int data)
{
	treeNode* current = root;
	treeNode* parent = root;

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

		if (!current)
			return;

		if (!(current->left) && !(current->right)) {
			if (current == root)
				root = nullptr;
			else if (current == parent->left)
				parent->left = nullptr;
			else if (current->right == nullptr)
				parent->right = nullptr;
			delete current;
		}
}

bool BinaryTree::search(int data)
{
	return false;
}

void BinaryTree::print_post_order(treeNode* root)
{
	if (!root)
		return;
	print_post_order(root->left);
	print_post_order(root->right);
	std::cout << root->data << " ";

}

void BinaryTree::print_in_order(treeNode* root)
{
	if (!root)
		return;
	print_in_order(root->left);
	std::cout << root->data << " ";
	print_in_order(root->right);

}

void BinaryTree::print_pre_order(treeNode* root)
{
	if (!root)
		return;
	std::cout << root->data << " ";
	print_pre_order(root->left);
	print_pre_order(root->right);

}
