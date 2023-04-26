from functools import reduce
def evaluate(coefficients, x):
    lst = range(len(coefficients))[::-1]
    res = list(map(lambda a, b:  b*(x**a), lst, coefficients))
    return reduce(lambda a, b: a+b, res)
coefficients = list(map(int, input().split()))
x = int(input())
print(evaluate(coefficients, x))