"""
-------------------------------------------------------
Utilities
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-02-01"
-------------------------------------------------------
"""
from Stack_array import Stack


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        item = source.pop()
        stack.push(item)

    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not stack.is_empty():
        item = stack.pop()
        target.insert(0, item)

    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    s = Stack()

    try:
        s.pop()
    except AssertionError:
        print("Pop on empty stack correctly raised an exception.")

    try:
        s.peek()
    except AssertionError:
        print("Peek on empty stack correctly raised an exception.")

    for item in source:
        s.push(item)
        print(f"Pushed {item} onto the stack. Top of stack is now: {s.peek()}")

    print("Test is_empty after pushing:", s.is_empty())

    while not s.is_empty():
        item = s.pop()
        print(f"Popped {item} from the stack.")

    print("Test is_empty after popping all items:", s.is_empty())

    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        queue.insert(source.pop(0))

    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())

    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print("Queue is empty:", q.is_empty())

    for item in a:
        q.insert(item)
        print(f"Inserted {item}. Queue size is now {len(q)}")

    print("Queue is empty after insertions:", q.is_empty())
    print("Peek at front of queue:", q.peek())

    while not q.is_empty():
        print("Removed:", q.remove())

    print("Queue is empty after removals:", q.is_empty())

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        pq.insert(source.pop(0))

    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())

    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print("Priority Queue is empty:", pq.is_empty())

    for item in a:
        pq.insert(item)
        print(f"Inserted {item}. Priority Queue size is now {len(pq)}")

    print("Priority Queue is empty after insertions:", pq.is_empty())
    print("Peek at highest priority:", pq.peek())

    while not pq.is_empty():
        print("Removed:", pq.remove())

    print("Priority Queue is empty after removals:", pq.is_empty())

    return


def array_to_list(llist, source):
    while source:
        llist.append(source.pop(0))


def list_to_array(llist, target):
    while llist._values:
        target.append(llist.remove(llist._values[0]))


def list_test(source):
    lst = List()
    for value in source:
        lst.append(value)
    print("List contents:", lst._values)
    print("List max:", lst.max())
    print("List min:", lst.min())
    print("List count of first element:", lst.count(source[0]) if source else 0)
    print("Is list empty?:", lst.is_empty())
    if not lst.is_empty():
        print("Index of first element:", lst.index(source[0]))
        print("Finding first element:", lst.find(source[0]))
        lst.insert(1, 999)
        print("List after insertion:", lst._values)
        lst.remove(source[0])
        print("List after removal:", lst._values)

