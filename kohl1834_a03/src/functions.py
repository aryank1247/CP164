"""
-------------------------------------------------------
[Functions file]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-01-26"
-------------------------------------------------------
"""

from Stack_array import Stack


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = []
    target2 = []
    i = 1
    while not source.is_empty():
        if i % 2 != 0:
            target1.append(source.pop())
        else:
            target2.append(source.pop())
        i += 1
    return target1, target2


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    chars = ""
    for s in string:
        if s.isalpha():
            chars += s.lower()

    l = len(chars)
    mid = -1
    if l == 0:
        palindrome = True
    else:
        mid = l // 2
        first_half = Stack()
        for i in range(mid):
            first_half.push(chars[i])
        if l % 2 == 0:
            second_half_chars = chars[mid:]
        else:
            second_half_chars = chars[mid + 1:]
        second_half_chars = second_half_chars.lower()
        i = 0
        while palindrome and i < mid:
            s = second_half_chars[i]
            p = first_half.pop()
            if s == p:
                i += 1
            else:
                palindrome = False
    return palindrome


# Constants
OPERATORS = "+-*/"
NUMBERS = "12356890"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    elements = string.split()
    for e in elements:
        if e not in OPERATORS:
            stack.push(e)
        else:
            top = float(stack.pop())
            second = float(stack.pop())
            if e == "+":
                stack.push(second + top)
            elif e == "-":
                stack.push(second - top)
            elif e == "*":
                stack.push(second * top)
            else:
                stack.push(second / top)
    answer = stack.pop()
    return answer


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """

    temp_stack = Stack()

    while not source.is_empty():
        temp_stack.push(source.pop())

    while not temp_stack.is_empty():
        source.push(temp_stack.pop())

    return


def reroute(opstring, values_in):
    """
    Reroutes values in a list according to an operation string and
    returns a new list of values. values_in is unchanged.

    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)

    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - If opstring is valid, then values_out contains a
                     reordered version of values_in; otherwise returns
                     None (list of ?)
    """
    stack = []
    values_out = []
    input_index = 0  # Tracks the current index of values_in

    for op in opstring:
        if op == 'S':
            if input_index >= len(values_in):  # Validate input list bounds
                return None
            stack.append(values_in[input_index])
            input_index += 1
        elif op == 'X':
            if not stack:  # Validate stack is not empty
                return None
            values_out.append(stack.pop())
        else:
            # Invalid character in opstring
            return None

    # Check if all inputs were consumed and outputs are valid
    if input_index != len(values_in):
        return None

    return values_out
