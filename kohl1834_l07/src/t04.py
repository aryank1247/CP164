"""
-------------------------------------------------------
[Lab 7 Task 4]
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
lst2 = List()
a = [2, 4, 3, 5, 1]
a1 = [2, 4, 1, 12, 11]

for i in a:
    lst.append(i)
for i in a1:
    lst1.append(i)

lst2.intersection_r(lst, lst1)
for i in lst2:
    print(i)
