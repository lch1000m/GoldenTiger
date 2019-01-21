# set list class for list with set property


def list_add(a, b):
    return list(set(a) | set(b))


def list_sub(a, b):
    return list(set(a) - set(b))
