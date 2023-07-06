#!/usr/bin/python3

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)


def main():
    # Test cases
    boxes1 = [[1], [2], [3], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 2], [3, 4], [0, 3], [], []]
    print(canUnlockAll(boxes2))  # False

    boxes3 = [[1], [2], [3], [], [4]]
    print(canUnlockAll(boxes3))  # False

    boxes4 = [[1], [2], [3], [4], [5]]
    print(canUnlockAll(boxes4))  # True


if __name__ == "__main__":
    main()

