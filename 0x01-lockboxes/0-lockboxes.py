#!/usr/bin/python3


def canUnlockAll(boxes):
    num_boxes = len(boxes)

    visited = set()

    def unlock_boxes(box_index):
        visited.add(box_index)
        keys = boxes[box_index]

        for key in keys:
            if key not in visited and key < num_boxes:
                unlock_boxes(key)

    unlock_boxes(0)

    return len(visited) == num_boxes
