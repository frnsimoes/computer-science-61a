from euclidian import gcd

if __name__ == '__main__':
    assert gcd(12, 8) == 4
    assert gcd(16, 12) == 4
    assert gcd(16, 8) == 8
    assert gcd(2, 16) == 2
    assert gcd(5, 5) == 5

    