def curry_2_args(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

# lambda version
curry_lambda = lambda f: lambda x: lambda y: f(x,y)

if __name__ == '__main__':
    from operator import add
    m = curry_2_args(add)
    add_three = m(3)
    x = add_three(2)
    print(x)