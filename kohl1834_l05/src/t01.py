"""
-------------------------------------------------------
[Lab 5 Task 1]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-02-08"
-------------------------------------------------------
"""
from random import randint
from functions import recurse

x = randint(0, 5)
y = randint(0, 5)

print("x: {}\ty {}".format(x, y))
ans = recurse(x, y)
print(ans)

x = randint(0, 3)
y = randint(0, 3)

print("x: {}\ty {}".format(x, y))
ans = recurse(x, y)
print(ans)
