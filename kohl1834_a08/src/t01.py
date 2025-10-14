"""
-------------------------------------------------------
[Assignment 8 Task 1]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-03-16"
-------------------------------------------------------
"""
# Imports
# Constants

from BST_linked import BST

bst = BST()
num = [1, 2, 3, 4, 5]

for value in num:
    bst.insert(value)

print(bst.is_valid())

print(bst.is_balanced())

print(bst.min())

print()
print(bst.leaf_count())

print(bst.one_child_count())

print(bst.two_child_count())

print()

print(bst.inorder())

print(bst.preorder())

print(bst.postorder())

print(bst.levelorder())

print(bst.remove(3))
