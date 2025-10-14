"""
-------------------------------------------------------
[Lab 2 Task 2]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-18"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = [1, 2, 3, 4, 5]

print("Source array before transferring to stack:", source)

array_to_stack(stack, source)

print("Source array after transferring to stack:", source)

print("Elements in the stack from top to bottom:")
for element in stack:
    print(element)

