// linkedi.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "BinaryTree.h"
#include <Windows.h>

int main()
{

    BinaryTree tree;

    tree.insert(25);
    tree.insert(15);
    tree.insert(10);
    tree.insert(4);
    tree.insert(12);

    tree.print_post_order(tree.getRoot());
    std::cout << "\n";
    tree.print_in_order(tree.getRoot());
    std::cout << "\n";
    tree.print_pre_order(tree.getRoot());
    std::cout << "\n";

    tree.remove(tree.getRoot(), 4);

    tree.print_pre_order(tree.getRoot());
    std::cout << "\n";


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
