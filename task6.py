def print_products(*args):
    lst = []
    for i in args:
        if type(i) == str and len(i) != 0:
            lst.append(i)
    if len(lst) != 0:
        for i in range(1, len(lst)+1):
            print(str(i) + ')', lst[i-1])
    else:
        print('Нет продуктов')