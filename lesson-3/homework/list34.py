def rotate_list(lst, shift):
    shift = shift % len(lst) if lst else 0
    return lst[-shift:] + lst[:-shift]