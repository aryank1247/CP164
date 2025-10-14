"""
-------------------------------------------------------
[Assignment 4 Task 5]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-02-02"
-------------------------------------------------------
"""
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue
q = Priority_Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)

t1, t2 = (pq_split_key(q, 2))

print(list(t1), list(t2))
