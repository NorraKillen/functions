def info_kwargs(**kwargs):
    lst = []
    for key, value in kwargs.items():
        lst.append(key + ': ' + str(value))
    lst.sort()
    for i in lst:
        print(i)