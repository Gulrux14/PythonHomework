def get_unique_elements_tuple(tpl):
    seen = set()
    return tuple(x for x in tpl if not (x in seen or seen.add(x)))
