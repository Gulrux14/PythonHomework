def create_nested_tuple(tpl, size):
    return tuple(tpl[i:i+size] for i in range(0, len(tpl), size))