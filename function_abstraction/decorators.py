def trace1(fn):
    def traced(x):
        print('Calling', fn, 'on argument', x)
    return traced


@trace1
def square(x):
    return x * x

def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k +1
    return total

"""
@trace1
def triple(x):
    return 3 * x

is identical to:

triple = trace1(triple)
"""


if __name__ == '__main__':
    square(2)
    square = trace1(square(2))
    