from operator import add, mul

def square(x):
    return mul(x, x)

def pirate(arg):
    print("Matey")
    def plunder(arg):
        return arg
    return plunder

if __name__ == '__main__':
    r1 = add(pirate(3)(square)(4), 1)
    print(r1)
    