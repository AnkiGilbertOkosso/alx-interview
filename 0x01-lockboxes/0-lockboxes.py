#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Determines whether all boxes in a list of boxes, each containing keys
    to other boxes, can be unlocked, assuming the first box is unlocked.

    :param boxes: A list of lists representing the boxes and their keys.
    :type boxes: list[list[int]]
    :return: True if all boxes can be unlocked, False otherwise.
    :rtype: bool
    '''
    n = len(boxes)
    visited_boxes = set([0])
    unvisited_boxes = set(boxes[0]).difference(set([0]))
    while len(unvisited_boxes) > 0:
        box_idx = unvisited_boxes.pop()
        if not box_idx or box_idx >= n or box_idx < 0:
            continue
        if box_idx not in visited_boxes:
            unvisited_boxes = unvisited_boxes.union(boxes[box_idx])
            visited_boxes.add(box_idx)
    return n == len(visited_boxes)
