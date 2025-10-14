"""
-------------------------------------------------------
[Assignment 3 Task 4]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-26"
-------------------------------------------------------
"""
from Stack_array import Stack


def main():
    source1 = Stack()
    source2 = Stack()
    l = [8, 12, 8, 5]
    for v in l:
        source1.push(v)
    l2 = [14, 9, 7, 1, 6, 3]
    for x in l2:
        source2.push(x)
    stack = Stack()
    stack.combine(source1, source2)
    for s in stack:
        print(s)


main()
