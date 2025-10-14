"""
-------------------------------------------------------
[Assignment 1 Task 4]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-12"
-------------------------------------------------------
"""
from functions import find_subs

# Testing find_subs function
print(find_subs("It was a really, really, big assignment.", "real"))  # Expected: [9, 17]
print(find_subs("aaaa", "aa"))  # Expected: [0, 2]
