"""
-------------------------------------------------------
[Assignment 1 Task 10]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-12"
-------------------------------------------------------
"""
from functions import matrix_rotate_right

# Test the matrix_rotate_right function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

rotated = matrix_rotate_right(matrix)

print("Rotated matrix:")
for row in rotated:
    print(row)
