#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked 
using their keys.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
        boxes (list of lists): A list where sublists contain keys for box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)  # Total boxes
    unlocked = set([0])  # The first box is default unlocked
    keys = set(boxes[0])  # Keys in the first box

    while keys:
        key = keys.pop()  # Get a key from set
        if key not in unlocked and 0 <= key < n:  # Valid key not unlocked
            unlocked.add(key)  # Mark box unlocked
            keys.update(boxes[key])  # Add new key from this box

    # Return True if all boxes are unlocked
    return len(unlocked) == n


if __name__ == "__main__":
    # Test for canUnlockAll module
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False