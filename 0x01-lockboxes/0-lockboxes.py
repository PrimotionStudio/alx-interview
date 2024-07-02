#!/usr/bin/python3
_boxes = []


def canUnlockAll(boxes):
    global _boxes
    _boxes = boxes
    num_of_boxes = len(boxes)
    global visited
    visited = [False] * num_of_boxes
    visit(boxes[0], 0)
    if visited is ([True] * num_of_boxes):
        return True
    return False


def visit(box, index):
    if visited[index] is True:
        return
    visited[index] = True
    for key_id in range(len(box)):
        key = box[key_id]
        try:
            visit(_boxes[key], key)
        except IndexError:
            pass
