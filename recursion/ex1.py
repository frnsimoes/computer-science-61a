def split(n):
    """split positive n into all but its last digit and its digit
    >>> split(2013)
    >>> (201, 3)
    """
    return n // 10, n % 10

def sum_digits(n):
    """return the sum of the digits of positive integer n"""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        print(all_but_last, last)
        return sum_digits(all_but_last) + last

if __name__ == '__main__':
    print(sum_digits(1989))
    