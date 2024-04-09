#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked given the keys inside them.

    Args:
    - boxes: A list of lists representing the boxes and their keys.

    Returns:
    - True if all boxes can be unlocked, False otherwise.
    """
    num_boxes = len(boxes)

    visited = set()

    def unlock_boxes(box_index):
        """
        Recursively unlocks boxes starting from the given box index.

        Args:
        - box_index: Index of the box to start unlocking from.
        """
        visited.add(box_index)
        keys = boxes[box_index]

        for key in keys:
            if key not in visited and key < num_boxes:
                unlock_boxes(key)

    unlock_boxes(0)

    return len(visited) == num_boxes
