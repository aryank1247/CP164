"""
-------------------------------------------------------
[Assignment 4 Task 2]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-02-02"
-------------------------------------------------------
"""
from Queue_array import Queue

# Test Case 1: Equal Queues
q1 = Queue()
q2 = Queue()
q1.insert(1)
q1.insert(2)
q1.insert(3)
q2.insert(1)
q2.insert(2)
q2.insert(3)
print("Test Case 1 - Equal Queues:", q1 == q2)  # Expected: True

# Test Case 2: Unequal Queues (Different Values)
q3 = Queue()
q4 = Queue()
q3.insert(1)
q3.insert(2)
q3.insert(3)
q4.insert(4)
q4.insert(5)
q4.insert(6)
print("Test Case 2 - Unequal Queues (Different Values):", q3 == q4)  # Expected: False

# Test Case 3: Unequal Queues (Different Lengths)
q5 = Queue()
q6 = Queue()
q5.insert(1)
q5.insert(2)
q6.insert(1)
q6.insert(2)
q6.insert(3)
print("Test Case 3 - Unequal Queues (Different Lengths):", q5 == q6)  # Expected: False

# Test Case 4: Both Empty Queues
q7 = Queue()
q8 = Queue()
print("Test Case 4 - Both Empty Queues:", q7 == q8)  # Expected: True

# Test Case 5: One Empty, One Non-Empty Queue
q9 = Queue()
q10 = Queue()
q10.insert(1)
print("Test Case 5 - One Empty, One Non-Empty Queue:", q9 == q10)  # Expected: False
