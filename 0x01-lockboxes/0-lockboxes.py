#!/usr/bin/python3
def canUnlockAll(boxes):
    print(boxes)
    num_of_boxes = len(boxes)
    visited = [False] * num_of_boxes
    visited[0] = True
    print(visited)
    for box_id in range(len(boxes)):
        box = boxes[box_id]
        print("In box: {}".format(box))
        if len(box) == 0:
            visited[box_id] = True
            continue
        for key_id in range(len(box)):
            key = box[key_id]
            try:
                # key === box
                if boxes[key]:
                    print("box {} exists, key was found in {}".format(boxes[key], box))
                    visited[key] = True
            except IndexError:
                print("box {} exists, key was not found in {}".format(boxes[key], box))
    print(visited)

    if visited == ([True] * num_of_boxes):
        return True
    return False