def second_largest_tuple(tpl):
    unique_sorted = sorted(set(tpl), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None