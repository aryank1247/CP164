"""
-------------------------------------------------------
[Assignment 1 Task 3]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-12"
-------------------------------------------------------
"""
from functions import file_analyze

# Test the file_analyze function
file_name = "test_file.txt"  # Example file name (must exist in the working directory)

# Create a sample file for testing
with open(file_name, "w") as file:
    file.write("Hello World 123!\n")
    file.write("Python is fun.\n")
    file.write("Let's test this function.\n")

# Analyze the file
with open(file_name, "r") as fv:
    upp, low, dig, whi, rem = file_analyze(fv)

# Print the results
print(f"Uppercase letters: {upp}")
print(f"Lowercase letters: {low}")
print(f"Digits: {dig}")
print(f"Whitespace characters: {whi}")
print(f"Remaining characters: {rem}")

