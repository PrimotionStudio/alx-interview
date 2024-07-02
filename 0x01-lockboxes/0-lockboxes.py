#!/usr/bin/python3
_boxes = []
def canUnlockAll(boxes):
    # print(boxes)
    global _boxes
    _boxes = boxes
    num_of_boxes = len(boxes)
    global visited
    visited = [False] * num_of_boxes
    # print(visited)
    # visited(box, index)
    visit(boxes[0], 0)
    # for box_id in range(len(boxes)):
    #     box = boxes[box_id]
    #     print("In box: {}".format(box))
    #     if len(box) == 0:
    #         visited[box_id] = True
    #         continue
    #     for key_id in range(len(box)):
    #         key = box[key_id]
    #         try:
    #             # key === box
    #             if boxes[key]:
    #                 print("box {} exists, key was found in {}".format(boxes[key], box))
    #                 visited[key] = True
    #         except IndexError:
    #             print("box {} exists, key was not found in {}".format(boxes[key], box))
    # print(visited)
    if visited == ([True] * num_of_boxes):
        return True
    return False

def visit(box, index):
    if visited[index] == True:
        return
    # print("Visiting box: {} at index {}".format(box, index))
    visited[index] = True
    # print("Length Box {}".format(len(box)))

    for key_id in range(len(box)):
        key = box[key_id]
        # print("Next Key to look at: {}".format(key))
        try:
            # if _boxes[key]:
            # print("looking at box {}".format(_boxes[key]))
            # print("box {} exists, key was found in {}".format(_boxes[key], box))
            visit(_boxes[key], key)
        except IndexError:
            pass
            # print("box {} exists, key was not found in {}".format(_boxes[key], box))