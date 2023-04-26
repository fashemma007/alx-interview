#!/usr/bin/python3

def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked"""
    unlocked = [0]  # store all boxes that's been unlocked
    # loop and get the index and content of each box i.e inner list
    for box_index, box in enumerate(boxes):
        # print(f"Keys in box {box_index} can unlock boxes => {box}")
        if not box:  # if box is empty skip it
            continue
        for key in box:
            # print(f"🔑 for box {key} found in 🥡 {box_index}")
            # check if the key falls within box range
            key_valid = (key < len(boxes))
            # check if the key is not already in the list
            key_missing = (key not in unlocked)
            # check if the key isnt a duplicate to open current box
            key_not_for_current_box = (key != box_index)
            all_checks = key_valid and key_missing and key_not_for_current_box
            # if all conditions are met
            if all_checks:
                # print(f"🥡 {key} can now be unlocked")
                # add the key to the unlocked box
                unlocked.append(key)
                # print(unlocked)
            # else:
                # print(f"Duplicate 🔑 {key} found in 🥡 {box_index}")
    # after all iterations, check if all boxes were unlocked
    return True if len(unlocked) == len(boxes) else False
