def mean(*args):
    lst = []
    for i in args:
        if type(i) in (int, float):
            lst.append(i)
    if len(lst) == 0:
        return float(0)
    else:
        return sum(lst)/len(lst)