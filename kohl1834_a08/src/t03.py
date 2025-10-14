"""
-------------------------------------------------------
[Assignment 8 Task 3]
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
from functions import letter_table, do_comparisons, comparison_total
from Letter import Letter
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"

bst2 = BST()

for a in DATA2:
    letter = Letter(a)
    bst2.insert(letter)

file = open("gibbon.txt", "r", encoding="utf-8")
do_comparisons(file, bst2)
total = comparison_total(bst2)

letter_table(bst2)
