"""
-------------------------------------------------------
[Lab 1 Task 1]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-18"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_to_array

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

target = []

stack_to_array(stack, target)

print("Is the stack empty after transferring to array? ", stack.is_empty())

print("Elements in the target array:", target)
