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
    satck[0]

    while stack:
        box_index = stack.pop()
        visited.add(box_index)

        keys = boxes[box_index]

        for key in keys:
            if key not in visited and key < num_boxes:
                stack.append(key)
    return len(visited) == num_boxes
