def repeat_elements_tuple(tpl, times):
    return tuple(x for x in tpl for _ in range(times))