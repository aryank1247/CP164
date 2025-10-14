"""
-------------------------------------------------------
[Lab 1 Functions file]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-12"
-------------------------------------------------------
"""


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """

    unique = []

    for value in values:

        if value not in unique:
            unique.append(value)

    values.clear()
    values.extend(unique)

    return


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    new_list = []

    for each in minuend:

        if each not in subtrahend:
            new_list.append(each)

    minuend.clear()
    minuend.extend(new_list)

    return


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    upp = low = dig = whi = rem = 0

    for line in fv:
        for char in line:
            if char.isupper():
                upp += 1
            elif char.islower():
                low += 1
            elif char.isdigit():
                dig += 1
            elif char.isspace():
                whi += 1
            else:
                rem += 1

    return upp, low, dig, whi, rem


def find_subs(string, sub):
    """
    Finds the indices of the locations of sub within string,
    left to right. Already used characters are ignored.

    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)

    Returns:
        locations - an ordered list of the indices of the locations
        of sub within string (list of int)
    """
    locations = []
    index = 0
    while index < len(string):
        index = string.find(sub, index)
        if index == -1:
            break
        locations.append(index)
        index += len(sub)  # Move past the current match
    return locations


def is_palindrome(string):
    """
    Determines if a string is a palindrome. Ignores case, spaces, and punctuation in the string.

    Parameters:
        string - a string (str)

    Returns:
        palindrome - True if the string is a palindrome, False otherwise (bool)
    """
    import re
    # Normalize the string by removing non-alphanumeric characters and converting to lowercase
    normalized = re.sub(r'[^a-zA-Z0-9]', '', string).lower()
    return normalized == normalized[::-1]


def median_scores(fv):
    """
    Determines the median of a series of integers in a file.

    Parameters:
        fv - a file variable for an already open file of integers (file)

    Returns:
        median - the median of the values in the file (float)
    """
    numbers = [int(line.strip()) for line in fv]
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2


def matrix_transpose(a):
    """
    Transpose the contents of matrix a.

    Parameters:
        a - a 2D list (list of lists of ?)

    Returns:
        b - the transposed matrix (list of lists of ?)
    """
    return [list(row) for row in zip(*a)]


def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    a must be unchanged.
    Use: b = matrix_flatten(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    return [element for sublist in a for element in sublist]


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrices a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    # Initialize result matrix with zeros
    c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                c[i][j] += a[i][k] * b[k][j]

    return c


def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2D list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    b = [list(row) for row in zip(*a[::-1])]
    return b
