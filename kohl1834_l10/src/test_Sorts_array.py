"""
-------------------------------------------------------
[Lab 1 Task 1]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-03-21"
-------------------------------------------------------
"""

from Number import Number
from Sorts_array import Sorts
import random

# Constants
SIZE = 100
XRANGE = 1000
TESTS = 100

(
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
    from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    values = []
    for i in range(SIZE):
        number = Number(i)
        values.append(number)
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
    from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    i = SIZE
    values = []
    while i != 0:
        i -= 1
        number = Number(i)
        values.append(number)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    arrays = []

    for i in range(SIZE):

        col = []
        for i in range(TESTS):
            a = random.randint(0, XRANGE)
            number = Number(a)
            col.append(number)
        arrays.append(col)

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    sorted = create_sorted()
    reverse = create_reversed()
    random = create_randoms()

    Number.comparisons = 0
    Sorts.swaps = 0

    func(sorted)
    sortedSwap = round(Sorts.swaps, 0)
    sortedComp = round(Number.comparisons, 0)

    Sorts.swap = 0
    Number.comparisons = 0

    func(reverse)
    reverseSwap = round(Sorts.swaps, 0)
    reverseComp = round(Number.comparisons, 0)

    Sorts.swap = 0
    Number.comparisons = 0

    randComp = 0
    for i in random:
        func(i)
        randComp += Number.comparisons
        Number.comparisons = 0
    randSwap = round(Sorts.swaps / len(random), 0)
    randComp = round(randComp / len(random), 0)

    print(f"{title}          {sortedComp}     {reverseComp}       {randComp}        {sortedSwap}      {reverseSwap}       {randSwap}")
