"""
-------------------------------------------------------
[Lab 5 Task 6]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-02-08"
-------------------------------------------------------
"""
from functions import bag_to_set

# bag = [4,3,2,1,0]
# bag = [0,1,2,3,4]
bag = [4, 5, 3, 4, 5, 2, 2, 4]
print("Bag: {}".format(bag))
set = bag_to_set(bag)
print("Set: {}".format(set))
