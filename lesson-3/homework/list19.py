def replace_element(lst, old, new):
    if old in lst:
        lst[lst.index(old)] = new
    return lst