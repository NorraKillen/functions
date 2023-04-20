def func_apply(func, lst):
    l = []
    for item in lst:
        l.append(func(item))
    return l