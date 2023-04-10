#include "Tree.h"

Node::Node(int data)
{
	this->data = data;
	this->left = nullptr;
	this->right = nullptr;
}

Node::~Node()
{
}

Tree::Tree()
{
	this->root = nullptr;
}

Tree::~Tree()
{
}

//need to pass node by reference(if not the new_node will always replace the head)
void Tree::insert(Node* & root,int data)
{
	Node* new_node = new Node(data);
	if (!root)
		root = new_node;
	else if (data < root->data)
		insert(root->left, data);
	else
		insert(root->right, data);
}

//no need to pass by reference cause we'll not modify any value.
Node* Tree::search(Node* root, int data)
{
	if (root == nullptr || root->data == data)
		return root;
	else if (data < root->data)
		return search(root->left, data);
	else
		return search(root->right, data);
}


//remove a node from a bst it's a little complicated
void Tree::remove(Node*& root, int data)
{
	//ll use these pointers to delete properly
	Node* parent = root;
	Node* current = root;
	//while loop to find the node who'll be deleted and your parent node
	while (current->data != data) {
		parent = current;
		if (data < current->data)
			current = current->left;
		else
			current = current->right;
		if (!current)
			break;
	}
	if (!current)
		return;
	//case if both node children are null
	if (!current->left && !current->right) {
		//if the node is root, we make root point to null
		if (current == root) {
			root = nullptr;
		}
		//else, we need to find if it's left child or right child of parent
		else if(!parent->left) {
			parent->right = nullptr;
		}
		else {
			parent->left = nullptr;
		}
		//properly delete without memory problems
		delete current;
	}
	//if it doesn't has left child
	else if (!current->left) {
		//if node it's root, the new root ll be right child
		if (current == root) {
			root = current->right;
		}
		//else, we need to find if it's left child or right child of parent
		else if (current == parent->left)
			parent->left = current->right;
		else
			parent->right = current->right;
		delete current;
	}
	//this case is equals the case before, but for right child
	else if (!current->right) {
		if (current == root)
			root = current->left;
		else if (current == parent->left)
			parent->left = current->left;
		else
			parent->right = current->left;
		delete current;
	}

	//in this case the node has both children
	else {
		//need this pointers to find the node who'll replace the deleted node
		//we need his parent too for properly delete him.
		Node* new_node = current->right;
		Node* new_node_parent = current->right;
		
		//while loop to find the node and your parent
		while (new_node->left) {
			new_node_parent = new_node;
			new_node = new_node->left;
		}
		//if this node has a right child we proced with this
		//the right child will occupe the node's position and the node will replace deleted node
		if (new_node->right) {
			Node* tmp = new_node->right;
			//just need to replace deleted node data
			current->data = new_node->data;
			//parent left child is equal of replaceable node, so we'll put parent left child as right child of reaplaceable node
			new_node_parent->left = tmp;
			new_node->right = nullptr;
			//delete reaplaceable node from old's position
			delete new_node;
		}
		//else, we proced with this
		//if doesn't has right child, we just have to delete him.
		else {
			current->data = new_node->data;
			new_node_parent->left = nullptr;
			delete new_node;
		}
	}

	//i dind't find any way to make this method recursively, if i add a pointer to node's parent i think this method can be a little small
	//but i prefer use only pointers to left and right child.
}


Node* Tree::maximum(Node* root)
{
	while (root->right) {
		root = root->right;
	}
	return root;

}

Node* Tree::minimum(Node* root)
{
	while (root->left) {
		root = root->left;
	}
	return root;
}

void Tree::print_inorder(Node* root)
{
	if (root) {
		print_inorder(root->left);
		std::cout << root->data << " ";
		print_inorder(root->right);
	}
}

void Tree::print_preorder(Node* root)
{
	if (root) {
		std::cout << root->data << " ";
		print_preorder(root->left);
		print_preorder(root->right);
	}
}

void Tree::print_posorder(Node* root)
{
	if (root) {
		print_preorder(root->left);
		print_preorder(root->right);
		std::cout << root->data << " ";
	}
}

Node* Tree::sucessor(Node* root, int data)
{
	Node* current = root;
	while (data != current->data) {
		if (data < current->data)
			current = current->left;
		else
			current = current->right;
	}

	if (current->right)
		return minimum(current->right);

	Node* parent = root;
	Node* sucessor = nullptr;

	while (parent->data != current->data){
		if (current->data < parent->data){
			sucessor = parent;
			parent = parent->left;
		}
		else
			parent = parent->right;
	}
	if (!sucessor)
		return current;
	return sucessor;
}

Node* Tree::predecessor(Node* root, int data)
{
	Node* current = root;
	while (data != current->data) {
		if (data < current->data)
			current = current->left;
		else
			current = current->right;
	}

	if (current->left)
		return maximum(current->left);

	Node* parent = root;
	Node* predecessor = nullptr;

	while (parent->data != current->data) {
		if (current->data < parent->data)
			parent = parent->left;
		else {
			predecessor = parent;
			parent = parent->right;
			
		}
	}
	if (!predecessor)
		return current;
	return predecessor;


}
