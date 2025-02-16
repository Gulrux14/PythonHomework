def second_smallest_tuple(tpl):
    unique_sorted = sorted(set(tpl))
    return unique_sorted[1] if len(unique_sorted) > 1 else None