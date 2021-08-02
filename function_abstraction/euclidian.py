def gcd(m, n):
    "returns the largest number that divides both parameters evenly"

    if n % m == 0:
        return m
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m-n, n)