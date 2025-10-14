"""
-------------------------------------------------------
[Assignment 4 Task 3]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-02-02"
-------------------------------------------------------
"""
from Queue_array import Queue
from functions import queue_combine

# Test Case 1: Interleaved Queues
source1 = Queue()
source2 = Queue()

source1.insert(5)
source1.insert(8)
source1.insert(12)
source1.insert(8)

source2.insert(7)
source2.insert(9)
source2.insert(14)

target = queue_combine(source1, source2)

print("Test Case 1 - Interleaved Queues")
print("Expected: 5, 7, 8, 9, 12, 14, 8")
print("Result:", end=" ")
while not target.is_empty():
    print(target.remove(), end=", ")
print("\n")

# Test Case 2: One Empty Queue
source1 = Queue()
source2 = Queue()

source1.insert(1)
source1.insert(3)
source1.insert(5)

target = queue_combine(source1, source2)

print("Test Case 2 - One Empty Queue")
print("Expected: 1, 3, 5")
print("Result:", end=" ")
while not target.is_empty():
    print(target.remove(), end=", ")
print("\n")

# Test Case 3: Both Empty Queues
source1 = Queue()
source2 = Queue()

target = queue_combine(source1, source2)

print("Test Case 3 - Both Empty Queues")
print("Expected: (empty)")
print("Result:", end=" ")
while not target.is_empty():
    print(target.remove(), end=", ")
print("\n")

# Test Case 4: Different Sized Queues
source1 = Queue()
source2 = Queue()

source1.insert(10)
source1.insert(20)

source2.insert(5)
source2.insert(15)
source2.insert(25)
source2.insert(35)

target = queue_combine(source1, source2)

print("Test Case 4 - Different Sized Queues")
print("Expected: 10, 5, 20, 15, 25, 35")
print("Result:", end=" ")
while not target.is_empty():
    print(target.remove(), end=", ")
print("\n")
