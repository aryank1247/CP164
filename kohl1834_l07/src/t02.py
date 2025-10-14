"""
-------------------------------------------------------
[Lab 7 Task 2]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-03-01"
-------------------------------------------------------
"""
from List_linked import List

lst = List()
lst1 = List()

a = [2, 3, 5, 4, 1]
a1 = [4, 3, 2, 1, 5]

for value in a:
    lst.append(value)
for value in a1:
    lst1.append(value)
#
print(lst.identical_r(lst1))
