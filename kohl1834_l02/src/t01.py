"""
-------------------------------------------------------
[Lab 2 Task 1]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-18"
-------------------------------------------------------
"""
from Stack_array import Stack

stack = Stack()

print("Is the stack empty? ", stack.is_empty())

stack.push(26)
stack.push(43)
stack.push(52)

print("Is the stack empty after pushing elements? ", stack.is_empty())

top_element = stack.peek()
print("Top element (peek): ", top_element)

popped_element = stack.pop()
print("Popped element: ", popped_element)

new_top_element = stack.peek()
print("New top element after popping: ", new_top_element)

print("Elements in the stack from top to bottom:")

for element in stack:
    print(element)
