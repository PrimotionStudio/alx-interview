#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes4 = [[1, 2], [3, 4], [0, 5], [], [2], [4, 6], [1]]
print(canUnlockAll(boxes4))

boxes5 = [[2], [3, 5, 7], [1], [4], [6], [7, 0], [8, 9], [10], [11, 12], [13], [14], [15], [16], [17], [18], [19], [20], [], [22], [21]]
print(canUnlockAll(boxes5))

boxes6 = [[1, 3, 5, 7, 9], [2], [4], [6], [8], [10], [], [], [], [], [0]]
print(canUnlockAll(boxes6))

boxes7 = [[], [0, 1, 2, 3], [4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23], [24, 25, 26], [27, 28, 29]]
print(canUnlockAll(boxes7))

boxes8 = [[1], [2, 3], [3, 4, 5], [6, 7, 8], [9], [10, 11], [12, 13, 14], [15, 16, 17], [18, 19], [20, 21, 22], [23, 24, 25]]
print(canUnlockAll(boxes8))