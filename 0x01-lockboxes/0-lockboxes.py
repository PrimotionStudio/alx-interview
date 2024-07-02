#!/usr/bin/python3
"""Module is fucking documented"""
_boxes = []


def canUnlockAll(boxes):
    """Shit is fucking documented"""
    global _boxes
    _boxes = boxes
    num_of_boxes = len(boxes)
    global visited
    visited = [False] * num_of_boxes
    visit(boxes[0], 0)
    if visited == ([True] * num_of_boxes):
        return True
    return False


def visit(box, index):
    """Shit is fucking documented"""
    if visited[index] is True:
        return
    visited[index] = True
    for key_id in range(len(box)):
        key = box[key_id]
        try:
            visit(_boxes[key], key)
        except IndexError:
            pass
