"""
-------------------------------------------------------
[Assignment 3 Task 7]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-26"
-------------------------------------------------------
"""
from functions import reroute


def run_tests():

    # Test case 1: Valid operations
    values_in = [1, 2, 3, 4]
    opstring = "SSXXSSXX"
    print(f"Test Case 1:\nInput: {values_in}\nOpstring: '{opstring}'")
    result = reroute(opstring, values_in)
    print(f"Expected Output: [2, 1, 4, 3]\nActual Output: {result}\n")

    # Test case 2: Invalid operations (pop from empty stack)
    opstring = "SX"
    print(f"Test Case 2:\nInput: {values_in}\nOpstring: '{opstring}'")
    result = reroute(opstring, values_in)
    print(f"Expected Output: None\nActual Output: {result}\n")

    # Test case 3: Invalid operations (not all input values are processed)
    opstring = "SSX"
    print(f"Test Case 3:\nInput: {values_in}\nOpstring: '{opstring}'")
    result = reroute(opstring, values_in)
    print(f"Expected Output: None\nActual Output: {result}\n")

    # Test case 4: Edge case - Empty inputs
    values_in = []
    opstring = ""
    print(f"Test Case 4:\nInput: {values_in}\nOpstring: '{opstring}'")
    result = reroute(opstring, values_in)
    print(f"Expected Output: []\nActual Output: {result}\n")

    # Test case 5: Invalid character in opstring
    values_in = [1, 2, 3, 4]
    opstring = "SSXSY"
    print(f"Test Case 5:\nInput: {values_in}\nOpstring: '{opstring}'")
    result = reroute(opstring, values_in)
    print(f"Expected Output: None\nActual Output: {result}\n")


# Run the tests
if __name__ == "__main__":
    run_tests()

