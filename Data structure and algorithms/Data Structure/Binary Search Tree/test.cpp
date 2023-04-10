// bsts.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "Tree.h"

int main()
{
    Tree tree;
    tree.insert(tree.root, 15);
    tree.insert(tree.root, 6);
    tree.insert(tree.root, 18);
    tree.insert(tree.root, 17);
    tree.insert(tree.root, 20);
    tree.insert(tree.root, 3);
    tree.insert(tree.root, 7);
    tree.insert(tree.root, 2);
    tree.insert(tree.root, 4);
    tree.insert(tree.root, 13);
    tree.insert(tree.root, 9);
    tree.print_inorder(tree.root);
    std::cout << "\n";
    tree.print_preorder(tree.root);
    std::cout << "\n";
    tree.print_posorder(tree.root);
    std::cout << "\n";
    tree.remove(tree.root, 25);
    tree.print_inorder(tree.root);
    std::cout << "\n";
    std::cout << tree.predecessor(tree.root, 2)->data <<"\n";

    std::cout << "Hello World!\n";
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
