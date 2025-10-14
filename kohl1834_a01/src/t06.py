"""
-------------------------------------------------------
[Assignment 1 Task 6]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-12"
-------------------------------------------------------
"""
from functions import median_scores

# Testing median_scores function
with open("numbers.txt", "r") as file:
    print(median_scores(file))
