"""
-------------------------------------------------------
[Assignment 6 Task 1]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-03-02"
-------------------------------------------------------
"""
from Queue_linked import Queue

# Test Queue operations
queue = Queue()

print("Testing Queue:")

# Test is_empty on empty queue
print("Is empty:", queue.is_empty())  # Expected: True

# Test insert
queue.insert(10)
queue.insert(20)
queue.insert(30)
print("Inserted 10, 20, 30")

print("Queue length:", len(queue))  # Expected: 3

# Test peek
print("Peek front:", queue.peek())  # Expected: 10

# Test remove
print("Removed:", queue.remove())  # Expected: 10
print("Removed:", queue.remove())  # Expected: 20

# Test is_empty after removals
print("Is empty:", queue.is_empty())  # Expected: False

# Test remove last element
print("Removed:", queue.remove())  # Expected: 30

# Test is_empty on empty queue again
print("Is empty:", queue.is_empty())  # Expected: True
