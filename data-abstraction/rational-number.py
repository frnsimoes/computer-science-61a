"""
# Data abstraction allo us to separe partes of any program.
# - how data are represented (as parts);
# - how data are manipulated (as unites);

# Data abstraction: a methodology by which functions enforce an abstraction barrier between representation and use.

"""

# Rational arithmetic

def add_rational(x, y):
    """Add rational numbers x and y."""

    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx *dy)

def mul_rational(x, y):
    """Multiply rational numbers x and y"""
    return rational(numer(x * numer(y), denom(x) * denom(y)))

def rationals_are_equal(x, y):
    """Return whether rational numbers x and y are equal"""
    return numer(x) * denom(y) == numer(y) * denom(x)

# Constructor and selectors

def rational(n, d):
    """Construct a rational number x that represents n/d"""
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    """Return the numerator of rational number x."""
    return x('n')

def denom(x):
    """Return the denominator of rational number x"""
    return x('d')
