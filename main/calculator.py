def door_kit_compare(door1, door2):
    """compares two doors
    :return: True if doors are equal, otherwise False
    """
    for key, value in door1.items():
        if door1[key] != door2[key]:
            return False
    return True


def kit_dimensions_compare(door1, door2):
    """compares two doors dimensions. It doesn't compare direction!
    :return: True if doors are equal, otherwise False
    """
    for key, value in door1.items():
        if key not in ['direction', 'amount_L', 'amount_R'] and door1[key] != door2[key]:
            return False
    return True
