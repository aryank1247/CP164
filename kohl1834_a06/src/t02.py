"""
-------------------------------------------------------
[Assignment 6 Task 2]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-03-02"
-------------------------------------------------------
"""
from Priority_Queue_linked import Priority_Queue

# Test Priority Queue operations
pq = Priority_Queue()

print("Testing Priority Queue:")

# Test is_empty on empty queue
print("Is empty:", pq.is_empty())  # Expected: True

# Test insert with priority order
pq.insert(50)
pq.insert(20)
pq.insert(40)
pq.insert(10)
pq.insert(30)
print("Inserted 50, 20, 40, 10, 30 (should be ordered by priority)")

print("Priority Queue length:", len(pq))  # Expected: 5

# Test peek
print("Peek front:", pq.peek())  # Expected: 10 (lowest value has highest priority)

# Test remove
print("Removed:", pq.remove())  # Expected: 10
print("Removed:", pq.remove())  # Expected: 20

# Test is_empty after removals
print("Is empty:", pq.is_empty())  # Expected: False

# Test remove last elements
print("Removed:", pq.remove())  # Expected: 30
print("Removed:", pq.remove())  # Expected: 40
print("Removed:", pq.remove())  # Expected: 50

# Test is_empty on empty queue again
print("Is empty:", pq.is_empty())  # Expected: True
