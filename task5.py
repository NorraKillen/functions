def greet(name, *args):
    a = f'Hello, {name}'
    for i in args:
        a += ' and ' + i
    return a + '!'