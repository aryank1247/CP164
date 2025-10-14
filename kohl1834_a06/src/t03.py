"""
-------------------------------------------------------
[Assignment 6 Task 3]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-03-02"
-------------------------------------------------------
"""
from Deque_linked import Deque

# Test Deque operations
deque = Deque()

print("Testing Deque:")

# Test is_empty on empty deque
print("Is empty:", deque.is_empty())  # Expected: True

# Test insert_front and insert_rear
deque.insert_front(20)
deque.insert_rear(30)
deque.insert_front(10)
deque.insert_rear(40)
print("Inserted 10 at front, 20 at front, 30 at rear, 40 at rear")

print("Deque length:", len(deque))  # Expected: 4

# Test peek_front and peek_rear
print("Peek front:", deque.peek_front())  # Expected: 10
print("Peek rear:", deque.peek_rear())  # Expected: 40

# Test remove_front and remove_rear
print("Removed from front:", deque.remove_front())  # Expected: 10
print("Removed from rear:", deque.remove_rear())  # Expected: 40

# Test is_empty after removals
print("Is empty:", deque.is_empty())  # Expected: False

# Test remove remaining elements
print("Removed from front:", deque.remove_front())  # Expected: 20
print("Removed from rear:", deque.remove_rear())  # Expected: 30

# Test is_empty on empty deque again
print("Is empty:", deque.is_empty())  # Expected: True
