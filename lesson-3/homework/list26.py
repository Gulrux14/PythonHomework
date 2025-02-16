def get_middle_element(lst):
    if not lst:
        return None
    mid = len(lst) // 2
    return lst[mid] if len(lst) % 2 else (lst[mid - 1], lst[mid])