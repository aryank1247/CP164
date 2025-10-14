"""
-------------------------------------------------------
[Assignment 10  Task 4]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-03-29"
-------------------------------------------------------
"""
# Constants
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()

array = [88, 23, 54, 13, 87, 999, 100, 5]

for i in array:
    a.insert_rear(i)

Sorts.gnome_sort(a)
array = []
for i in a:
    print(i)
