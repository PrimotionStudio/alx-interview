#!/usr/bin/python3
def canUnlockAll(boxes):
    num_of_boxes = len(boxes)
    visited = [False] * num_of_boxes
    for box in boxes:
        for key in box:
            try:
                if box[key]:
                    print("{} box exists, key was found".format(key))
            except IndexError:
                continue
                