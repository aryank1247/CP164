"""
-------------------------------------------------------
[Lab 7 Task 3]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-03-01"
-------------------------------------------------------
"""
from List_linked import List

lst = List()
a = [2, 3, 1, 4, 5]

for i in a:
    lst.append(i)

target1, target2 = lst.split_alt_r()

print("Target1: ")
for value in target1:
    print(value)
print("---------------")
print("Target2: ")
for i in target2:
    print(value)
