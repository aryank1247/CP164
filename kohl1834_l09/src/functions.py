"""
-------------------------------------------------------
[Functions File]
-------------------------------------------------------
Author:  Aryan Kohli
ID:      169091834
Email:   kohl1834@mylaurier.ca
__updated__ = "2025-03-14"
-------------------------------------------------------
"""


# Functions file implementation with hash_table function
def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash Slot Key
    ----- ---- ------------------------
    1652346 3 Dark City, 1998
    848448 6 Zulu, 1964

    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
        slots - the number of slots available (int > 0)
        values - the values to hash (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    print(f"{'Hashes':<10} {'Slot':<5} {'Key':<30}")
    print(f"{'-'*10} {'-'*5} {'-'*30}")

    result = []
    for value in values:
        h = hash(value)
        slot = h % slots
        result.append(f"{h:<10} {slot:<5} {value}")

    for line in result:
        print(line)
    return

