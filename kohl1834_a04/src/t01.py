"""
-------------------------------------------------------
[Assignment 4 Task 1]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-02-02"
-------------------------------------------------------
"""
from Queue_circular import Queue


def test_queue():
    print("Testing Circular Queue Implementation\n")

    q = Queue(5)
    print("Initial Queue (should be empty):", list(q))

    print("Inserting values: 1, 2, 3")
    q.insert(1)
    q.insert(2)
    q.insert(3)
    print("Queue after inserts:", list(q))

    print("Peeking at front (should be 1):", q.peek())

    print("Removing an element (should be 1)")
    print("Removed:", q.remove())
    print("Queue after remove:", list(q))

    print("Inserting more values: 4, 5")
    q.insert(4)
    q.insert(5)
    print("Queue after inserts:", list(q))

    print("Inserting another value: 6 (should wrap around)")
    q.insert(6)
    print("Queue after wrap-around insert:", list(q))

    print("Removing elements until empty")
    while not q.is_empty():
        print("Removed:", q.remove())
        print("Queue:", list(q))

    print("Queue should now be empty.")


test_queue()

