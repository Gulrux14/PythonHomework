def get_unique_elements_in_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]