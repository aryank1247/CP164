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
from functions import gcd
from random import randint

m = randint(0, 20000)
n = randint(-20000, 20000)

ans = gcd(m, n)
print("m: {}\tn: {}\tans: {}".format(m, n, ans))
