import math


def x_main():
    return math.cos(2) ** 2 + 1


def y_main():
    return 3 ** 2 - 1


f = lambda x, y: x() + y()

result = f(x_main, y_main)
print(f'Result for f(x, y): {result}')
