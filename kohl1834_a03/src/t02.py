"""
-------------------------------------------------------
[Assignment 3 Task 2]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-26"
-------------------------------------------------------
"""
from Stack_array import Stack
if __name__ == "__main__":
    source = Stack()
    for value in [8, 14, 9, 7, 5, 12]:  # Push values into source stack
        source._values.append(value)  # Directly append to _values for testing

    print("Source (original):")
    print(" -> ".join(map(str, reversed(source._values))))  # Print top to bottom

    target1, target2 = source.split_alt()

    print("Source (after split):")
    print(" -> ".join(map(str, reversed(source._values))))  # Should be empty

    print("Target1 (alternating values):")
    print(" -> ".join(map(str, reversed(target1._values))))  # Print target1 values

    print("Target2 (alternating values):")
    print(" -> ".join(map(str, reversed(target2._values))))  # Print target2 values

