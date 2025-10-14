"""
-------------------------------------------------------
[Assignment 1 Task 9]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-12"
-------------------------------------------------------
"""
from functions import matrixes_multiply

# Test the matrixes_multiply function
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8], [9, 10], [11, 12]]
result = matrixes_multiply(matrix_a, matrix_b)

print("Matrix multiplication result:")
for row in result:
    print(row)
